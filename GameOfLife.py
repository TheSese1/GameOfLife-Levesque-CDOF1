# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 14:09:06 2025

@author: Sebastien
"""


#%% Introduction

# Game of Life implementation :
# The famous game by mathematician John Horton Conway. 
# To make it console based, 
# you can use spaces for dead cells and # for live cells.

#%% Imports
import numpy as np
import random as rd
import os
import sys
import time

#%% Implementation

class Game_of_life:
    def __init__(self, size:int):
        # random generation of a seed : (0=dead, 1=alive)
        self.grid = [[rd.choice([0, 1]) for _ in range(size)] for _ in range(size)]
        self.size = size
    
    def clear_console():
        """
        Clears the console using a system command based on the user's operating system.
    
        """
    
        if sys.platform.startswith('win'):
            os.system("cls")
        elif sys.platform.startswith('linux'):
            os.system("clear")
        elif sys.platform.startswith('darwin'):
            os.system("clear")
        else:
            print("Unable to clear terminal. Your operating system is not supported.\n\r")
    
    def print_game(self):
        dic = {0:' ', 1:'█'}
        for l in self.grid:
            for ele in l:
                print(dic[ele], end='')
            print()
    
    def get_live_neighbors(self, row, col):
        """
        Counts the number of live cells surrounding a center cell at grid[row][cell].
        """
        life_sum = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if not (i == 0 and j == 0):
                    # Using the modulo operator (%) the grid wraps around
                    life_sum += self.grid[((row + i) % self.size)][((col + j) % self.size)]
        return life_sum

    
    def next_grid(self):
        """
        Analyzes the current generation of the Game of Life grid and determines what cells live and die in the next
        generation of the Game of Life grid.
        """
        next_grid_ = [[' ' for _ in range(self.size)] for _ in range(self.size)]
        for row in range(self.size):
            for col in range(self.size):
                # Get the number of live cells adjacent to the cell at grid[row][col]
                live_neighbors = self.get_live_neighbors(row, col)
    
                # If the number of surrounding live cells is < 2 or > 3 then we make the cell at grid[row][col] a dead cell
                if live_neighbors < 2 or live_neighbors > 3:
                    next_grid_[row][col] = 0
                # If the number of surrounding live cells is 3 and the cell at grid[row][col] was previously dead then make
                # the cell into a live cell
                elif live_neighbors == 3 and self.grid[row][col] == 0:
                    next_grid_[row][col] = 1
                # If the number of surrounding live cells is 3 and the cell at grid[row][col] is alive keep it alive
                else:
                    next_grid_[row][col] = self.grid[row][col]
        
        self.grid = next_grid_
        return next_grid_
    
    def count_alive(self):
        """
        Counts the number of alive cells in a
        """
        counter = 0
        for l in self.grid:
            for i in l:
                if i==1:
                    counter += 1
        return counter

#%% Run game

def run_game(size:int, generations:int):
    # Initialization
    game = Game_of_life(size)
    print("Generation : 0")
    print(game.count_alive(), " alive cells")
    game.print_game()
    current_state = game.grid
    
    # Run Game of Life sequence
    for gen in range(1, generations + 1):
        print("Generation :", gen)
        # next state
        next_state = game.next_grid()
        # printing grid
        print(game.count_alive(), " alive cells")
        game.print_game()
        # verif change
        if next_state == current_state:
            break
    
        time.sleep(1 / 5.0)

run_game(10, 10)
