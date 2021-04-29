#Challenge: https://www.codewars.com/kata/5765870e190b1472ec0022a2
#Main function in path_finder()
def empty(x,y, maze): #Check if the position is empty
  if (x>=len(maze) or y >=len(maze) or x< 0 or y < 0): 
    return False
  elif maze[y][x] == ".":
    return True
  else: return False

dir = [(1,0), (0,1), (0,-1), (-1,0)] # all directions used in a loop to prevent use of if else

def path_finder(maze):
  maze = maze.split()
  for i in range(len(maze)):
     maze[i] = (" ").join(maze[i]).split(" ") #the argument is a string it's changed into a list
  x,y = 0,0
  return pathf(maze,x,y)
  
def pathf(maze, x, y):
      for i in dir:
        if (x == len(maze)-1 and y == len(maze)-1):
          return True
        elif empty(x+i[0], y+i[1], maze): #Checks emptiness of next position and apply parhf on it
          maze[y][x]="O" #put in passed position O to prevent a loop
          if pathf(maze, x+i[0],y+i[1]):
            return True #Recusively, if you reach the and all what is before is true
      return False
