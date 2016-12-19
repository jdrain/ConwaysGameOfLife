Implementation of [Conway's Game Of
Life](https://en.wikipedia.org/wiki/Conway's_Game_of_Life)

Right now, this is pretty basic, but it functions well as far as I am
aware.

Planned additions:
    +GUI/Display of some sort. Right now we just have the data in arrays
of binary and it'd be great to have something available for better
visualization
    +Functionality to create cool structures like
[gliders and guns](https://en.wikipedia.org/wiki/Conway's_Game_of_Life#Examples_of_patterns)
    +Functionality to do calculations with the game

Classes:
    +Square; is either on or off
    +Board; collection of squares. 2D. Calculates the next iterations of
the board
    +Game; collection of boards, each of which is determined by the
previous one, per the rules of the game
