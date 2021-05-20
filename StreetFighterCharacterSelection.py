#The challenge: https://www.codewars.com/kata/58583922c1d5b415b00000ff/python

dir = {"up": (-1,0),"down":(1,0), "right":(0,1), "left":(0,-1)}
def super_street_fighter_selection(fighters, position, moves):
    length, length1, solution = len(fighters[0]), len(fighters), []
    pos = list(position)
   
    for i in moves:
        x = dir[i][0]
        y = dir[i][1]
        
        pos[1] = (pos[1] + y)%length
        last = pos[0]
        pos[0] += x * (pos[0]+x >= 0 and pos[0] + x < length1)
        while fighters[pos[0]][pos[1]] == "":
            if pos[0] == last:
                 pos[1] = (pos[1] + y)%length
            else:
                pos[0] = last
        solution.append(fighters[pos[0]][pos[1]])
    return solution
