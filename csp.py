import sys
import itertools
from collections import Counter
import operator


class csp:
    def __init__(self, nput):
        self.nput = nput
        self.alphaList = 'ABCDEFGHI'
        self.numbeList = '123456789'
        
        self.board = {}
        self.createBoard()

        self.constraints= []
        self.createConstraints()
        
        self.neighbors = {}
        self.createNeighbors()

        self.unassigned = {}
        
        

    ###########################################################################
    # Create Empty Board with IDs
    # Assign Domains to Empty Board
    # Create Unassigned List for BTS
    
    def createBoard(self):
        self.emptyBoard=[]
        for x in self.alphaList:
            for y in self.numbeList:
                self.emptyBoard.append(x+y)
        self.assignBoard()


    def assignBoard(self):
        for x in range(0, len(self.emptyBoard)):
            if self.nput[x] == '0':
                domain = list(range(1,10))
            else:
                domain = self.nput[x]
                domain = [int(domain)]
            self.board.update({self.emptyBoard[x]: domain})


    def createUnassignment(self):
        for x in range(0, len(self.emptyBoard)):
            if self.nput[x] == '0':
                domain = list()
            else:
                domain = self.nput[x]
                domain = [int(domain)]
            self.unassigned.update({self.emptyBoard[x]: domain})
            
        
    ####################################
    # 1. Create Row Constraints
    # 2. Create Column Constraints
    # 3. Create Cube Lists
    # 4. Create Cube Constraints
    # 5. Create Neighbors

        
    def createConstraints(self):
        for x in self.emptyBoard:
            for y in self.emptyBoard:
                if x!=y and x[0]==y[0]:
                    self.constraints.append([x, y])
                    
        self.createColumnConstraints()
                    
                    
    def createColumnConstraints(self):
        for x in self.emptyBoard:
            for y in self.emptyBoard:
                if x!=y and x[1]==y[1]:
                    self.constraints.append([x, y])

        self.createCubes()

    def createCubes(self):
        self.cubes=[]
        for x in ['ABC', 'DEF', 'GHI']:
            for n in ['123', '456', '789']:
                cube=[]
                for a in x:
                    for b in n:
                        cube.append(a+b)
                self.cubes.append(cube)
        self.createCubeConstraints()
                        
    
    def createCubeConstraints(self):
        for cube in self.cubes:
            for x in cube:
                for y in cube:
                    if x != y and [x, y] not in self.constraints:
                        self.constraints.append([x, y])
    
    def createNeighbors(self):
        for x in self.board:
            self.neighbors[x] = list()
            for c in self.constraints:
                if x == c[0]:
                    self.neighbors[x].append(c[1])



    ###################################################################
    # Backtrack Functions:
    # 1. MRV - returns key with least values in domain
    # 2. LCV - returns sorted list of values from least occurences
    # 3. consistant - returns bool true if value is not assigned to neighbor
    # 4. forwardChecking - removes val from neighbor domain and creates inference

    def MRV(self, assignment):
        newBoard = {key: value for key, value in self.board.items() if key not in assignment}
        for k in sorted(newBoard, key=lambda k: len(newBoard[k])):
            return k

    def LCV(self, var):
        if len(self.board[var]) == 1:
            return self.board[var]
        
        neighbors = {key: value for key, value in self.board.items() if key in self.neighbors[var]}
        c = Counter()
        for x in neighbors.values():
            c.update(set(x))
        Counter(c.values())
        rank = {key: value for key, value in c.items() if key in self.board[var]}
        return [x[0] for x in sorted(rank.items(), key=operator.itemgetter(1))]


    def consistent(self, assignment, var, value):
        for key, val in assignment.items():
            if val == value and key in self.neighbors[var]:
                consistent = False
        return True

    def forwardChecking(self, assignment, var, value):
        for n in self.neighbors[var]:
            if n not in assignment and value in self.board[n]:
                self.board[n].remove(value)
                self.unassigned[var].append((n, value))

        
    def reassign(self, var, assignment):
        for x in self.unassigned[var]:
            self.board[x[0]].append(x[1])
        
        



    ###########################################################################
    # Check If puzzle is solved for AC3
    # Check if Assignment is complete
    # Create Output String of Solved Puzzle

    def solved(self):
        return sum(len(v) for k, v in self.board.items()) == 81

    def complete(self, assignment):
        for x in self.emptyBoard:
            if x in assignment:
                continue
            else: return False
        return True

    
    def solutionStr(self):
        solution = ''
        for x in self.emptyBoard:
            self.board[x]
            solution = solution + str(self.board[x][0])
        return solution

    
            

    
            

        




