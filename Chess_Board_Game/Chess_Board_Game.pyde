# Name: Muhammad Wajahat Mirza (mwm356) and Abraham Okbasslaise Hdru (ah3300)
# Date: May 15th 2019
# Description : Final Project Chess

import os 
from copy import deepcopy
path = os.getcwd()
add_library("minim")
audioPlayer = Minim(this)

num_rows = 8 
num_cols = 8 
cell_height = 64
cell_width  = 64

check = False 
check_black = False
check_white = False

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
        image(piece_img, x, y, cell_width, cell_height)                          # This loads images at x,y position\
        
    # def limit_moves(self, lpm):
    #     flag = 0
    #     assassin = []
    #     ans = []
    #     if self.color == "white":
    #         if len(chess_grid.white_eater) != 0:
    #             flag = 1
    #             assassin = chess_grid.white_eater
    #     else:
    #         if len(chess_grid.black_eater) != 0:
    #             flag = 1
    #             assassin = chess_grid.black_eater
                
    #     if flag == 1:
    #         print("flagged")
    #         for i in lpm:
    #             if chess_grid.chess_grid_board[i[0]][i[1]] in assassin:
    #                 ans.append(i)
    #                 continue
                
    #             real = [self.x, self.y]
    #             real_piece = chess_grid.chess_grid_board[i[0]][i[1]]
    #             chess_grid.chess_grid_board[i[0]][i[1]] = self
    #             chess_grid.chess_grid_board[i[0]][i[1]].x = self.x           #Update piece's coordinates
    #             chess_grid.chess_grid_board[i[0]][i[1]].y = self.y
    #             temp_possible_moves = chess_grid.chess_grid_board[i[0]][i[1]].possible_moves()
                
                
    #             global check_white
    #             global check_black
                
    #             for j in assassin:
    #                 chess_grid.check_move(j)
    #                 if self.color == "white":
    #                     if check_white == False:
    #                         ans.append(i)
    #                         break
    #                 else:
    #                     if check_black == False:
    #                         ans.append(i)
    #                         break
    #             print("are you here?")
    #             chess_grid.chess_grid_board[i[0]][i[1]] = real_piece
    #             chess_grid.chess_grid_board[real[0]][real[1]] = self
    #             chess_grid.chess_grid_board[real[0]][real[1]].x = self.x
    #             chess_grid.chess_grid_board[real[0]][real[1]].y = self.y

    #         if len(ans) == 0:
    #             return lpm
            
    #         else:
    #             print("yeh", ans)
    #             return ans
    #         #we'll do the checks here
    #     else:
    #         print("not flagged")
    #         return lpm
        
    
class Rook(Pieces):                                  
    def __init__(self, x, y, img_path, color):
        Pieces.__init__(self, x, y, img_path, color)
        
    def possible_moves(self, chess_grid):                        # This checks all the possible moves from the given position of the piece           
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
        
    def possible_moves(self, chess_grid):
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
    
    def possible_moves(self, chess_grid): 
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
        
    def possible_moves(self, chess_grid): 
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
        
    def possible_moves(self, chess_grid): 
        possible_moves = []
        
        offset_x = 1
        while(True):                                 # This loop checks moves on x_increment plane/scale
            if not chess_grid.piece_inside_board(self.y,self.x + offset_x):
                
                break
            if(chess_grid.get_piece(self.y,self.x + offset_x) == 0):
                
                possible_moves.append([self.y,self.x + offset_x])
                break
            elif chess_grid.get_piece(self.y,self.x + offset_x).color != self.color:
                
                possible_moves.append([self.y,self.x + offset_x])
                break
            else:
                break
        
        offset_x = 1
        while(True):                                  # This loop checks moves on x_decrement plane/scale
            if not chess_grid.piece_inside_board(self.y,self.x - offset_x):
                
                break
            if(chess_grid.get_piece(self.y,self.x - offset_x) == 0):
                possible_moves.append([self.y,self.x - offset_x])
                break
            elif chess_grid.get_piece(self.y,self.x - offset_x).color != self.color:
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
        
        # if self.color == "white":
        #     lst = chess_grid.white_eater
        # else:
        #     lst = chess_grid.black_eater
        
        # for i in lst:
        #     for j in i.possible_moves():
        #         if j in possible_moves:
        #             possible_moves.remove(j)
        
        # if len(lst) != 0:
        #     for i in possible_moves:
        #         # print(self)
        #         print(i[0], i[1])
        #         chess_grid.chess_grid_board[i[0]][i[1]] = self
        #         # for j in lst:
        #         #     for k in j.possible_moves():
        #         #         print("hi")
        #         #         if k in possible_moves:
        #         #             print("lol almost died")
        #         #             possible_moves.remove(k)
        
        # chess_grid.chess_grid_board[self.y][self.x] = self
        return possible_moves
            
class Pawn(Pieces):
    def __init__(self, x, y, img_path, color):
        Pieces.__init__(self, x, y, img_path, color)
        
    def possible_moves(self, chess_grid):
        possible_moves = []
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
        #possible_moves = self.limit_moves(possible_moves)
        return possible_moves

        
class Chess_board:
    def __init__(self, num_rows, num_cols):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.game_over = False
        self.highlighted = False
        self.possible_highlights = []
        self.turn_color = "white"
        self.sound_Move = audioPlayer.loadFile(path + "/images/Move.wav")
        self.sound_harry = audioPlayer.loadFile(path + "/images/harry_potter_theme.mp3")
        self.white_eater = []
        self.black_eater = []
        # self.white_name = None
        # self.black_name = None
    
        self.chess_grid_board = []         # this is to initialize a grid on the screen
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
        self.white_king = self.chess_grid_board[0][4]
        
        self.chess_grid_board[7][0] = Rook(0,7, "black_rook", "black")
        self.chess_grid_board[7][7] = Rook(7,7, "black_rook", "black")
        
        self.chess_grid_board[7][1] = Knight(1,7, "black_knight", "black")
        self.chess_grid_board[7][6] = Knight(6,7, "black_knight", "black")
        
        self.chess_grid_board[7][2] = Bishop(2,7, "black_bishop", "black")
        self.chess_grid_board[7][5] = Bishop(5,7, "black_bishop", "black")
    
        self.chess_grid_board[7][3] = Queen(3,7, "black_queen", "black")
        self.chess_grid_board[7][4] = King(4,7, "black_king", "black")
        self.black_king = self.chess_grid_board[7][4]
        
        self.king_list = [self.white_king,self.black_king]
        return
         
    def display_background(self):
        possible_move_img = loadImage(path + "/images/possible_move.png")
        possible_attack_img = loadImage(path + "/images/possible_attack_move.png")
        sound_harry.pause()
        
       
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

        if len(self.possible_highlights) != 0:                  # this is display the blue image for possible movements of the clicked piece 
            for i in self.possible_highlights: 
                image(possible_move_img, i[1] * cell_width,i[0] * cell_height, cell_width, cell_height)
                if i == self.chess_grid_board[self.highlighted[0]][self.highlighted[1]] and i.color != self.turn_color: 
                    image(possible_attack_img, i[1] * cell_width,i[0] * cell_height, cell_width, cell_height)
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
    
    def user_clicked(self, row, col):                   
        global check_black
        global check_white
        
        if not self.piece_inside_board(row, col):
           self.possible_highlights = []
           return
                         
        if self.highlighted == False:                    # Check if a piece is here/present
            if real_chess_grid.get_piece(row,col) == 0: 
                return

            if self.chess_grid_board[row][col].color == self.turn_color:          #Check if correct color
                self.highlighted = [row,col]               
                self.sound_Move.pause()
                self.sound_Move.rewind()
                self.sound_Move.play()          
                current_piece = self.chess_grid_board[row][col]
                # Create a temporary board to backend vislualize movement for check and checkmate
                temp = self.chess_grid_board[row][col].possible_moves(self)
                res = []          # res = result
                for r, c in temp:
                    temp_board = deepcopy(self.chess_grid_board)   # this import helps to create the temporary board
                    temp_board[r][c] = temp_board[row][col]
                    temp_board[r][c].x = c           #Update piece's coordinates
                    temp_board[r][c].y = r           #Update piece's coordinates
                    temp_board[row][col] = 0
                   
                     # This is for when king is in check
                    if "king" in current_piece.img_path:
                        if "black" in current_piece.img_path:
                            w,b = self.check_king(temp_board, self.white_king.x, self.white_king.y, c, r)     
                        else:
                            w,b = self.check_king(temp_board, c, r, self.black_king.x, self.black_king.y)
                    else:
                        w,b = self.check_king(temp_board, self.white_king.x, self.white_king.y, self.black_king.x, self.black_king.y)
                    
                    if self.turn_color == "white" and w == False:
                        res.append([r,c])
                    elif self.turn_color == "black" and b == False:
                        res.append([r,c])
                self.possible_highlights = res
    
            else:
                return
        else: 
            
            if [row,col] in self.chess_grid_board[self.highlighted[0]][self.highlighted[1]].possible_moves(self):

                self.chess_grid_board[row][col] = self.chess_grid_board[self.highlighted[0]][self.highlighted[1]]
                self.chess_grid_board[row][col].x = col           #Update piece's coordinates
                self.chess_grid_board[row][col].y = row           #Update piece's coordinates
                self.chess_grid_board[self.highlighted[0]][self.highlighted[1]] = 0
                self.check_mate()
                
                if self.turn_color == "white":                  #Change the color after each turn
                    self.turn_color = "black"
                else:
                    self.turn_color = "white"
            
            self.possible_highlights = []
            self.highlighted = False
            
    def check_king(self, board, wkx, wky, bkx, bky):   # wkx, wky = whiteking-x, whiteking-y # bky,bkyx = blackking-x, blackking-y 
        
        white_check = False
        black_check = False

        temp = Chess_board(num_rows, num_cols)
        temp.chess_grid_board = board
        
        for lc in board:
            for cell in lc:
                if cell != 0: 
                    print(cell)
                    if cell.color == "black":
                        moves = cell.possible_moves(temp)
                        for r,c in moves:
                            if r == wky and c == wkx:
                                white_check = True
                    else: 
                        moves = cell.possible_moves(temp)
                        for r,c in moves:
                            if r == bky and c == bkx:
                                black_check = True                    
        return (white_check, black_check)
        
    def check_mate(self):
        is_mate = False

        w,b = self.check_king(self.chess_grid_board, self.white_king.x, self.white_king.y, self.black_king.x, self.black_king.y)
        if self.turn_color == "white":
            # for white
            if w == True:
                cnt = 0
                for row in range(self.num_rows):
                    for col in range(self.num_cols):
                        cell = self.chess_grid_board[row][col]
                        if cell != 0 and cell.color == "white":
                            current_piece = cell
                            
                            # Just like check, creat temporary checkmate to check no possible move remains and king is check
                            temp = cell.possible_moves(self)
                            res = []
                            for r, c in temp:
                                temp_board = deepcopy(self.chess_grid_board)
                                temp_board[r][c] = temp_board[row][col]
                                temp_board[r][c].x = c           #Update piece's coordinates
                                temp_board[r][c].y = r           #Update piece's coordinates
                                temp_board[row][col] = 0
                                if "king" in current_piece.img_path:
                                    if "black" in current_piece.img_path:
                                        w,b = self.check_king(temp_board, self.white_king.x, self.white_king.y, c, r)
                                    else:
                                        w,b = self.check_king(temp_board, c, r, self.black_king.x, self.black_king.y)
                                else:
                                    w,b = self.check_king(temp_board, self.white_king.x, self.white_king.y, self.black_king.x, self.black_king.y)
                            if self.turn_color == "white" and w == False:
                                res.append([r,c])
                            elif self.turn_color == "black" and b == False:
                                res.append([r,c])
                            cnt += len(res)
                if cnt == 0:
                    is_mate = True
                    self.game_over = True

        else:
            #for black
            if b == True:
                cnt = 0
                for row in range(self.num_rows):
                    for col in range(self.num_cols):
                        cell = self.chess_grid_board[row][col]
                        if cell != 0 and cell.color == "black":
                            current_piece = cell
                            # self.sound_Move
                            temp = cell.possible_moves(self)
                            res = []
                            for r, c in temp:
                                temp_board = deepcopy(self.chess_grid_board)
                                temp_board[r][c] = temp_board[row][col]
                                temp_board[r][c].x = c           #Update piece's coordinates
                                temp_board[r][c].y = r           #Update piece's coordinates
                                temp_board[row][col] = 0
                                if "king" in current_piece.img_path:
                                    if "black" in current_piece.img_path:
                                        w,b = self.check_king(temp_board, self.white_king.x, self.white_king.y, c, r)
                                    else:
                                        w,b = self.check_king(temp_board, c, r, self.black_king.x, self.black_king.y)
                                else:
                                    w,b = self.check_king(temp_board, self.white_king.x, self.white_king.y, self.black_king.x, self.black_king.y)
                            if self.turn_color == "white" and w == False:
                                res.append([r,c])
                            elif self.turn_color == "black" and b == False:
                                res.append([r,c])
                            cnt += len(res)
                if cnt == 0:
                    is_mate = True
                    self.game_over = True      
        print("Game Over")    
        return is_mate

class Button: 
    def __init__(self,label,x,y, height,width, mode): 
        self.label = label 
        self.x = x
        self.y = y 
        self.height = height 
        self.width = width 
        self.mode = mode  ## Adding modes to easily change between game, name input, instruction, and scoreboard  

    def contains_mouse(self):
        return self.x <= mouseX <= self.x + self.width and self.y - self.height <= mouseY <= self.y
        
    def display(self):  ## function to change button color when mouse hovers
        if self.contains_mouse():
            fill(100)
            if Game.state == "instruction":
                fill(255, 0, 0)
            text(self.label, self.x, self.y)
            fill(255)
        
        elif Game.state == "nameinput": 
            fill(255, 0, 0)
            text(self.label, self.x, self.y)
            
        elif Game.state == "instruction": 
            fill(0)
            text(self.label, self.x, self.y)
        else:
            fill(255)
            textSize(50)
            text(self.label, self.x, self.y)

sound_harry = audioPlayer.loadFile(path + "/images/harry_potter_theme.mp3")

class Display: 
    def __init__(self, width,height): 
        print("Initializing GameDisplay")
        self.width = width 
        self.height = height 
        self.state = "menu"
        self.buttons = [] 
        self.returnbutton = 0
        self.playgamebutton = 0
        self.chessimage = loadImage(path + "/images/chess_main_image.png")
        self.backimage = loadImage(path + "/images/inputbackground.png")
        self.scoreboardimage = loadImage(path + "/images/scoreboard.png")
        self.rulesimage = loadImage(path + "/images/rules.png")
        self.whiteplayer = 0
        self.blackplayer = 0
        self.NameList = []
        self.white_name = None 
        self.black_name = None
        
        # Add Buttons; Start, Instruction, Scoreboard 
        self.buttons.append(Button("Start Game", self.width//2-100, self.height//2 - 50, 50, 250,"nameinput" ))
        self.buttons.append(Button("Instructions", self.width//2-100, self.height//2 + 50, 50, 250,"instruction"))
        self.buttons.append(Button("Scoreboard", self.width//2-100, self.height//2 + 150, 50, 250, "scoreboard"))
        
        # Add Play Start Button
        self.playgamebutton =(Button("Play Game", self.width//2-100, self.height//2 - 50, 50, 250,"game" ))
        
        # Return button 
        self.returnbutton = (Button("Return",self.width-470, self.height - 20, 50, 250, "return"))
        
        # White and Black name button 
        self.whiteplayer = (Button("White", self.width//2-100, self.height//2 + 50, 50, 250,"White-Player"))
        self.blackplayer = (Button("Black", self.width//2-100, self.height//2 + 150, 50, 250,"Black-Player"))
        
    def menu_display(self):
        background(155)
        image(self.chessimage, 0, 0, height, width)
        sound_harry.play()
        
        for button in self.buttons:   ## Reiterated through button list for display 
            button.display()
    
    def nameinput_display(self): 
        background(155) 
        image(self.backimage, 0, 0, height, width)
        self.playgamebutton.display()
        self.whiteplayer.display()
        self.blackplayer.display()
        self.returnbutton.display()
    
    def whiteplayername_display(self):        # Adding white name (Player 1) to scoreboard text file 
        self.white_name = input(" Enter your name (white): ")
        if self.white_name == None:
            self.white_name = "No Name Given (white)"
        # self.NameList.append(self.white_name.encode('utf-8'))
        f = open("scoreboard.txt", "a")
        f.write(self.white_name + "\n" )
        # print(NameList)
        
    def blackplayername_display(self):      # Adding black name (Player 2) to scoreboard text file 
        self.black_name = input(" Enter your name (black): ")
        if self.black_name == None:
            self.black_name = "No Name Given (black)"
        # self.NameList.append(self.black_name.encode('utf-8'))
        f = open("scoreboard.txt", "a")
        f.write(self.black_name)
        # print(self.NameList)
    
    def instruction_display(self): 
        background(155)
        image(self.rulesimage, 0, 0, height, width)
        self.returnbutton.display()
        
    def scoreboard_display(self): 
        background(155)
        # image(self.scoreboardimage, 0, 0, height, width)
        self.returnbutton.display()
        #f = open("scoreboard.txt", "r")
        text("  Name         Score  ", 0, 100) 
        with open("scoreboard.txt", "r") as f:
            lines = f.readlines()
            score_dict = {}
            for index, line in enumerate(lines):
                vals = line.split(",")
                #score_dict[vals[0]] = vals[1].rstrip("\n")
                text(vals[0], 0, 300+index*100)
                # text(vals[1], 300, 300+index*100)    
        

                
real_chess_grid = Chess_board(num_rows, num_cols)
Game = Display(500,500)


def setup():
    size(num_rows * cell_height, num_cols * cell_width)
        
def input(message=''):        
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(frame, message)

def textfile():
    exists = os.path.isfile("scoreboard.txt") 
    if exists: 
        return 
    else: 
        fh = open('scoreboard.txt', 'w') 
        fh.write("Name,Scoreboard\n")
        fh.close()
        
textfile()

def draw():
    if Game.state == "menu":
        Game.menu_display()
    elif Game.state == "nameinput": 
        Game.nameinput_display() and Game.whiteplayer_display() and Game.blackplayer_display() and Game.returnbutton.display()
    elif Game.state == "White-Player": 
        Game.whiteplayername_display()
        if Game.black_name == None:
            Game.state = "nameinput"
        else:
            Game.state = "game"
    elif Game.state == "Black-Player": 
        Game.blackplayername_display()
        if Game.white_name == None:
            Game.state = "nameinput"
        else:
            Game.state = 'game'
    elif Game.state == "game":
        real_chess_grid.display_background()
        real_chess_grid.display()
    elif Game.state == "instruction": 
        Game.instruction_display() 
    elif Game.state == "scoreboard": 
        Game.scoreboard_display() 
        

def mouseClicked(self):
    
    if Game.state == "menu":
        col = mouseX // cell_width
        row = mouseY // cell_height
        print("clicked at "  + str(row) + " " + str(col))
        for b in Game.buttons:
            if b.contains_mouse():
                Game.state = b.mode
                
    elif Game.state == "instruction": 
        col = mouseX // cell_width
        row = mouseY // cell_height
        print("clicked at "  + str(row) + " " + str(col))
        if Game.returnbutton.contains_mouse(): 
            Game.state = "menu"
    
    elif Game.state == "scoreboard": 
        col = mouseX // cell_width
        row = mouseY // cell_height
        print("clicked at "  + str(row) + " " + str(col))
        if Game.returnbutton.contains_mouse(): 
            Game.state = "menu"
            
    elif Game.state == "nameinput": 
        col = mouseX // cell_width
        row = mouseY // cell_height
        print("clicked at "  + str(row) + " " + str(col))
    
        if Game.playgamebutton.contains_mouse(): 
            Game.state = "game"
        elif Game.whiteplayer.contains_mouse(): 
            Game.state = "White-Player"
        elif Game.blackplayer.contains_mouse(): 
            Game.state = "Black-Player"    
        elif Game.returnbutton.contains_mouse(): 
            Game.state = "menu"
     
    elif Game.state == "game":
        col = mouseX // cell_width
        row = mouseY // cell_height
        
        print("clicked at "  + str(row) + " " + str(col))
        piece = real_chess_grid.get_piece(row, col)
        
        real_chess_grid.user_clicked(row, col)
        print(piece, row, col)
        
## Add elif     
 # temp = current_piece.possible_moves()
                # if check == True:
                #     print(self.possible_highlights)
                #     print("highlighting")
                #     for i in self.assassins:
                #         for j in i.possible_moves():
                #             if j in temp:
                #                 self.possible_highlights.append(j)
