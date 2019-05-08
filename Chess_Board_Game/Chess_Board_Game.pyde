# Name: Muhammad Wajahat Mirza (mwm356) and Abraham Okbasslaise Hdru (ah3300)
# Date: May 6th 2019
# Description : Final Project Chess

import os 
path = os.getcwd()

num_rows = 8 
num_cols = 8 
cell_height = 64
cell_width  = 64

class Pieces:
    def __init__(self, x, y, img_path):
        self.x, self.y = self.convertCoord(x,y)
        self.img_path = img_path

    def convertCoord(self,x,y):
        return x * cell_width,y * cell_height
   
    def display_pieces(self):
        piece_img  = loadImage(path + "/images/" + self.img_path + ".png")
        image(piece_img, self.x,self.y,cell_width,cell_height)
    
class Rook(Pieces):
    pass 

class Knight(Pieces):
    pass

class Bishop(Pieces):
    pass

class Queen(Pieces):
    pass 

class King(Pieces):
    pass
    
class Pawn(Pieces):
    pass
    
class Chess_board:
    def __init__(self, num_rows, num_cols, ):#pieces
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
        
        self.pieces = self.create_pieces()
        
    def create_pieces(self):
        pieces = []
        for i in range(num_cols):
            pawn_w = Pawn(i,1, "white_pawn")
            pieces.append(pawn_w)

        rock_white_left = Rook(0,0, "white_rock") 
        pieces.append(rock_white_left)
        rock_white_right = Rook(7,0, "white_rock")
        pieces.append(rock_white_right)
        
        knight_white_left =Knight(1,0, "white_knight")
        pieces.append(knight_white_left)
        knight_white_right =Knight(6,0, "white_knight")
        pieces.append(knight_white_right)
        
        bishop_white_left = Bishop(2,0, "white_bishop")
        pieces.append(bishop_white_left)
        bishop_white_right = Bishop(5,0, "white_bishop")
        pieces.append(bishop_white_right)
        
        queen_white = Queen(3,0, "white_queen")
        pieces.append(queen_white)
        king_white =King(4,0, "king_white") 
        pieces.append(king_white)
        
        for j in range(num_cols):
            pawn_b = Pawn(j,6, "black_pawn")
            pieces.append(pawn_b)
       
        rock_black_left = Rook(0,7, "black_rock") 
        pieces.append(rock_black_left)
        rock_black_right = Rook(7,7, "black_rock")
        pieces.append(rock_black_right)
        
        knight_black_left =Knight(1,7, "black_knight")
        pieces.append(knight_black_left)
        knight_black_right =Knight(6,7, "black_knight")
        pieces.append(knight_black_right)
        
        bishop_black_left = Bishop(2,7, "black_bishop")
        pieces.append(bishop_black_left)
        bishop_black_right = Bishop(5,7, "black_bishop")
        pieces.append(bishop_black_right)
        
        queen_black = Queen(3,7, "black_queen")
        pieces.append(queen_black)
        king_black =King(4,7, "black_white") 
        pieces.append(king_black)
         
        
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
    
    def display(self, piece, coords):
        color = ["white_" + piece, "black_" + piece]
        counter = 0 
        num = len(coords)
        limit = num // 2
        
        for i in coords:
            if counter < limit:
                tempStr = "{}({}, {}, '{}')".format(piece.capitalize(), i[0], i[1], color[0])
                eval(tempStr).display_pieces()
            else:
                tempStr = "{}({}, {}, '{}')".format(piece.capitalize(), i[0], i[1], color[1])
                eval(tempStr).display_pieces()
            counter += 1 
    
    def display_pawn(self):
        for i in range(num_cols):
            pawn_w = Pawn(i,1, "white_pawn")
            pawn_w.display_pieces()
        
        for j in range(num_cols):
            pawn_b = Pawn(j,6, "black_pawn")
            pawn_b.display_pieces()
    
    
    
    
chess_grid = Chess_board(num_rows, num_cols) #pieces
  
def setup():
    size(num_rows * cell_height, num_cols * cell_width)

def draw():
    chess_grid.display_background()
    chess_grid.display("rook", [[0,0],[7,0],[0,7],[7,7]])
    chess_grid.display("knight", [[1,0],[6,0],[1,7],[6,7]])
    chess_grid.display("bishop", [[2,0],[5,0],[2,7],[5,7]])
    chess_grid.display("queen", [[3,0],[3,7]])
    chess_grid.display("king", [[4,0],[4,7]])
    
    #chess_grid.update()
    
    chess_grid.display_pawn()

def mouseClicked(self):
    col = mouseX // cell_width
    row = mouseY // cell_height
    print("clicked at "  + str(row) + " " + str(col))

    
    
# class Moves (Pieces, Chess_board):
#     def __init__(self, Rock, Knight,Bishop, Queen, King, Pawn): 
#         self.Rock = Rock 
#         self.Knight = Knight 
#         self.Bishop = Bishop 
#         self.Queen = Queen 
#         self.King = King 
#         self.Pawn = Pawn 
        
#     def RockMoves(num_rows, num_cols)  
