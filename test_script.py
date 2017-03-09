from board import board
from game import game
import time
import sys

#get user args for board size and game length
if len(sys.argv) != 3:
    print("use is of the form: python test_script.py <board size> <game length>\n")
else:
    b=board(int(sys.argv[1]))
    b.randomize()
    print("Randomized board: ")
    b.display()
    time.sleep(.5)
    g=game(int(sys.argv[2]),b,[])
    g.construct_game()
    g.display()
