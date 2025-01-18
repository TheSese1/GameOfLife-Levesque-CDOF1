# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 14:09:06 2025

@author: Sebastien
"""

#%% Introduction

# Game of Life implementation:
# The famous game by mathematician John Horton Conway.
# To make it console based,
# you can use spaces for dead cells and █ for live cells.

#%% Imports
import random as rd
import time

#%% Implementation

class Game_of_life:
    def __init__(self, size=10, seed=None):
        if seed is not None:
            # Given squared seed: (0=dead, 1=alive)
            self.grid = seed
            self.size = len(seed)
        else:
            # Random generation of a seed based on the size: (0=dead, 1=alive)
            self.grid = [[rd.choice([0, 1]) for _ in range(size)] for _ in range(size)]
            self.size = size
        
        # Variable pour suivre la durée de vie des cellules
        self.cell_lifetimes = [[0 for _ in range(self.size)] for _ in range(self.size)]
    
    def print_game(self):
        dic = {0: ' ', 1: '█'}
        for row in self.grid:
            print("".join(dic[cell] for cell in row))
    
    def get_live_neighbors(self, row, col):
        """
        Counts the number of live cells surrounding a center cell at grid[row][cell].
        """
        life_sum = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if not (i == 0 and j == 0):  # Ignore the current cell
                    life_sum += self.grid[(row + i) % self.size][(col + j) % self.size]
        return life_sum

    def next_grid(self):
        """
        Analyzes the current generation and determines the next state of the grid.
        """
        next_grid_ = [[0 for _ in range(self.size)] for _ in range(self.size)]
        for row in range(self.size):
            for col in range(self.size):
                live_neighbors = self.get_live_neighbors(row, col)
                if live_neighbors < 2 or live_neighbors > 3:
                    next_grid_[row][col] = 0  # Cell dies
                elif live_neighbors == 3:
                    next_grid_[row][col] = 1  # Cell becomes alive
                else:
                    next_grid_[row][col] = self.grid[row][col]  # Cell state unchanged
        
        # Update cell lifetimes
        self.update_lifetimes(next_grid_)
        self.grid = next_grid_
        return next_grid_

    def update_lifetimes(self, next_grid_):
        """
        Updates the lifetime of cells.
        """
        for row in range(self.size):
            for col in range(self.size):
                if next_grid_[row][col] == 1:
                    self.cell_lifetimes[row][col] += 1
                else:
                    self.cell_lifetimes[row][col] = 0

    def count_alive(self):
        """
        Counts the number of alive cells in the grid.
        """
        return sum(sum(row) for row in self.grid)

    def average_lifetime(self):
        """
        Calculates the average lifetime of living cells.
        """
        live_cells = [self.cell_lifetimes[row][col]
                      for row in range(self.size)
                      for col in range(self.size)
                      if self.grid[row][col] == 1]
        return sum(live_cells) / len(live_cells) if live_cells else 0


#%% Run game

def run_game(seed=None):
    # Generations initialization
    generation = "None"
    while not generation.isdigit() or int(generation) < 1:
        generation = input("Enter a number of iterations greater than 1: ")
        if not generation.isdigit():
            print("Invalid input. Please enter a valid integer.")
    
    # Size initialization (only if random seed)
    if seed is None:
        size = "None"
        while not size.isdigit() or int(size) < 2:
            size = input("Enter a size greater than 2: ")
            if not size.isdigit():
                print("Invalid input. Please enter a valid integer.")
    else:
        size = len(seed)

    # Initialization
    generation = int(generation)
    size = int(size)
    game = Game_of_life(size, seed)
    
    print("Generation : 0")
    print(f"{game.count_alive()} alive cells")
    print(f"Average lifetime: {game.average_lifetime():.2f}")
    game.print_game()
    current_state = game.grid
    time.sleep(0.5)

    # Run the Game of Life sequence
    for gen in range(1, generation + 1):
        print(f"\nGeneration : {gen}")
        # Next state
        next_state = game.next_grid()
        print(f"{game.count_alive()} alive cells")
        print(f"Average lifetime: {game.average_lifetime():.2f}")
        game.print_game()
        # verif change
        if next_state == current_state:
            break

        current_state = next_state
        time.sleep(0.5)


#%% Examples

# Random seed
run_game(None)

# Given seed, with 1 blinker
seed = [[0, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 0, 0]]
run_game(seed)

# Given seed, with 1 spaceship
seed = [[0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]]
run_game(seed)
