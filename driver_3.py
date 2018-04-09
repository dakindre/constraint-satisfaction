import sys
import argparse


class SudokuBoard:
    def __init__(self, nput):
        self.nput = nput
        self.board ={}
        self.alphaList = ['A','B','C','D','E','F','G','H','I']
        self.numbeList = ['1','2','3','4','5','6','7','8','9']
        self.boredSkeleton()
        self.createBored()
        

    def boredSkeleton(self):
        self.boardList=[]
        for x in self.alphaList:
            for y in self.numbeList:
                self.boardList.append(x+y)


    def createBored(self):
        for x in self.nput:
            self.board.update({self.boardList[x]: self.nput[x]})
        print(self.board)
            

    

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('b', type=str)

    args = parser.parse_args()
    
    board = SudokuBoard(args.b)

if __name__ == "__main__":
	main()
