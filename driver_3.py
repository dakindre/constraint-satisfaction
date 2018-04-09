import sys
import argparse
import itertools

    

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
            else: domain = self.nput[x]
            
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
        
            
def ac3(sudoku):

    queue = list(sudoku.constraints)

    while queue:

        xi, xj = queue.pop(0)

        if revise(sudoku, xi, xj):

            if len(sudoku.domains[xi]) == 0:
                return False

            for xk in sudoku.neighbors[xi]:
                if xk != xi:
                    queue.append([xk, xi])

    return True

    
def revise(sudoku, xi, xj):

    revised = False

    for x in sudoku.domains[xi]:
        if not any([sudoku.constraint(x, y) for y in sudoku.domains[xj]]):
            sudoku.domains[xi].remove(x)
            revised = True

    return revised


def backtrack(assignment, sudoku):

    if len(assignment) == len(sudoku.variables):
        return assignment

    var = select_unassigned_variable(assignment, sudoku)

    for value in order_domain_values(sudoku, var):

        if sudoku.consistent(assignment, var, value):

            sudoku.assign(var, value, assignment)

            result = backtrack(assignment, sudoku)
            if result:
                return result

            sudoku.unassign(var, assignment)

    return False


# Most Constrained Variable heuristic
# Pick the unassigned variable that has fewest legal values remaining.
def select_unassigned_variable(assignment, sudoku):
    unassigned = [v for v in sudoku.variables if v not in assignment]
    return min(unassigned, key=lambda var: len(sudoku.domains[var]))


# Least Constraining Value heuristic
# Prefers the value that rules out the fewest choices for the neighboring variables in the constraint graph.
def order_domain_values(sudoku, var):
    if len(sudoku.domains[var]) == 1:
        return sudoku.domains[var]

    return sorted(sudoku.domains[var], key=lambda val: sudoku.conflicts(sudoku, var, val))



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('b', type=str)

    args = parser.parse_args()
    
    board = csp(args.b)

    if ac3(board):
        if board.solved():
            print(board.board)

        else:

            assignment = {}

            for x in sudoku.variables:
                if len(sudoku.domains[x]) == 1:
                    assignment[x] = sudoku.domains[x][0]

            assignment = backtrack(assignment, sudoku)

            for d in sudoku.domains:
                sudoku.domains[d] = assignment[d] if len(d) > 1 else sudoku.domains[d]

            if assignment:

                print(board.board)

            else:
                print ("No solution exists")
            

if __name__ == "__main__":
	main()
