#Challenge: https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7/python

diagonals = [(1,1), (1,-1), (-1,-1), (-1,1)]
def index_exist(indice, matrix):
    return 0<=indice<=len(matrix)

def validate_battlefield(field):
    s1,s2,s3,s4 = 0,0,0,0
    for x in range(len(field)):
        for y in range(len(field[x])):
            if (field[x][y] == 1):
                #checks diagonals   
                if x in range(1, len(field)-1) and y in range(1,len(field[x])-1):
                    for i in diagonals:
                        if field[x+i[0]][y + i[1]] != 0:
                            return False
                tempX = x
                tempY = y
                while tempY+1 < len(field) and field[x][tempY +1] == 1:
                        field[x][tempY + 1] += field[x][tempY]
                        tempY +=1
                        
                if field[x][tempY] > 4:
                    return False
                elif field[x][tempY] == 4:
                    s4 +=1
                elif field[x][tempY] == 3:
                    s3 +=1
                elif field[x][tempY] == 2:
                    s2 += 1
                    
                while tempX+1 < len(field) and field[tempX+1][y] == 1:
                        field[tempX + 1][y] += field[tempX][y]
                        tempX +=1
                        
                if field[tempX][y] > 4:
                    return False
                if field[tempX][y] == 4:
                    s4 +=1                
                elif field[tempX][y] == 3:
                    s3 +=1
                elif field[tempX][y] == 2:
                    s2 += 1
                if field[x][tempY] == 1 and field[tempX][y] == 1:
                    s1+=1
    if (s1,s2,s3,s4) == (4,3,2,1):
        return True
    return False

diagonals = [(1,1), (1,-1), (-1,-1), (-1,1)]
def index_exist(indice, matrix):
    return 0<=indice<=len(matrix)

def validate_battlefield(field):
    s1,s2,s3,s4 = 0,0,0,0
    for x in range(len(field)):
        for y in range(len(field[x])):
            if (field[x][y] == 1):
                #checks diagonals   
                if x in range(1, len(field)-1) and y in range(1,len(field[x])-1):
                    for i in diagonals:
                        if field[x+i[0]][y + i[1]] != 0:
                            return False
                tempX = x
                tempY = y
                while tempY+1 < len(field) and field[x][tempY +1] == 1:
                        field[x][tempY + 1] += field[x][tempY]
                        tempY +=1
                        
                if field[x][tempY] > 4:
                    return False
                elif field[x][tempY] == 4:
                    s4 +=1
                elif field[x][tempY] == 3:
                    s3 +=1
                elif field[x][tempY] == 2:
                    s2 += 1
                    
                while tempX+1 < len(field) and field[tempX+1][y] == 1:
                        field[tempX + 1][y] += field[tempX][y]
                        tempX +=1
                        
                if field[tempX][y] > 4:
                    return False
                if field[tempX][y] == 4:
                    s4 +=1                
                elif field[tempX][y] == 3:
                    s3 +=1
                elif field[tempX][y] == 2:
                    s2 += 1
                if field[x][tempY] == 1 and field[tempX][y] == 1:
                    s1+=1
    if (s1,s2,s3,s4) == (4,3,2,1):
        return True
    return False
