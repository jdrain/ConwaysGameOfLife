from board import board
import time

class game:

    def __init__(self,length,initial_board,game):
        self.length=length
        self.initial_board=initial_board
        self.game=[self.initial_board if i==0 else None for i in range(0,self.length)]

    def construct_game(self):
        for i in range(0,self.length-1):
            self.game[i+1]=self.game[i].calculate_next_board()

    def display(self):
        print("\033c")
        for i in range(0,self.length):
            print("\033c")
            self.game[i].display()
            time.sleep(.2)
