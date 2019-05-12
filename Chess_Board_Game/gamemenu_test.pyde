### Creating Game class 

class Button: 
    def __init__(self,label,x,y, height,width): 
        self.label = label 
        self.x = x
        self.y = y 
        self.height = height 
        self.width = width 

    def contains_mouse(self):
        return self.x <= mouseX <= self.x + self.width and self.y - self.height <= mouseY <= self.y
        
    def display(self):
        print(self.x, mouseX, self.x + self.width)
        if self.contains_mouse():
            print("stroke is being called")
            fill(255, 0, 0)
        else:
            fill(255)
            textSize(40)
            text(self.label, self.x, self.y)
    
print("breaker")
def mouseClicked():
    col = mouseX // cell_width
    row = mouseY // cell_height
    print("clicked at "  + str(row) + " " + str(col))
    
    #piece = chess_grid.get_piece(row, col)
    #chess_grid.user_clicked(row, col)
    print(piece, row, col)
    #piece.possible_moves()

class Game: 
    def __init__(self, width,height): 
        print("Initializing GameDisplay")
        self.width = width 
        self.height = height 
        self.state = "menu"
        self.buttons = [] 
        #self.sound_beginning = audioPlayer.loadFile(path + "sound/")
        
        # Add Buttons; Start, Instruction, Scoreboard 
        self.buttons.append(Button("Start Game", self.width//2-100, self.height//2 - 50, 50, 250))
        self.buttons.append(Button("Instructions", self.width//2-100, self.height//2 - 50, 50, 250))
        self.buttons.append(Button("Scoreboard", self.width//2-100, self.height//2 - 50, 50, 250))
    
    def displayMenu(self):
        background(0)
        
        for button in self.buttons:
            button.display()
        
    def display(self):
        if self.state == "menu": 
            self.displayMenu()
        elif self.state =="game":
            self.displayGame()
                
GameDisplay = Game(500,500) 

def setup():
    size(500,500)
    # print("Literally anything")

def draw():
    GameDisplay.display()
    
