from board import board
from game import game
import time

b=board(50)
b.randomize()
print("Randomized board: ")
b.display()
time.sleep(.5)
g=game(500,b,[])
g.construct_game()
g.display()
