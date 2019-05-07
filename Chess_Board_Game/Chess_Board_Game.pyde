# Name: Muhammad Wajahat Mirza (mwm356) and Abraham Okbasslaise Hdru (ah3300)
# Date: May 6th 2019
# Description : Final Project Chess

import os 
path = os.getcwd()

num_rows = 8 
num_cols = 8 
cell_height = 64
cell_width  = 64

class Rook:
    def __init__(self, x, y):
        self.x, self.y = self.convertCoord(x,y)

    def convertCoord(self,x,y):
        return x*64,y*64

    def display_rook(self):
        white_rook_img  = loadImage(path + "/images/white_rook.png")
        black_rook_img  = loadImage(path + "/images/black_rook.png")
        image(white_rook_img, self.x,self.y,cell_width,cell_height)
    
    def move(self, x,y):
        self.x, self.y = self.convertCoord(x,y)
        self.display_rook()
    
    def check_valid(self):
        pass
    

class Chess_board:
    def __init__(self, num_rows, num_cols):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.game_over = False
    
        self.chess_grid = []                  # this is to initialize a grid on the screen
        for row in range(self.num_rows):
            self.chess_row = []               # to iterate through each row
            for col in range(self.num_cols):
                self.chess_row.append(0)
            self.chess_grid.append(self.chess_row) 
        print(self.chess_grid)                # for test purposes
    
    def display_background(self):
        pos_x = 0
        pos_y = 0 
        for row in range(num_rows):
            for col in range(num_cols):
                if (col + row) % 2 == 1: 
                 # Algorithm. The even-ness or odd-ness of the sum of row and col has same color          
                    cell_A_img = loadImage(path + "/images/white.png") 
                    image(cell_A_img, pos_x,pos_y,cell_width,cell_height)
                    pos_x += 64
                else:
                    cell_B_img = loadImage(path + "/images/black.png")
                    image(cell_B_img, pos_x,pos_y,64,64)
                    pos_x += 64
            pos_x  = 0
            pos_y += 64

    def display_rook(self):
        rook1 = Rook(0,0)
        rook1.display_rook()
        rook2 = Rook(7,0)
        rook2.display_rook()
    
   # # def add_chess_pieces(self):
   #      white_pawn_img   = loadImage(path + "/images/white_pawn.png")
   #      white_rook_img   = loadImage(path + "/images/white_rook.png")
   #      white_knight_img = loadImage(path + "/images/white_knight.png")
   #      white_bishop_img = loadImage(path + "/images/white_bishop.png")
   #      white_queen_img  = loadImage(path + "/images/white_queen.png")
   #      white_king_img   = loadImage(path + "/images/white_king.png")
        
   #      image(white_rook_img, 0,0,cell_width,cell_height)
        
        
chess_grid = Chess_board(num_rows, num_cols) 
  
def setup():
    size(num_rows * cell_height, num_cols * cell_width)
    #background(155)

def draw():
    chess_grid.display_background()
    #chess_grid.add_chess_pieces()
    chess_grid.display_rook()
    #background(155)
