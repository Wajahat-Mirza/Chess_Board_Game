# Name: Muhammad Wajahat Mirza (mwm356) and Abraham Okbasslaise Hdru (ah3300)
# Date: May 6th 2019
# Description : Final Project Chess

import os 
path = os.getcwd()
add library("minim")
audio_track = Minim(this)

num_rows = 8 
num_cols = 8 
cell_height = 64
cell_width  = 64

class Pieces:
    def __init__(self, x, y, img_path):
        self.x, self.y = x, y
        self.img_path = img_path
        self.backend_game_sound = audio_track.loadFile(path + "/sounds/chessbackground") # Need to download sound tracks

    def convertCoord(self,x,y):
        return x * cell_width,y * cell_height
   
    def display_pieces(self):
        piece_img  = loadImage(path + "/images/" + self.img_path + ".png")
        x, y = self.convertCoord(self.x, self.y)
        image(piece_img, x, y, cell_width, cell_height)
    
class Rook(Pieces):
    def __init__(self, x, y, img_path):
        Pieces.__init__(self, x, y, img_path)
        
    def possible_moves(self):
        all_moves = [] 
        for y in range(self.y, num_rows):
            for x in range(self.x, num_cols):
            #if self.x != Pieces: 
                all_moves.append((x, y))
        print(len(all_moves))
        # for x in range(self.x, num_cols):
        #     #if self.y != Pieces: 
        #         solutionMoves.append((self.y,x))
        #     print(x)
        
        print("rook")
        #returns the possible moves

class Knight(Pieces):
    def __init__(self, x, y, img_path):
        Pieces.__init__(self, x, y, img_path)
        
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
    def __init__(self, x, y, img_path):
        Pieces.__init__(self, x, y, img_path)
    
    def possible_moves(self): 
        directions = [[1,1],[-1,1],[-1,-1],[1,-1]]
        moves = []
        possible_x = self.x
        possible_y = self.y
        for direction in directions: #search for squares in every direction diagonally around the piece
            for counter in range(0,8):
                possible_x += direction[0]
                possible_y += direction[1]
                if(chess_grid.piece_inside_board(possible_x,possible_y)): 
                    moves.append([possible_x,possible_y])
                else: 
                    break
        print(moves)
        return moves
        # problems here: 1. rather than on 6,6, it comes on 7,7 and rather than 1,1 it comes on 0,0.
        # 2. works fine for white bishops. Doesn't work fully for black bishops
    
    def obtain_possible_moves(self):
        possible_moves = self.possible_moves()
        print(possible_moves)
        return possible_moves

class Queen(Pieces):
    def __init__(self, x, y, img_path):
        Pieces.__init__(self, x, y, img_path)
        
    def possible_moves(self):
        print("Queen") 

class King(Pieces):
    def __init__(self, x, y, img_path):
        Pieces.__init__(self, x, y, img_path)
        
    def possible_moves(self):
        print("King")
        all_moves = [[self.x-1,self.y+1],[self.x,self.y+1],[self.x+1,self.y+1],[self.x+1,self.y],
                     [self.x+1,self.y-1],[self.x,self.y-1],[self.x-1,self.y-1],[self.x-1,self.y]]
        print(all_moves)
       
        possible_moves = []
        for i in all_moves:
            if(chess_grid.piece_inside_board(i[0],i[1])):
           # if i[0] < 0 or i[1] <0 or i[0] > 7 or i[1] > 7:
               # continue
                possible_moves.append(i)
        print(possible_moves)
            
class Pawn(Pieces):
    def __init__(self, x, y, img_path):
        Pieces.__init__(self, x, y, img_path)
        
    def possible_moves(self):
        print("Pawn")
    
class Chess_board:
    def __init__(self, num_rows, num_cols):#pieces
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
        
    def get_piece(self, y, x):
        for piece in self.pieces:
            if piece.y == y and piece.x == x:
                return piece
        # return a piece corresponding to x and y
        
    def create_pieces(self):
        chess_pieces = []
        for i in range(num_cols):
            pawn_w = Pawn(i,1, "white_pawn")
            chess_pieces.append(pawn_w)

        rook_white_left = Rook(0,0, "white_rock") 
        chess_pieces.append(rook_white_left)
        rook_white_right = Rook(7,0, "white_rock")
        chess_pieces.append(rook_white_right)
        
        knight_white_left =Knight(1,0, "white_knight")
        chess_pieces.append(knight_white_left)
        knight_white_right =Knight(6,0, "white_knight")
        chess_pieces.append(knight_white_right)
        
        bishop_white_left = Bishop(2,0, "white_bishop")
        chess_pieces.append(bishop_white_left)
        bishop_white_right = Bishop(5,0, "white_bishop")
        chess_pieces.append(bishop_white_right)
        
        queen_white = Queen(3,0, "white_queen")
        chess_pieces.append(queen_white)
        king_white =King(4,0, "king_white") 
        chess_pieces.append(king_white)
        
        for j in range(num_cols):
            pawn_b = Pawn(j,6, "black_pawn")
            chess_pieces.append(pawn_b)
       
        rook_black_left = Rook(0,7, "black_rock") 
        chess_pieces.append(rook_black_left)
        rook_black_right = Rook(7,7, "black_rock")
        chess_pieces.append(rook_black_right)
        
        knight_black_left =Knight(1,7, "black_knight")
        chess_pieces.append(knight_black_left)
        knight_black_right =Knight(6,7, "black_knight")
        chess_pieces.append(knight_black_right)
        
        bishop_black_left = Bishop(2,7, "black_bishop")
        chess_pieces.append(bishop_black_left)
        bishop_black_right = Bishop(5,7, "black_bishop")
        chess_pieces.append(bishop_black_right)
        
        queen_black = Queen(3,7, "black_queen")
        chess_pieces.append(queen_black)
        king_black =King(4,7, "black_white") 
        chess_pieces.append(king_black)
        return chess_pieces
        print(chess_pieces)
         
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
    
    def piece_inside_board(self, y, x):
        if (x < 0) or (x > 7) or (y < 0) or (y > 7):
            return False
        else:
            return True
    
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
    chess_grid.display_pawn()

def mouseClicked(self):
    col = mouseX // cell_width
    row = mouseY // cell_height
    print("clicked at "  + str(row) + " " + str(col))
    
    
    piece = chess_grid.get_piece(row, col)
    print(piece)
    piece.possible_moves()
