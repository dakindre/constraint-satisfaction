import sys
import csp
from collections import deque


########################################
# AC3
########################################

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




########################################
# BackTracking
########################################
def complete(assignment, csp):
    for key in csp.board.items():
        if key in assignment:
            continue
        else: return False
    return True

def BackTrackingSearch(csp):
    return backtrack({}, csp)



def backtrack(assignment, csp):
    if complete(assignment, csp):
        return assignment
    var = csp.minimumRemainingVariable()
    for value in csp.orderDomainValues(var, assignment):
        if consistant(value, assignment):
            
