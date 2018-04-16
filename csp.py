import sys
import itertools
from collections import Counter


class csp:
    def __init__(self, nput):
        self.nput = nput
        self.alphaList = 'ABCDEFGHI'
        self.numbeList = '123456789'
        
        self.board = {}
        self.createBoard()
        
        self.constraints = []
        self.createConstraints()
        
        self.neighbors = {}
        self.build_neighbors()

        self.pruned = {}
        
        

    ###########################################################################
    # Create Empty Board with IDs
    # Assign Domains to Empty Board
    
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


    def createPrune(self):
        for x in range(0, len(self.emptyBoard)):
            if self.nput[x] == '0':
                domain = list()
            else:
                domain = self.nput[x]
                domain = [int(domain)]
            self.pruned.update({self.emptyBoard[x]: domain})
            
        
    ####################################
    #

    #Bad
    def createConstraints(self):
        blocks = (
            [self.combine(self.alphaList, number) for number in self.numbeList] +
            [self.combine(character, self.numbeList) for character in self.alphaList] +
            [self.combine(character, number) for character in ('ABC', 'DEF', 'GHI') for number in ('123', '456', '789')])

        for block in blocks:
            combinations = self.permutate(block)
            for combination in combinations:
                if [combination[0], combination[1]] not in self.constraints:
                    self.constraints.append([combination[0], combination[1]])

    #Bad
    def build_neighbors(self):

        for x in self.board:
            self.neighbors[x] = list()
            for c in self.constraints:
                if x == c[0]:
                    self.neighbors[x].append(c[1])

    #Bad
    def permutate(self, iterable):
        result = list()

        for L in range(0, len(iterable) + 1):
            if L == 2:
                for subset in itertools.permutations(iterable, L):
                    result.append(subset)

        return result

    #Bad
    def combine(self, alpha, beta):
        return [a + b for a in alpha for b in beta]

    




    ###################################################################
    # Backtrack Functions:
    # 1. MRV - returns key with least values in domain
    # 2. LCV - returns sorted list of values from least occurences
    # 3. consistant - returns bool true if value is not assigned to neighbor
    # 4. forwardChecking - removes val from neighbor domain and creates inference

    #Good
    def MRV(self, assignment):
        newBoard = {key: value for key, value in self.board.items() if key not in assignment}
        for k in sorted(newBoard, key=lambda k: len(newBoard[k])):
            return k

    #Bad
    def LCV(self, var):
        neighbors = {key: value for key, value in self.board.items() if key in self.neighbors[var]}
        c = Counter()
        for x in neighbors.values():
            c.update(set(x))
        Counter(c.values())
        print(neighbors)
        print(c)
        sort = sorted(c.values())
        print(sort)
        


    



    #Bad
    def conflicts(self, var, val):

        count = 0

        for n in self.neighbors[var]:
            if len(self.board[n]) > 1 and val in self.board[n]:
                count += 1

        return count
    
    



    #Bad
    def consistent(self, assignment, var, value):
        consistent = True

        for key, val in assignment.items():
            if val == value and key in self.neighbors[var]:
                consistent = False

        return consistent

    #Bad
    def assign(self, var, value, assignment):

        assignment[var] = value

        self.forwardChecking(var, value, assignment)

        
    #Bad
    def unassign(self, var, assignment):

        if var in assignment:

            for (D, v) in self.pruned[var]:
                self.board[D].append(v)

            self.pruned[var] = []

            del assignment[var]

    #Bad
    def forwardChecking(self, var, value, assignment):
        for neighbor in self.neighbors[var]:
            if neighbor not in assignment:
                if value in self.board[neighbor]:
                    self.board[neighbor].remove(value)
                    self.pruned[var].append((neighbor, value))


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
        for value in self.board.values():
            solution = solution + str(value[0])
        return solution

        

'''    def createAssignment(self):
        for key, value in self.board.items():
            if len(value) == 1:
                self.assignment[key] = value[0]'''
    
    
            

    
            

        




