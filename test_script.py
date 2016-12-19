from board import board
from game import game

b=board(10)
b.display()
b.randomize()
print("Randomized board: ")
b.display()
g=game(10,20,b,[])
g.construct_game()
g.display()
