# GameOfLife-Levesque-CDOF1
Simple python implementation of the famous game by mathematician John Horton Conway : the "Game of Life".

## Getting Started

### Prerequisites
Dependencies (basic python libraries)
```
 - Random
 - Time
```

Installing
```
All libraries should already be installed. If it's not the case, they can be found here :
https://www.python.org/downloads/
```

### Installing

Python need to be installed

```
Download Python from https://www.python.org/downloads
```

To run the code :
```
First, import the necessary libraries (code given)
Then, run the GamOfLife class.
Finally, run the run_game function definition.
Use this function to run the simulation, shoosing the size of the map beforehand.
```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Inspiration was taken from this code, by mwharrisjr, available on github : https://github.com/mwharrisjr/Game-of-Life/blob/master/script/main.py

## "The Game of Life" : A simple yet profound simulation

The Game of Life, described by mathematician John Horton Conway in 1970, is a cellular automaton that simulates the evolution of patterns on a two-dimensional grid based on simple rules. Each cell in the grid can be in one of two states: alive or dead. At each generation the number of living cells and average lifetime of a cell is displayed. The state of each cell in the next generation is determined by the states of its eight neighboring cells, following these rules:

    Underpopulation: A living cell with fewer than two living neighbors dies.
    Survival: A living cell with two or three living neighbors continues to live.
    Overpopulation: A living cell with more than three living neighbors dies.
    Reproduction: A dead cell with exactly three living neighbors becomes alive.

Even though very simple, some interesting patterns found in the Game of Life can be related to patterns found in living organisms. The following study examines those parallels between the Game of Life and biological processes.
https://www.frontiersin.org/journals/cellular-and-infection-microbiology/articles/10.3389/fcimb.2016.00057/full?utm_source=chatgpt.com
