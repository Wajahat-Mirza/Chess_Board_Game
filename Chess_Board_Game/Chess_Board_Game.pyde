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
        piece_img  = loadImage(path + "/images/" + self.img_path + ".png")
        x, y = self.convertCoord(self.x, self.y)
        image(piece_img, x, y, cell_width, cell_height)
    
class Rook(Pieces):                                  
    def __init__(self, x, y, img_path, color):
        Pieces.__init__(self, x, y, img_path, color)
        
    def possible_moves(self):                        # This checks all the possible moves from the given position of the piece           
        possible_moves = []
        offset = 1
        while(True):                                 # This loop checks moves on x_increment place/scale               
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
        while(True):                                 # This loop checks moves on x_decrement place/scale
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
        while(True):                                 # This loop checks moves on y_increment place/scale
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
        while(True):                                 # This loop checks moves on y_decrement place/scale
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
        while(True):                                 # This loop checks moves on y_decrement, x_decrement place/scale
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
        while(True):                                 # This loop checks moves on y_increment, x_increment place/scale
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
        while(True):                                 # This loop checks moves on y_decrement, x_increment place/scale
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
        while(True):                                 # This loop checks moves on y_increment, x_decrement place/scale
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
        while(True):                                 # This loop checks moves on y_decrement, x_decrement place/scale
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
        while(True):                                 # This loop checks moves on y_decrement, x_increment place/scale
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
        while(True):                                 # This loop checks moves on y_increment, x_increment place/scale
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
        while(True):                                 # This loop checks moves on y_increment, x_decrement place/scale
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
        while(True):                                 # This loop checks moves on y_increment, x_increment place/scale
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
        while(True):                                 # This loop checks moves on y_decrement, x_decrement place/scale
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
        while(True):                                 # This loop checks moves on y_increment, x_decrement place/scale
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
        while(True):                                 # This loop checks moves on y_decrement, x_increment place/scale
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
        while(True):                                  # This loop checks moves on x_increment place/scale
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
        while(True):                                  # This loop checks moves on x_decrement place/scale
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
        while(True):                                   # This loop checks moves on y_increment place/scale
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
        while(True):                                  # This loop checks moves on y_decrement place/scale
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
        while(True):                                  # This loop checks moves on y_increment, x_increment place/scale
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
        while(True):                                  # This loop checks moves on y_decrement, x_decrement place/scale
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
        while(True):                                  # This loop checks moves on y_increment, x_decrement place/scale
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
        while(True):                                  # This loop checks moves on y_decrement, x_increment place/scale
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
        while(True):
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
        while(True):
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
        while(True):
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
        while(True):
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
        while(True):
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
        while(True):
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
        while(True):
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
        while(True):
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
        print(possible_moves)
        return possible_moves
            
class Pawn(Pieces):
    def __init__(self, x, y, img_path, color):
        Pieces.__init__(self, x, y, img_path, color)
        
    def possible_moves(self):
        print("Pawn")
        possible_moves = []
        offset = 1
        if chess_grid.get_piece(self.y,self.x).color == "black":
            while(True):
                if not chess_grid.piece_inside_board(self.y - offset,self.x):
                    break
                if(chess_grid.get_piece(self.y - offset,self.x) == 0):
                    possible_moves.append([self.y - offset,self.x])
                elif (chess_grid.get_piece(self.y - offset,self.x + offset).color != self.color) or (chess_grid.get_piece(self.y - offset,self.x - offset).color != self.color):
                    possible_moves.append([self.y - offset,self.x + offset])
                    possible_moves.append([self.y - offset,self.x - offset])
                    break
                else:
                    break
            #offset += 1
        print(possible_moves)
        return possible_moves
        
    
class Chess_board:
    def __init__(self, num_rows, num_cols):#pieces
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
        print(self.chess_grid_board)                # for test purposes
        
        self.create_pieces()
    
    def get_piece(self, x, y):
        return self.chess_grid_board[x][y]
        
    def create_pieces(self):
        for i in range(num_cols):
            print(i)
            #self.chess_grid_board[1][i] = Pawn(i,1, "white_pawn", "white")
            self.chess_grid_board[num_rows - 2][i] = Pawn(i,num_rows - 2, "black_pawn", "black")

        # Improve this code later 
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
    
        
        print(self.chess_grid_board)
        return
         
    def display_background(self):
        possible_move_img = loadImage(path + "/images/possible_move.png")
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

        if self.possible_highlights != 0:
            for i in self.possible_highlights: 
                image(possible_move_img, i[1] * cell_width,i[0] * cell_height, cell_width, cell_height)
        return
            

    def display(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                if self.chess_grid_board[i][j]:
                    self.chess_grid_board[i][j].display_pieces()
        
        
    
    def piece_inside_board(self, x, y):
        if (x < 0) or (x > 7) or (y < 0) or (y > 7):
            return False
        else:
            return True
    
    def user_clicked(self, row, col):
        
        if not self.piece_inside_board(row, col):
            self.possible_highlights = 0
            return
        if self.highlighted == False:
            #Check if a piece is here
            if chess_grid.get_piece(row,col) == 0: 
                return
            #Check if correct color
            if self.chess_grid_board[row][col].color == self.turn_color:
                self.highlighted = [row,col]
                self.possible_highlights = self.chess_grid_board[row][col].possible_moves()
            else:
                return
        else: 
            if [row,col] in self.chess_grid_board[self.highlighted[0]][self.highlighted[1]].possible_moves():
                self.chess_grid_board[row][col] = self.chess_grid_board[self.highlighted[0]][self.highlighted[1]]

                #Update piece's coordinates
                self.chess_grid_board[row][col].x = col
                self.chess_grid_board[row][col].y = row
                
                self.chess_grid_board[self.highlighted[0]][self.highlighted[1]] = 0
                #Change the color. Black to white etc..
                if self.turn_color == "white":
                    self.turn_color = "black"
                else:
                    self.turn_color = "white"
                print("gellow")
            self.possible_highlights = 0
            self.highlighted = False
    
    def possible_highlight_moves(self,row,col):
        current_piece = self.chess_grid_board[row][col]
        self.possible_highlights = current_piece.possible_moves()

chess_grid = Chess_board(num_rows, num_cols) #pieces

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
    #piece.possible_moves()

print(chess_grid.create_pieces())
