# Name: Muhammad Wajahat Mirza (mwm356) and Abraham Okbasslaise Hdru (ah3300)
# Date: May 6th 2019
# Description : Final Project Chess

import os 
path = os.getcwd()

num_rows = 8 
num_cols = 8 
cell_height = 64
cell_width  = 64

class Chess:
    def __init__(self, row, col): 
        self.row = row 
        self.col = col 
        self.chess_board_img = loadImage(path + "/images/brown_dark.png")
        
    def display(self):
        image(self.chess_board_img, self.col * cell_width, self.row * cell_height)

class Board:
    def __init__(self):
        self.num_rows = num_rows
        self._num_cols = num_cols
        
        self.chess_grid = []
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                self.board.append(Chess(row, col))
    
def setup():
    size(num_rows * cell_height, num_cols*cell_width)
    background(155)

def draw():
    background(155)
