from square import square
from random import randint

class board:

    def __init__(self, size):
        #instantiate blank board
        ls=[[square(1) for i in range(0,size)] for j in range(0,size)]
        self.size = size
        self.board = ls

    def construct(self,board_ls):
        self.size=len(board_ls)
        self.board=board_ls

    def randomize(self):
        for i in range(0,self.size):
            for j in range(0,self.size):
                self.board[i][j]=square(randint(0,1))

    def display(self):
        for i in range(0,self.size):
            s=[
                "x" if self.board[i][j].status == 1 else " " for j in range(0,self.size)
              ]

            print(" ".join(s))

    def neighbor_count(self,i,j):
        #if i is 0 or self.size
        #if j is 0 or self.size
        #if both
        count=0
        if i==0:
            if j==0:
                #top left corner
                count+=self.board[i][j+1].status
                count+=self.board[i+1][j+1].status
                count+=self.board[i+1][j].status
            elif j==self.size-1:
                #top right corner
                count+=self.board[i][j-1].status
                count+=self.board[i+1][j-1].status
                count+=self.board[i+1][j].status
            else:
                #somewhere in the first row
                count+=self.board[i][j-1].status
                count+=self.board[i][j+1].status
                count+=self.board[i+1][j-1].status
                count+=self.board[i+1][j].status
                count+=self.board[i+1][j+1].status
        elif i==self.size-1:
            if j==0:
                #bottom left corner
                count+=self.board[i][j+1].status
                count+=self.board[i-1][j+1].status
                count+=self.board[i-1][j].status
            elif j==self.size-1:
                #bottom right corner
                count+=self.board[i-1][j-1].status
                count+=self.board[i-1][j].status
                count+=self.board[i][j-1].status
            else:
                #somewhere in the last row
                count+=self.board[i][j-1].status
                count+=self.board[i][j+1].status
                count+=self.board[i-1][j-1].status
                count+=self.board[i-1][j].status
                count+=self.board[i-1][j+1].status
        else:
            if j==0:
                #somewhere in the first column
                count+=self.board[i][j+1].status
                count+=self.board[i-1][j].status
                count+=self.board[i-1][j+1].status
                count+=self.board[i+1][j].status
                count+=self.board[i+1][j+1].status
            elif j==self.size-1:
                #somewhere in the last column
                count+=self.board[i][j-1].status
                count+=self.board[i-1][j].status
                count+=self.board[i-1][j-1].status
                count+=self.board[i+1][j].status
                count+=self.board[i+1][j-1].status
            else:
                #somewhere in the middle
                count+=self.board[i][j-1].status
                count+=self.board[i][j+1].status
                count+=self.board[i-1][j-1].status
                count+=self.board[i-1][j].status
                count+=self.board[i-1][j+1].status
                count+=self.board[i+1][j-1].status
                count+=self.board[i+1][j].status
                count+=self.board[i+1][j+1].status
        return count

    def calculate_next_board(self):
        """
        calculate the next board based on conway's rules:
        +if a cell is alive
            -it survives if it has two or three neighbors
            -it dies if it has four or more neighbors
        +if a cell is dead
            -it becomes alive if it has three neighbors
        """

        next_board_ls=[[0 for i in range(0,self.size)] for j in range(0,self.size)]
        for i in range(0,self.size):
            for j in range(0,self.size):
                neighbor_count=self.neighbor_count(i,j)
                if self.board[i][j].status==1:
                    if neighbor_count==2 or neighbor_count==3:
                        next_board_ls[i][j]=square(1)
                    else:
                        next_board_ls[i][j]=square(0)
                else:
                    if neighbor_count==3:
                        next_board_ls[i][j]=square(1)
                    else:
                        next_board_ls[i][j]=square(0)
        next_board=board(10)
        next_board.construct(next_board_ls)
        return next_board
