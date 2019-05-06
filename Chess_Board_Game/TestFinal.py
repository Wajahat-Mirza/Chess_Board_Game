#Creating the grid 
def make_grid():
  #initialize empty grid
  grid=[]
  for row in range(numRows):
    #creates a list for the row
    rowList=[]
    for col in range(numCols):
      rowList.append(' ')
    # adds a row to the grid
    grid.append(rowList) 
  return grid

#creating a function to print the grid/aesthetics
def print_bsgrid(grid):
  for col in range(numCols):
    #Use ASCII to change num var to its coresponding letter
    print('  '+chr(col + 65),end=' ') #'end' separates each string/character from each other 

  print()

  for row in range(numRows):
    print(row,end='')
    for col in range(numCols):
      print(grid[row][col]+'  |',end='')
    print('\n' + ' '+'---+'*numCols)
