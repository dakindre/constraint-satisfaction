import sys
import itertools
from collections import Counter


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
        
            
    ####################################
    # Fix
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

    ###########################################################################

    def minimumRemainingVariable(self):
        for key, value in self.board.items:
            minV = 10
            if len(value) > 1 and len(value) < minV:
                minV = len(value)
                minK = key
            else: continue
        return minK

    def orderDomainValues(self, var, assignment):
        c = Counter()
        for x in self.board.itervalues():
            c.update(set(v))
        Counter(c.values())
            

    unassigned = [v for v in sudoku.variables if v not in assignment]
    return min(unassigned, key=lambda var: len(sudoku.domains[var]))
            

        




