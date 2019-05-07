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
        return x * cell_width,y * cell_height

    def display_w_rook(self):
        white_rook_img  = loadImage(path + "/images/white_rook.png")
        image(white_rook_img, self.x,self.y,cell_width,cell_height)
    
    def display_b_rook(self):
        black_rook_img  = loadImage(path + "/images/black_rook.png")
        image(black_rook_img, self.x,self.y,cell_width,cell_height)
        
    def move(self, x,y):
        self.x, self.y = self.convertCoord(x,y)
        self.display_rook()
    
    def check_valid(self):
        pass
    
class Knight:
    def __init__(self, x, y):
        self.x, self.y = self.convertCoord(x,y)

    def convertCoord(self,x,y):
        return x * cell_width,y * cell_height
    
    def display_w_knight(self):
        white_knight_img  = loadImage(path + "/images/white_knight.png")
        image(white_knight_img, self.x,self.y,cell_width,cell_height)
    
    def display_b_knight(self):
        black_knight_img  = loadImage(path + "/images/black_knight.png")
        image(black_knight_img, self.x,self.y,cell_width,cell_height)
    
    
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
                    pos_x += cell_width
                else:
                    cell_B_img = loadImage(path + "/images/black.png")
                    image(cell_B_img, pos_x,pos_y,cell_width,cell_height)
                    pos_x += cell_width
            pos_x  = 0
            pos_y += cell_height

    def display_rook(self):
        rook_w1 = Rook(0,0)
        rook_w1.display_w_rook()
        rook_w2 = Rook(7,0)
        rook_w2.display_w_rook()
        
        rook_b1 = Rook(0,7)
        rook_b1.display_b_rook()
        rook_b2 = Rook(7,7)
        rook_b2.display_b_rook()
    
    def display_knight(self):
        knight_w1 = Knight(1,0)
        knight_w1.display_w_knight()
        knight_w2 = Knight(6,0)
        knight_w2.display_w_knight()
        
        knight_b1 = Knight(1,7)
        knight_b1.display_b_knight()
        knight_b2 = Knight(6,7)
        knight_b2.display_b_knight()
        
    
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
    chess_grid.display_knight()
    #background(155)
