from board import board

class game:

    def __init__(self,game_size,length,initial_board,game):
        self.game_size=game_size
        self.length=length
        self.initial_board=initial_board
        self.game=[self.initial_board if i==0 else None for i in range(0,self.length)]

    def construct_game(self):
        for i in range(0,self.length-1):
            self.game[i+1]=self.game[i].calculate_next_board()

    def display(self):
        for i in range(0,self.length):
            print("Game No. " + str(i) + ":")
            self.game[i].display()
