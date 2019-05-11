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

class Pieces:
    def __init__(self, x, y, img_path, color):
        self.color = color
        #self.player = player
        self.x, self.y = x, y
        self.img_path = img_path
       # self.backend_game_sound = audio_track.loadFile(path + "/sounds/chessbackground") # Need to download sound tracks

    def convertCoord(self,x,y):
        return x * cell_width,y * cell_height
   
    def display_pieces(self):
        piece_img  = loadImage(path + "/images/" + self.img_path + ".png")
        x, y = self.convertCoord(self.x, self.y)
        image(piece_img, x, y, cell_width, cell_height)
    
class Rook(Pieces):
    def __init__(self, x, y, img_path, color):
        Pieces.__init__(self, x, y, img_path, color)
        
    def possible_moves(self): # Improve this algorithm later 
        print("Rook")
        possible_moves = []
        offset = 1
        while(True):
            if not chess_grid.piece_inside_board(self.x + offset,self.y):
                break
            if(chess_grid.get_piece(self.x + offset,self.y) == 0):
                possible_moves.append([self.x + offset,self.y])
            elif chess_grid.get_piece(self.x + offset,self.y).color != self.color:
                possible_moves.append([self.x + offset,self.y])
                break
            else:
                break
            offset += 1
        offset = 1
        # while(True):
        #     if(chess_grid.piece_inside_board(self.x - offset,self.y) == 0):
        #         possible_moves.append([self.x - offset,self.y])
        #     elif chess_grid.piece_inside_board(self.x - offset,self.y).color != self.color:
        #         possible_moves.append([self.x - offset,self.y])
        #         break
        #     else:
        #         break
        #     offset += 1
        print(possible_moves) 
            
        # all_moves = [[self.x,self.y+1],[self.x,self.y+2],[self.x,self.y+3],[self.x,self.y+4],
        #              [self.x,self.y+5],[self.x,self.y+6],[self.x,self.y+7],
        #              [self.x+1,self.y],[self.x+2,self.y],[self.x+3,self.y],[self.x+4,self.y],
        #              [self.x+5,self.y],[self.x+6,self.y],[self.x+7,self.y],
        #              [self.x-1,self.y],[self.x-2,self.y],[self.x-3,self.y],[self.x-4,self.y],
        #              [self.x-5,self.y],[self.x-6,self.y],[self.x-7,self.y],
        #              [self.x,self.y-1],[self.x,self.y-2],[self.x,self.y-3],[self.x,self.y-4],
        #              [self.x,self.y-5],[self.x,self.y-6],[self.x,self.y-7]]
        # print(all_moves)
        # possible_moves = []
        # for i in all_moves:
        #     if (chess_grid.piece_inside_board(i[0],i[1])):
        #         possible_moves.append(i)
        # print(possible_moves)
        
        # moveable_cells =[]
        # for j in possible_moves: 
        #     if chess_grid.get_piece(j[0], j[1]) == 0:
        #         moveable_cells.append(j)
        # print(moveable_cells)

class Knight(Pieces):
    def __init__(self, x, y, img_path,color):
        Pieces.__init__(self, x, y, img_path,color)
        
    def possible_moves(self):
        print("knight")
        all_moves = [[self.x-2,self.y-1],[self.x-1,self.y-2],[self.x+1,self.y-2],[self.x+2,self.y-1],
                     [self.x+2,self.y+1],[self.x+1,self.y+2],[self.x-1,self.y+2],[self.x-2,self.y+1]]
        print(all_moves)
        possible_moves = []
        for i in all_moves:
            if(chess_grid.piece_inside_board(i[0],i[1])):
                possible_moves.append(i)
        print(possible_moves)
            
        #3. Highlight moves: specific position walay box par color kardo ge
    #def check_move (check validity) 
    
class Bishop(Pieces):
    def __init__(self, x, y, img_path,color):
        Pieces.__init__(self, x, y, img_path,color)
    
    def possible_moves(self): # Improve this algorithm later 
        all_moves = [[self.x+1,self.y+1],[self.x+2,self.y+2],[self.x+3,self.y+3],[self.x+4,self.y+4],
                     [self.x+5,self.y+5],[self.x+6,self.y+6],[self.x+7,self.y+7],
                     [self.x-1,self.y+1],[self.x-2,self.y+2],[self.x-3,self.y+3],[self.x-4,self.y+4],
                     [self.x-5,self.y+5],[self.x-6,self.y+6],[self.x-7,self.y+7],
                     [self.x+1,self.y-1],[self.x+2,self.y-2],[self.x+3,self.y-3],[self.x+4,self.y-4],
                     [self.x+5,self.y-5],[self.x+6,self.y-6],[self.x+7,self.y-7],
                     [self.x-1,self.y-1],[self.x-2,self.y-2],[self.x-3,self.y-3],[self.x-4,self.y-4],
                     [self.x-5,self.y-5],[self.x-6,self.y-6],[self.x-7,self.y-7]]
        print(all_moves)
        possible_moves = []
        for i in all_moves:
            if (chess_grid.piece_inside_board(i[0],i[1])):
                    possible_moves.append(i)
        print(possible_moves)

class Queen(Pieces):
    def __init__(self, x, y, img_path,color):
        Pieces.__init__(self, x, y, img_path,color)
        
    def possible_moves(self): # Improve Algorithm
        print("Queen") 
        all_moves = [[self.x+1,self.y+1],[self.x+2,self.y+2],[self.x+3,self.y+3],[self.x+4,self.y+4],
                     [self.x+5,self.y+5],[self.x+6,self.y+6],[self.x+7,self.y+7],
                     [self.x,self.y+1],[self.x,self.y+2],[self.x,self.y+3],[self.x,self.y+4],
                     [self.x,self.y+5],[self.x,self.y+6],[self.x,self.y+7],
                     [self.x+1,self.y],[self.x+2,self.y],[self.x+3,self.y],[self.x+4,self.y],
                     [self.x+5,self.y],[self.x+6,self.y],[self.x+7,self.y],
                     
                     [self.x-1,self.y+1],[self.x-2,self.y+2],[self.x-3,self.y+3],[self.x-4,self.y+4],
                     [self.x-5,self.y+5],[self.x-6,self.y+6],[self.x-7,self.y+7],
                     [self.x-1,self.y],[self.x-2,self.y],[self.x-3,self.y],[self.x-4,self.y],
                     [self.x-5,self.y],[self.x-6,self.y],[self.x-7,self.y],
                     
                     [self.x-1,self.y-1],[self.x-2,self.y-2],[self.x-3,self.y-3],[self.x-4,self.y-4],
                     [self.x-5,self.y-5],[self.x-6,self.y-6],[self.x-7,self.y-7],
                     [self.x,self.y-1],[self.x,self.y-2],[self.x,self.y-3],[self.x,self.y-4],
                     [self.x,self.y-5],[self.x,self.y-6],[self.x,self.y-7],
        
                     [self.x+1,self.y-1],[self.x+2,self.y-2],[self.x+3,self.y-3],[self.x+4,self.y-4],
                     [self.x+5,self.y-5],[self.x+6,self.y-6],[self.x+7,self.y-7]]
        print(all_moves)
        possible_moves = []
        for i in all_moves:
            if(chess_grid.piece_inside_board(i[0],i[1])):
                possible_moves.append(i)
        print(possible_moves)
        print(len(possible_moves))

class King(Pieces):
    def __init__(self, x, y, img_path,color):
        Pieces.__init__(self, x, y, img_path,color)
        
    def possible_moves(self):
        print("King")
        all_moves = [[self.x-1,self.y+1],[self.x,self.y+1],[self.x+1,self.y+1],[self.x+1,self.y],
                     [self.x+1,self.y-1],[self.x,self.y-1],[self.x-1,self.y-1],[self.x-1,self.y]]
        print(all_moves)
        possible_moves = []
        for i in all_moves:
            if(chess_grid.piece_inside_board(i[0],i[1])):
                possible_moves.append(i)
        print(possible_moves)
            
class Pawn(Pieces):
    def __init__(self, x, y, img_path, color):
        Pieces.__init__(self, x, y, img_path, color)
        
    def possible_moves(self):
        print("Pawn")
    
class Chess_board:
    def __init__(self, num_rows, num_cols):#pieces
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.game_over = False
    
        self.chess_grid_board = []                  # this is to initialize a grid on the screen
        for row in range(self.num_rows):
            self.chess_row = []               # to iterate through each row
            for col in range(self.num_cols):
                self.chess_row.append(0)
            self.chess_grid_board.append(self.chess_row) 
        print(self.chess_grid_board)                # for test purposes
        
        self.create_pieces()
    
    def get_piece(self, y, x):
        return self.chess_grid_board[x][y]
        
    def create_pieces(self):
        for i in range(num_cols):
            print(i)
            self.chess_grid_board[i][1] = Pawn(i,1, "white_pawn", "white")
            self.chess_grid_board[i][num_rows - 2] = Pawn(i,num_rows - 2, "black_pawn", "black")

        # Improve this code later 
        self.chess_grid_board[0][0] = Rook(0,0, "white_rook", "white")
        self.chess_grid_board[7][0] = Rook(7,0, "white_rook", "white")
        
        self.chess_grid_board[1][0] = Knight(1,0, "white_knight", "white")
        self.chess_grid_board[6][0] = Knight(6,0, "white_knight", "white")
        
        self.chess_grid_board[2][0] = Bishop(2,0, "white_bishop", "white")
        self.chess_grid_board[5][0] = Bishop(5,0, "white_bishop", "white")
    
        self.chess_grid_board[3][0] = Queen(3,0, "white_queen", "white")
        self.chess_grid_board[4][0] = King(4,0, "white_king", "white")
        
        self.chess_grid_board[0][7] = Rook(0,7, "black_rook", "black")
        self.chess_grid_board[7][7] = Rook(7,7, "black_rook", "black")
        
        self.chess_grid_board[1][7] = Knight(1,7, "black_knight", "black")
        self.chess_grid_board[6][7] = Knight(6,7, "black_knight", "black")
        
        self.chess_grid_board[2][7] = Bishop(2,7, "black_bishop", "black")
        self.chess_grid_board[5][7] = Bishop(5,7, "black_bishop", "black")
    
        self.chess_grid_board[3][7] = Queen(3,7, "black_queen", "black")
        self.chess_grid_board[4][7] = King(4,7, "black_king", "black")
    
        
        print(self.chess_grid_board)
        return
         
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
    
    def display(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                if self.chess_grid_board[i][j]:
                    self.chess_grid_board[i][j].display_pieces()
        # color = ["white_" + piece, "black_" + piece]
        # counter = 0 
        # num = len(coords)
        # limit = num // 2
        # for i in coords:
        #     if counter < limit:
        #         tempStr = "{}({}, {}, '{}')".format(piece.capitalize(), i[0], i[1], color[0])
        #         print(tempStr)
        #         eval(tempStr).display_pieces()
        #     else:
        #         tempStr = "{}({}, {}, '{}')".format(piece.capitalize(), i[0], i[1], color[1])
        #         eval(tempStr).display_pieces()
        #         print(tempStr)
        #     counter += 1 
    
    # def display_pawn(self):
    #     for i in range(num_cols):
    #         pawn_w = Pawn(i,1, "white_pawn", "white")
    #         pawn_w.display_pieces()
        
    #     for j in range(num_cols):
    #         pawn_b = Pawn(j,6, "black_pawn", "black")
    #         pawn_b.display_pieces()
    
    def piece_inside_board(self, y, x):
        if (x < 0) or (x > 7) or (y < 0) or (y > 7):
            False
        else:
            return True
        
    def ally_or_foe(self):
        
        pass
    
chess_grid = Chess_board(num_rows, num_cols) #pieces
  
def setup():
    size(num_rows * cell_height, num_cols * cell_width)

def draw():
    chess_grid.display_background()
    # chess_grid.display("rook", [[0,0],[7,0],[0,7],[7,7]])
    # chess_grid.display("knight", [[1,0],[6,0],[1,7],[6,7]])
    # chess_grid.display("bishop", [[2,0],[5,0],[2,7],[5,7]])
    # chess_grid.display("queen", [[3,0],[3,7]])
    # chess_grid.display("king", [[4,0],[4,7]])
    chess_grid.display()

def mouseClicked(self):
    col = mouseX // cell_width
    row = mouseY // cell_height
    print("clicked at "  + str(row) + " " + str(col))
    
    
    piece = chess_grid.get_piece(row, col)
    print(piece)
    piece.possible_moves()

print(chess_grid.create_pieces())
