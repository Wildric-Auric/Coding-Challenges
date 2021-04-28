#Input must be 2D list representing sudoku board
def Possible(couple, board, num):
    #Check the row
    for i in range(len(board[0])):
        if board[couple[0]][i] == num and i != couple[1]:
            return False
    #Check the column
    for i in range(len(board[0])):
        if board[i][couple[1]] == num and i != couple[0]:
            return False
    #Chceck squares
    x = couple[0]//3
    y = couple[1]//3
    for i in range(x*3, x*3+3):
        for j in range(y*3, y*3+3):
            if board[i][j] == num and (i,j) != couple:
                return False
    return True
def empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return(i,j)
    return False

def sudoku(sud):
    nxt =  empty(sud)
    if nxt == False:
        return sud
    else: 
        (x,y) = nxt
    for i in range(1,10):
        if Possible(nxt,sud,i):
            sud[x][y] = i
            if sudoku(sud): 
                return sud
            sud[x][y] = 0
