import sys
import argparse
import csp as c
from collections import deque
from copy import deepcopy


###########################################################################
# AC3 Algorithm
#   Returns Success/Failure
# Revision function to remove unwanted values in domain
#   Returns True if value removed

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



###########################################################################
# backtracking - assigning values to keys in assignment
#   Return: Assignment/False


def backtrack(assignment, csp):
    if csp.complete(assignment):
        return assignment

    var = csp.MRV(assignment)
    
    for value in csp.LCV(var):
        if csp.consistent(assignment, var, value):
            assignment[var] = value
            csp.forwardChecking(assignment, var, value)
            result = backtrack(assignment, csp)
            if result:
                return result
            
            if var in assignment:
                csp.reassign(var, assignment)
                csp.unassigned[var]= []
                del assignment[var]

    return False           





###########################################################################
# Write Output String to file
# Main Function

def writeOutput(output):
    with open('output.txt', 'a') as myfile:
        myfile.write(output + '\n')


def main():
    #Import Puzzle to be solved
    parser = argparse.ArgumentParser()
    parser.add_argument('b', type=str)
    args = parser.parse_args()

    #Create Initial State Board
    csp = c.csp(args.b)

    #Run AC3/BackTrack
    if(AC3(csp)):
        if csp.solved():
            writeOutput(csp.solutionStr() + ' AC3')

        else:
            csp.createUnassignment()
            n = {key: value[0] for key, value in csp.board.items() if len(value) == 1}
            assignment = backtrack(n, csp)
            
            if isinstance(assignment, dict):
                for key, value in assignment.items():
                    csp.board[key] = [value]
                writeOutput(csp.solutionStr() + ' BTS')

        

            

if __name__ == "__main__":
	main()
