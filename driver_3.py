import sys
import argparse
import csp



def solutionStr(csp):
        solution = ''
        for key, value in csp.items():
            solution = solution + str(value[0])
        return solution
    
    
def writeOutput(output):
    with open('output.txt', 'a') as myfile:
        myfile.write(output + '\n')
        

    
def RunCSP(csp):
    assignment = AC3(csp)
    if assignment:
        return csp.solutionStr() + ' AC3'
    assignment = BTS(csp)
    return ' BTS'



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('b', type=str)
    args = parser.parse_args()
    board = csp(args.b)
    writeOutput(RunCSP(board))
            

if __name__ == "__main__":
	main()
