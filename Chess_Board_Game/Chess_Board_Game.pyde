# Name: Muhammad Wajahat Mirza (mwm356) and Abraham Okbasslaise Hdru (ah3300)
# Date: May 6th 2019
# Description : Final Project Chess

import os 
path = os.getcwd()
#add library("minim")
#audio_track = Minim(this)

num_rows = 8 
num_cols = 8 
cell_height = 64
cell_width  = 64

class Pieces:                                       # This is the base class
    def __init__(self, x, y, img_path, color):
        self.color = color
        self.x, self.y = x, y
        self.img_path = img_path
       # self.backend_game_sound = audio_track.loadFile(path + "/sounds/chessbackground") # Need to download sound tracks

    def convertCoord(self,x,y):                      # convert the coordinates 
        return x * cell_width,y * cell_height
   
    def display_pieces(self):
        piece_img  = loadImage(path + "/images/" + self.img_path + ".png")       # this will load images
        x, y = self.convertCoord(self.x, self.y)
        image(piece_img, x, y, cell_width, cell_height)                          # This loads images at x,y position
    
class Rook(Pieces):                                  
    def __init__(self, x, y, img_path, color):
        Pieces.__init__(self, x, y, img_path, color)
        
    def possible_moves(self):                        # This checks all the possible moves from the given position of the piece           
        possible_moves = []
        offset = 1
        while(True):                                 # This loop checks moves on x_increment plane/scale               
            if not chess_grid.piece_inside_board(self.y,self.x + offset):
                break
            if(chess_grid.get_piece(self.y,self.x + offset) == 0):
                possible_moves.append([self.y,self.x + offset])
            elif chess_grid.get_piece(self.y,self.x + offset).color != self.color:
                possible_moves.append([self.y,self.x + offset])
                break
            else:
                break
            offset += 1
            
        offset = 1
        while(True):                                 # This loop checks moves on x_decrement plane/scale
            if not chess_grid.piece_inside_board(self.y,self.x - offset):
                break
            if(chess_grid.get_piece(self.y,self.x - offset) == 0):
                possible_moves.append([self.y,self.x - offset])
            elif chess_grid.get_piece(self.y,self.x - offset).color != self.color:
                possible_moves.append([self.y,self.x - offset])
                break
            else:
                break
            offset += 1
            
        offset = 1
        while(True):                                 # This loop checks moves on y_increment plane/scale
            if not chess_grid.piece_inside_board(self.y + offset,self.x):
                break
            if(chess_grid.get_piece(self.y + offset,self.x) == 0):
                possible_moves.append([self.y + offset,self.x])
            elif chess_grid.get_piece(self.y + offset,self.x).color != self.color:
                possible_moves.append([self.y + offset,self.x])
                break
            else:
                break
            offset += 1
            
        offset = 1
        while(True):                                 # This loop checks moves on y_decrement plane/scale
            if not chess_grid.piece_inside_board(self.y - offset,self.x):
                break
            if(chess_grid.get_piece(self.y - offset,self.x) == 0):
                possible_moves.append([self.y - offset,self.x])
            elif chess_grid.get_piece(self.y - offset,self.x).color != self.color:
                possible_moves.append([self.y - offset,self.x])
                break
            else:
                break
            offset += 1
        return possible_moves
            
class Knight(Pieces):
    def __init__(self, x, y, img_path,color):
        Pieces.__init__(self, x, y, img_path,color)
        
    def possible_moves(self):
        possible_moves = []
        
        offset_y = 1
        offset_x = 2
        while(True):                                 # This loop checks moves on y_decrement, x_decrement plane/scale
            if not chess_grid.piece_inside_board(self.y - offset_y,self.x - offset_x):
                break
            if(chess_grid.get_piece(self.y - offset_y,self.x - offset_x) == 0):
                possible_moves.append([self.y - offset_y,self.x - offset_x])
                break
            elif chess_grid.get_piece(self.y - offset_y,self.x - offset_x).color != self.color:
                possible_moves.append([self.y - offset_y,self.x - offset_x])
                break
            else:
                break
        
        offset_y = 1
        offset_x = 2
        while(True):                                 # This loop checks moves on y_increment, x_increment plane/scale
            if not chess_grid.piece_inside_board(self.y + offset_y,self.x + offset_x):
                break
            if(chess_grid.get_piece(self.y + offset_y,self.x + offset_x) == 0):
                possible_moves.append([self.y + offset_y,self.x + offset_x])
                break
            elif chess_grid.get_piece(self.y + offset_y,self.x + offset_x).color != self.color:
                possible_moves.append([self.y + offset_y,self.x + offset_x])
                break
            else:
                break
        
        offset_y = 1
        offset_x = 2
        while(True):                                 # This loop checks moves on y_decrement, x_increment plane/scale
            if not chess_grid.piece_inside_board(self.y - offset_y,self.x + offset_x):
                break
            if(chess_grid.get_piece(self.y - offset_y,self.x + offset_x) == 0):
                possible_moves.append([self.y - offset_y,self.x + offset_x])
                break
            elif chess_grid.get_piece(self.y - offset_y,self.x + offset_x).color != self.color:
                possible_moves.append([self.y - offset_y,self.x + offset_x])
                break
            else:
                break
        
        offset_y = 1
        offset_x = 2
        while(True):                                 # This loop checks moves on y_increment, x_decrement plane/scale
            if not chess_grid.piece_inside_board(self.y + offset_y,self.x - offset_x):
                break
            if(chess_grid.get_piece(self.y + offset_y,self.x - offset_x) == 0):
                possible_moves.append([self.y + offset_y,self.x - offset_x])
                break
            elif chess_grid.get_piece(self.y + offset_y,self.x - offset_x).color != self.color:
                possible_moves.append([self.y + offset_y,self.x - offset_x])
                break
            else:
                break
        
        offset_y = 2
        offset_x = 1
        while(True):                                 # This loop checks moves on y_decrement, x_decrement plane/scale
            if not chess_grid.piece_inside_board(self.y - offset_y,self.x - offset_x):
                break
            if(chess_grid.get_piece(self.y - offset_y,self.x - offset_x) == 0):
                possible_moves.append([self.y - offset_y,self.x - offset_x])
                break
            elif chess_grid.get_piece(self.y - offset_y,self.x - offset_x).color != self.color:
                possible_moves.append([self.y - offset_y,self.x - offset_x])
                break
            else:
                break
        
        offset_y = 2
        offset_x = 1
        while(True):                                 # This loop checks moves on y_decrement, x_increment plane/scale
            if not chess_grid.piece_inside_board(self.y - offset_y,self.x + offset_x):
                break
            if(chess_grid.get_piece(self.y - offset_y,self.x + offset_x) == 0):
                possible_moves.append([self.y - offset_y,self.x + offset_x])
                break
            elif chess_grid.get_piece(self.y - offset_y,self.x + offset_x).color != self.color:
                possible_moves.append([self.y - offset_y,self.x + offset_x])
                break
            else:
                break
        offset_y = 2
        offset_x = 1
        while(True):                                 # This loop checks moves on y_increment, x_increment plane/scale
            if not chess_grid.piece_inside_board(self.y + offset_y,self.x + offset_x):
                break
            if(chess_grid.get_piece(self.y + offset_y,self.x + offset_x) == 0):
                possible_moves.append([self.y + offset_y,self.x + offset_x])
                break
            elif chess_grid.get_piece(self.y + offset_y,self.x + offset_x).color != self.color:
                possible_moves.append([self.y + offset_y,self.x + offset_x])
                break
            else:
                break
            
        offset_y = 2
        offset_x = 1
        while(True):                                 # This loop checks moves on y_increment, x_decrement plane/scale
            if not chess_grid.piece_inside_board(self.y + offset_y,self.x - offset_x):
                break
            if(chess_grid.get_piece(self.y + offset_y,self.x - offset_x) == 0):
                possible_moves.append([self.y + offset_y,self.x - offset_x])
                break
            elif chess_grid.get_piece(self.y + offset_y,self.x - offset_x).color != self.color:
                possible_moves.append([self.y + offset_y,self.x - offset_x])
                break
            else:
                break
        return possible_moves    
    
class Bishop(Pieces):
    def __init__(self, x, y, img_path,color):
        Pieces.__init__(self, x, y, img_path,color)
    
    def possible_moves(self): 
        possible_moves = []
        
        offset_y = 1
        offset_x = 1
        while(True):                                 # This loop checks moves on y_increment, x_increment plane/scale
            if not chess_grid.piece_inside_board(self.y + offset_y,self.x + offset_x):
                break
            if(chess_grid.get_piece(self.y + offset_y,self.x + offset_x) == 0):
                possible_moves.append([self.y + offset_y,self.x + offset_x])
            elif chess_grid.get_piece(self.y + offset_y,self.x + offset_x).color != self.color:
                possible_moves.append([self.y + offset_y,self.x + offset_x])
                break
            else:
                break
            offset_y += 1
            offset_x += 1
        
        offset_y = 1
        offset_x = 1
        while(True):                                 # This loop checks moves on y_decrement, x_decrement plane/scale
            if not chess_grid.piece_inside_board(self.y - offset_y,self.x - offset_x):
                break
            if(chess_grid.get_piece(self.y - offset_y,self.x - offset_x) == 0):
                possible_moves.append([self.y - offset_y,self.x - offset_x])
            elif chess_grid.get_piece(self.y - offset_y,self.x - offset_x).color != self.color:
                possible_moves.append([self.y - offset_y,self.x - offset_x])
                break
            else:
                break
            offset_y += 1
            offset_x += 1
       
        offset_y = 1
        offset_x = 1
        while(True):                                 # This loop checks moves on y_increment, x_decrement plane/scale
            if not chess_grid.piece_inside_board(self.y + offset_y,self.x - offset_x):
                break
            if(chess_grid.get_piece(self.y + offset_y,self.x - offset_x) == 0):
                possible_moves.append([self.y + offset_y,self.x - offset_x])
            elif chess_grid.get_piece(self.y + offset_y,self.x - offset_x).color != self.color:
                possible_moves.append([self.y + offset_y,self.x - offset_x])
                break
            else:
                break
            offset_y += 1
            offset_x += 1
        
        offset_y = 1
        offset_x = 1
        while(True):                                 # This loop checks moves on y_decrement, x_increment plane/scale
            if not chess_grid.piece_inside_board(self.y - offset_y,self.x + offset_x):
                break
            if(chess_grid.get_piece(self.y - offset_y,self.x + offset_x) == 0):
                possible_moves.append([self.y - offset_y,self.x + offset_x])
            elif chess_grid.get_piece(self.y - offset_y,self.x + offset_x).color != self.color:
                possible_moves.append([self.y - offset_y,self.x + offset_x])
                break
            else:
                break
            offset_y += 1
            offset_x += 1
        return possible_moves
        
class Queen(Pieces):
    def __init__(self, x, y, img_path,color):
        Pieces.__init__(self, x, y, img_path,color)
        
    def possible_moves(self): 
        possible_moves = []
        
        offset = 1
        while(True):                                  # This loop checks moves on x_increment plane/scale
            if not chess_grid.piece_inside_board(self.y,self.x + offset):
                break
            if(chess_grid.get_piece(self.y,self.x + offset) == 0):
                possible_moves.append([self.y,self.x + offset])
            elif chess_grid.get_piece(self.y,self.x + offset).color != self.color:
                possible_moves.append([self.y,self.x + offset])
                break
            else:
                break
            offset += 1
            
        offset = 1
        while(True):                                  # This loop checks moves on x_decrement plane/scale
            if not chess_grid.piece_inside_board(self.y,self.x - offset):
                break
            if(chess_grid.get_piece(self.y,self.x - offset) == 0):
                possible_moves.append([self.y,self.x - offset])
            elif chess_grid.get_piece(self.y,self.x - offset).color != self.color:
                possible_moves.append([self.y,self.x - offset])
                break
            else:
                break
            offset += 1
            
        offset = 1
        while(True):                                   # This loop checks moves on y_increment plane/scale
            if not chess_grid.piece_inside_board(self.y + offset,self.x):
                break
            if(chess_grid.get_piece(self.y + offset,self.x) == 0):
                possible_moves.append([self.y + offset,self.x])
            elif chess_grid.get_piece(self.y + offset,self.x).color != self.color:
                possible_moves.append([self.y + offset,self.x])
                break
            else:
                break
            offset += 1
            
        offset = 1
        while(True):                                  # This loop checks moves on y_decrement plane/scale
            if not chess_grid.piece_inside_board(self.y - offset,self.x):
                break
            if(chess_grid.get_piece(self.y - offset,self.x) == 0):
                possible_moves.append([self.y - offset,self.x])
            elif chess_grid.get_piece(self.y - offset,self.x).color != self.color:
                possible_moves.append([self.y - offset,self.x])
                break
            else:
                break
            offset += 1
            
        offset_y = 1
        offset_x = 1
        while(True):                                  # This loop checks moves on y_increment, x_increment plane/scale
            if not chess_grid.piece_inside_board(self.y + offset_y,self.x + offset_x):
                break
            if(chess_grid.get_piece(self.y + offset_y,self.x + offset_x) == 0):
                possible_moves.append([self.y + offset_y,self.x + offset_x])
            elif chess_grid.get_piece(self.y + offset_y,self.x + offset_x).color != self.color:
                possible_moves.append([self.y + offset_y,self.x + offset_x])
                break
            else:
                break
            offset_y += 1
            offset_x += 1
        
        offset_y = 1
        offset_x = 1
        while(True):                                  # This loop checks moves on y_decrement, x_decrement plane/scale
            if not chess_grid.piece_inside_board(self.y - offset_y,self.x - offset_x):
                break
            if(chess_grid.get_piece(self.y - offset_y,self.x - offset_x) == 0):
                possible_moves.append([self.y - offset_y,self.x - offset_x])
            elif chess_grid.get_piece(self.y - offset_y,self.x - offset_x).color != self.color:
                possible_moves.append([self.y - offset_y,self.x - offset_x])
                break
            else:
                break
            offset_y += 1
            offset_x += 1
       
        offset_y = 1
        offset_x = 1
        while(True):                                  # This loop checks moves on y_increment, x_decrement plane/scale
            if not chess_grid.piece_inside_board(self.y + offset_y,self.x - offset_x):
                break
            if(chess_grid.get_piece(self.y + offset_y,self.x - offset_x) == 0):
                possible_moves.append([self.y + offset_y,self.x - offset_x])
            elif chess_grid.get_piece(self.y + offset_y,self.x - offset_x).color != self.color:
                possible_moves.append([self.y + offset_y,self.x - offset_x])
                break
            else:
                break
            offset_y += 1
            offset_x += 1
        
        offset_y = 1
        offset_x = 1
        while(True):                                  # This loop checks moves on y_decrement, x_increment plane/scale
            if not chess_grid.piece_inside_board(self.y - offset_y,self.x + offset_x):
                break
            if(chess_grid.get_piece(self.y - offset_y,self.x + offset_x) == 0):
                possible_moves.append([self.y - offset_y,self.x + offset_x])
            elif chess_grid.get_piece(self.y - offset_y,self.x + offset_x).color != self.color:
                possible_moves.append([self.y - offset_y,self.x + offset_x])
                break
            else:
                break
            offset_y += 1
            offset_x += 1
        return possible_moves

class King(Pieces):
    def __init__(self, x, y, img_path,color):
        Pieces.__init__(self, x, y, img_path,color)
        
    def possible_moves(self):
        print("King") 
        possible_moves = []
        
        offset_x = 1
        while(True):                                 # This loop checks moves on x_increment plane/scale
            if not chess_grid.piece_inside_board(self.y,self.x + offset_x):
                print("this is loop 1 a test")
                break
            if(chess_grid.get_piece(self.y,self.x + offset_x) == 0):
                print("this is loop 1 b test")
                possible_moves.append([self.y,self.x + offset_x])
                break
            elif chess_grid.get_piece(self.y,self.x + offset_x).color != self.color:
                print("this is loop 1 c test")
                possible_moves.append([self.y,self.x + offset_x])
                break
            else:
                break
        
        offset_x = 1
        while(True):                                  # This loop checks moves on x_decrement plane/scale
            if not chess_grid.piece_inside_board(self.y,self.x - offset_x):
                print("this is loop 2a  test")
                break
            if(chess_grid.get_piece(self.y,self.x - offset_x) == 0):
                print("this is loop 2b  test")
                possible_moves.append([self.y,self.x - offset_x])
                break
            elif chess_grid.get_piece(self.y,self.x - offset_x).color != self.color:
                print("this is loop 2c  test")
                possible_moves.append([self.y,self.x - offset_x])
                break
            else:
                break
        
        offset_y = 1
        while(True):                                 # This loop checks moves on y_decrement plane/scale
            if not chess_grid.piece_inside_board(self.y - offset_y,self.x):
                break
            if(chess_grid.get_piece(self.y - offset_y,self.x) == 0):
                possible_moves.append([self.y - offset_y,self.x])
                break
            elif chess_grid.get_piece(self.y - offset_y,self.x).color != self.color:
                possible_moves.append([self.y - offset_y,self.x])
                break
            else:
                break
        
        offset_y = 1
        while(True):                                 # This loop checks moves on y_increment plane/scale
            if not chess_grid.piece_inside_board(self.y + offset_y,self.x):
                break
            if(chess_grid.get_piece(self.y + offset_y,self.x) == 0):
                possible_moves.append([self.y + offset_y,self.x])
                break
            elif chess_grid.get_piece(self.y + offset_y,self.x).color != self.color:
                possible_moves.append([self.y + offset_y,self.x])
                break
            else:
                break
        
        offset_y = 1
        offset_x = 1
        while(True):                                  # This loop checks moves on x_increment,y_decrement plane/scale
            if not chess_grid.piece_inside_board(self.y - offset_y,self.x + offset_x):
                break
            if(chess_grid.get_piece(self.y - offset_y,self.x + offset_x) == 0):
                possible_moves.append([self.y - offset_y,self.x + offset_x])
                break
            elif chess_grid.get_piece(self.y - offset_y,self.x + offset_x).color != self.color:
                possible_moves.append([self.y - offset_y,self.x + offset_x])
                break
            else:
                break
        
        offset_y = 1
        offset_x = 1
        while(True):                                  # This loop checks moves on x_decrement,y_decrement plane/scale
            if not chess_grid.piece_inside_board(self.y - offset_y,self.x - offset_x):
                break
            if(chess_grid.get_piece(self.y - offset_y,self.x - offset_x) == 0):
                possible_moves.append([self.y - offset_y,self.x - offset_x])
                break
            elif chess_grid.get_piece(self.y - offset_y,self.x - offset_x).color != self.color:
                possible_moves.append([self.y - offset_y,self.x - offset_x])
                break
            else:
                break
        
        offset_y = 1
        offset_x = 1
        while(True):                                  # This loop checks moves on y_increment,x_decrement plane/scale
            if not chess_grid.piece_inside_board(self.y + offset_y,self.x - offset_x):
                break
            if(chess_grid.get_piece(self.y + offset_y,self.x - offset_x) == 0):
                possible_moves.append([self.y + offset_y,self.x - offset_x])
                break
            elif chess_grid.get_piece(self.y + offset_y,self.x - offset_x).color != self.color:
                possible_moves.append([self.y + offset_y,self.x - offset_x])
                break
            else:
                break
        
        offset_y = 1
        offset_x = 1
        while(True):                                  # This loop checks moves on x_increment,y_increment plane/scale
            if not chess_grid.piece_inside_board(self.y + offset_y,self.x + offset_x):
                break
            if(chess_grid.get_piece(self.y + offset_y,self.x + offset_x) == 0):
                possible_moves.append([self.y + offset_y,self.x + offset_x])
                break
            elif chess_grid.get_piece(self.y + offset_y,self.x + offset_x).color != self.color:
                possible_moves.append([self.y + offset_y,self.x + offset_x])
                break
            else:
                break

        return possible_moves
            
class Pawn(Pieces):
    def __init__(self, x, y, img_path, color):
        Pieces.__init__(self, x, y, img_path, color)
        
    def possible_moves(self):
        print("Pawn")
        possible_moves = []
        
        # Bug:
        # 2. backward movement is allowed which should not be the case
        offset = 1                                   # This condition checks moves on black pawns for one forward, and diagonal if attack possible
        if chess_grid.get_piece(self.y,self.x).color == "black":
            if not chess_grid.piece_inside_board(self.y - offset,self.x):
                return possible_moves
            if chess_grid.get_piece(self.y - offset,self.x) == 0:
                possible_moves.append([self.y - offset,self.x])
        if self.x + offset <= 7:
            if chess_grid.get_piece(self.y - offset,self.x + offset) != 0 and (chess_grid.get_piece(self.y - offset,self.x + offset).color != self.color):
                possible_moves.append([self.y - offset,self.x + offset])
        if self.x - offset >= 0:
            if chess_grid.get_piece(self.y - offset,self.x - offset) != 0 and (chess_grid.get_piece(self.y - offset,self.x - offset).color != self.color):
                possible_moves.append([self.y - offset,self.x - offset])
       
        offset = 2
        offset_a = 1
        if self.y == 6:                                    # This condition checks moves on black pawns for two forward from starting position
            if chess_grid.get_piece(self.y,self.x).color == "black": #and count == 0:
                if not chess_grid.piece_inside_board(self.y - offset,self.x):
                    return possible_moves
                if chess_grid.get_piece(self.y - offset,self.x) == 0 and chess_grid.get_piece(self.y - offset_a,self.x) == 0:
                    count = 1
                    possible_moves.append([self.y - offset,self.x])

        offset = 1                                   # This condition checks moves on white pawns for one forward, and diagonal if attack possible
        if chess_grid.get_piece(self.y,self.x).color == "white":
            if not chess_grid.piece_inside_board(self.y + offset,self.x):
                return possible_moves
            if chess_grid.get_piece(self.y + offset,self.x) == 0:
                possible_moves.append([self.y + offset,self.x])
            if self.x + offset <= 7:
                if chess_grid.get_piece(self.y + offset,self.x + offset) != 0 and (chess_grid.get_piece(self.y + offset,self.x + offset).color != self.color):
                    possible_moves.append([self.y + offset,self.x + offset])
            if self.x - offset >= 0:
                if chess_grid.get_piece(self.y + offset,self.x - offset) != 0 and (chess_grid.get_piece(self.y + offset,self.x - offset).color != self.color):
                    possible_moves.append([self.y + offset,self.x - offset])
        
        offset = 2
        offset_a = 1
        if self.y == 1:                                   # This condition checks moves on white pawns for two forward from starting position
            if chess_grid.get_piece(self.y,self.x).color == "white": 
                if not chess_grid.piece_inside_board(self.y + offset,self.x):
                    return possible_moves
                if chess_grid.get_piece(self.y + offset,self.x) == 0 and chess_grid.get_piece(self.y + offset_a,self.x) == 0:
                    count = 1
                    possible_moves.append([self.y + offset,self.x])
        return possible_moves
        
    
class Chess_board:
    def __init__(self, num_rows, num_cols):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.game_over = False
        self.highlighted = False
        self.possible_highlights = []
        self.turn_color = "white"
    
        self.chess_grid_board = []                  # this is to initialize a grid on the screen
        for row in range(self.num_rows):
            self.chess_row = []               # to iterate through each row
            for col in range(self.num_cols):
                self.chess_row.append(0)
            self.chess_grid_board.append(self.chess_row) 
        self.create_pieces()
    
    def get_piece(self, x, y):                  # this is to obtain the piece from the chess board and return it 
        return self.chess_grid_board[x][y]
        
    def create_pieces(self):                   # this method creates pieces and allocates them in the chess board with their display images and color
        for i in range(num_cols):
            self.chess_grid_board[1][i] = Pawn(i,1, "white_pawn", "white")
            self.chess_grid_board[num_rows - 2][i] = Pawn(i,num_rows - 2, "black_pawn", "black")

        self.chess_grid_board[0][0] = Rook(0,0, "white_rook", "white")
        self.chess_grid_board[0][7] = Rook(7,0, "white_rook", "white")
        
        self.chess_grid_board[0][1] = Knight(1,0, "white_knight", "white")
        self.chess_grid_board[0][6] = Knight(6,0, "white_knight", "white")
        
        self.chess_grid_board[0][2] = Bishop(2,0, "white_bishop", "white")
        self.chess_grid_board[0][5] = Bishop(5,0, "white_bishop", "white")
    
        self.chess_grid_board[0][3] = Queen(3,0, "white_queen", "white")
        self.chess_grid_board[0][4] = King(4,0, "white_king", "white")
        
        self.chess_grid_board[7][0] = Rook(0,7, "black_rook", "black")
        self.chess_grid_board[7][7] = Rook(7,7, "black_rook", "black")
        
        self.chess_grid_board[7][1] = Knight(1,7, "black_knight", "black")
        self.chess_grid_board[7][6] = Knight(6,7, "black_knight", "black")
        
        self.chess_grid_board[7][2] = Bishop(2,7, "black_bishop", "black")
        self.chess_grid_board[7][5] = Bishop(5,7, "black_bishop", "black")
    
        self.chess_grid_board[7][3] = Queen(3,7, "black_queen", "black")
        self.chess_grid_board[7][4] = King(4,7, "black_king", "black")
        
        return
         
    def display_background(self):
        possible_move_img = loadImage(path + "/images/possible_move.png")
        possible_attack_img = loadImage(path + "/images/possible_attack_move.png")
       
        pos_x = 0
        pos_y = 0 
        for row in range(num_rows):                    # this is to display black and white background tiles on the grid 
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

        if self.possible_highlights != 0:                  # this is display the blue image for possible movements of the clicked piece 
            for i in self.possible_highlights: 
                image(possible_move_img, i[1] * cell_width,i[0] * cell_height, cell_width, cell_height)
       
         # if self.possible_highlights != 0:
        #     for j in self.possible_highlights:
        #         if j.color in self.possible_highlights != self.color:
        #             image(possible_attack_img, j[1] * cell_width,j[0] * cell_height, cell_width, cell_height)
        return
            

    def display(self):                  # this method is displaying the pieces
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                if self.chess_grid_board[i][j]:
                    self.chess_grid_board[i][j].display_pieces()
        return
    
    def piece_inside_board(self, x, y):                 # this method is checking if pieces and movements are within the range limits
        if (x < 0) or (x > 7) or (y < 0) or (y > 7):
            return False
        else:
            return True
    
    def user_clicked(self, row, col):                   # this method is 
        if not self.piece_inside_board(row, col):
            self.possible_highlights = 0
            return
        
        if self.highlighted == False:                    # Check if a piece is here/present
            if chess_grid.get_piece(row,col) == 0: 
                return
            if self.chess_grid_board[row][col].color == self.turn_color:          #Check if correct color
                self.highlighted = [row,col]
                self.possible_highlights = self.chess_grid_board[row][col].possible_moves()
            else:
                return
        else: 
            if [row,col] in self.chess_grid_board[self.highlighted[0]][self.highlighted[1]].possible_moves():
                self.chess_grid_board[row][col] = self.chess_grid_board[self.highlighted[0]][self.highlighted[1]]

                self.chess_grid_board[row][col].x = col           #Update piece's coordinates
                self.chess_grid_board[row][col].y = row           #Update piece's coordinates
                
                self.chess_grid_board[self.highlighted[0]][self.highlighted[1]] = 0
               
                if self.turn_color == "white":                  #Change the color after each turn
                    self.turn_color = "black"
                else:
                    self.turn_color = "white"
            self.possible_highlights = 0
            self.highlighted = False
    
    def check_king(self):
        pass
    
    def check_mate(self):
        pass
    
    def possible_highlight_moves(self,row,col):                 # This method calls for possible moves and the piece clicked
        current_piece = self.chess_grid_board[row][col]
        self.possible_highlights = current_piece.possible_moves()

chess_grid = Chess_board(num_rows, num_cols) 

def setup():
    size(num_rows * cell_height, num_cols * cell_width)

def draw():
    chess_grid.display_background()
    chess_grid.display()

def mouseClicked(self):
    col = mouseX // cell_width
    row = mouseY // cell_height
    print("clicked at "  + str(row) + " " + str(col))
    
    piece = chess_grid.get_piece(row, col)
    
    chess_grid.user_clicked(row, col)
    print(piece, row, col)
    
print(chess_grid.create_pieces())
