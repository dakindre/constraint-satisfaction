import sys
import argparse
import itertools
from collections import deque
from copy import deepcopy

    

class csp:
    def __init__(self, nput):
        self.nput = nput
        self.board = {}
        self.alphaList = 'ABCDEFGHI'
        self.numbeList = '123456789'
        self.constraints = []
        self.neighbors = {}
        self.boardSkeleton()
        self.createConstraints()
        self.build_neighbors()
        
        

    def boardSkeleton(self):
        self.emptyBoard=[]
        for x in self.alphaList:
            for y in self.numbeList:
                self.emptyBoard.append(x+y)
        self.createBoard()


    def createBoard(self):
        for x in range(0, len(self.emptyBoard)):
            if self.nput[x] == '0':
                domain = list(range(1,10))
            else:
                domain = self.nput[x]
                domain = [int(domain)]
            
            self.board.update({self.emptyBoard[x]: domain})
        
            

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

    def build_neighbors(self):

        for x in self.board:
            self.neighbors[x] = list()
            for c in self.constraints:
                if x == c[0]:
                    self.neighbors[x].append(c[1])

    def permutate(self, iterable):
        result = list()

        for L in range(0, len(iterable) + 1):
            if L == 2:
                for subset in itertools.permutations(iterable, L):
                    result.append(subset)

        return result

    def combine(self, alpha, beta):
        return [a + b for a in alpha for b in beta]

    def solved(self):
        for key, value in self.board.items():
            if len(value)>1: return False
        return True
        
    def solutionStr(self):
        solution = ''
        for key, value in self.board.items():
            solution = solution + str(value[0])

        return solution
            
            
def AC3(csp):

    queue = deque()
    for x in csp.constraints:
       queue.append(x)
    

    while queue:
        
        xi, xj = queue.popleft()
        

        if revise(csp, str(xi), str(xj)):
            

            if len(csp.board[xi]) == 0:
                return False

            for xk in csp.neighbors[xi]:
                if xk != xi:
                    queue.append([xk, xi])

    return True

    
def revise(csp, xi, xj):

    revised = False

    for x in csp.board[xi]:
        count = 0
        for y in csp.board[xj]:
            if x != y:
                count += count+1
        if count == 0:
            csp.board[xi].remove(x)
            revised = True

    return revised


def constraint(xi, xj): return xi != xj


'''def backtrack(assignment, csp):

    if len(assignment) == len(csp.variables):
        return assignment

    var = select_unassigned_variable(assignment, csp)

    for value in order_domain_values(csp, var):

        if sudoku.consistent(assignment, var, value):

            sudoku.assign(var, value, assignment)

            result = backtrack(assignment, sudoku)
            if result:
                return result

            sudoku.unassign(var, assignment)

    return False



def select_unassigned_variable(assignment, csp):
    unassigned = [v for v in csp.variables if v not in assignment]
    return min(unassigned, key=lambda var: len(csp.domains[var]))



def order_domain_values(csp, var):
    if len(csp.domains[var]) == 1:
        return csp.domains[var]

    return sorted(csp.domains[var], key=lambda val: csp.conflicts(csp, var, val))'''

def writeOutput(output):
    with open('output.txt', 'a') as myfile:
        myfile.write(output + '\n')
        

    
def RunCSP(board):
    assignment = AC3(board)
    if board.solved():
        return board.solutionStr() + ' AC3'
    #assignment = BTS(board)
    return ' BTS'



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('b', type=str)

    args = parser.parse_args()
    
    board = csp(args.b)

    writeOutput(RunCSP(board))

            

if __name__ == "__main__":
	main()
