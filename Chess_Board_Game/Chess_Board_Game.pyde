# Name: Muhammad Wajahat Mirza (mwm356) and Abraham Okbasslaise Hdru (ah3300)
# Date: May 6th 2019
# Description : Final Project Chess

import os 
path = os.getcwd()

num_rows = 8 
num_cols = 8 
cell_height = 64
cell_width  = 64

class Piece:
    def __init__(self, x, y, img_path):
        self.x, self.y = self.convertCoord(x,y)
        self.img_path = img_path

    def convertCoord(self,x,y):
        return x * cell_width,y * cell_height
   
    def display_w_pieces(self):
        white_img  = loadImage(path + "/images/" + self.img_path + ".png")
        image(white_img, self.x,self.y,cell_width,cell_height)
    
    def display_b_pieces(self):
        black_img  = loadImage(path + "/images/" + self.img_path + ".png")
        image(black_img, self.x,self.y,cell_width,cell_height)
    
class Rook(Piece):
    pass 

class Knight(Piece):
    pass

class Bishop(Piece):
    pass

class Queen(Piece):
    pass 

class King(Piece):
    pass
    
class Pawn(Piece):
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
                    pos_x += cell_width
                else:
                    cell_B_img = loadImage(path + "/images/black.png")
                    image(cell_B_img, pos_x,pos_y,cell_width,cell_height)
                    pos_x += cell_width
            pos_x  = 0
            pos_y += cell_height

    def display_rook(self):
        rook_w1 = Rook(0,0, "white_rook")
        rook_w1.display_w_pieces()
        rook_w2 = Rook(7,0, "white_rook")
        rook_w2.display_w_pieces()
        
        rook_b1 = Rook(0,7, "black_rook")
        rook_b1.display_b_pieces()
        rook_b2 = Rook(7,7,"black_rook")
        rook_b2.display_b_pieces()
    
    def display_knight(self):
        knight_w1 = Knight(1,0, "white_knight")
        knight_w1.display_w_pieces()
        knight_w2 = Knight(6,0,"white_knight")
        knight_w2.display_w_pieces()
        
        knight_b1 = Knight(1,7, "black_knight")
        knight_b1.display_b_pieces()
        knight_b2 = Knight(6,7, "black_knight")
        knight_b2.display_b_pieces()
    
    def display_bishop(self):
        bishop_w1 = Bishop(2,0, "white_bishop")
        bishop_w1.display_w_pieces()
        bishop_w1 = Bishop(5,0, "white_bishop")
        bishop_w1.display_w_pieces()
        
        bishop_b1 = Bishop(2,7, "black_bishop")
        bishop_b1.display_b_pieces()
        bishop_b1 = Bishop(5,7, "black_bishop")
        bishop_b1.display_b_pieces()
        
    def display_queen(self):
        queen_w = Queen(3,0, "white_queen")
        queen_w.display_w_pieces()
        
        queen_b = Queen(3,7, "black_queen")
        queen_b.display_b_pieces()
        
    def display_king(self):
        king_w = King(4,0, "white_king")
        king_w.display_w_pieces()
        
        king_b = King(4,7, "black_king")
        king_b.display_b_pieces()
        
    def display_pawn(self):
        for i in range(num_cols):
            pawn_w = Pawn(i,1, "white_pawn")
            pawn_w.display_w_pieces()
        
        for j in range(num_cols):
            pawn_b = Pawn(j,6, "black_pawn")
            pawn_b.display_b_pieces()
        
chess_grid = Chess_board(num_rows, num_cols) 
  
def setup():
    size(num_rows * cell_height, num_cols * cell_width)

def draw():
    chess_grid.display_background()
    chess_grid.display_rook()
    chess_grid.display_knight()
    chess_grid.display_bishop()
    chess_grid.display_queen()
    chess_grid.display_king()
    chess_grid.display_pawn()

def mouseClicked(self):
    col = mouseX // cell_width
    row = mouseY // cell_height
    print("clicked at "  + str(row) + " " + str(col))
    
