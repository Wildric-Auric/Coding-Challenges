#Do you know connect four game? This program, according to players decisions find who's the winner: Yellow or Red; alphabets are refering to columns
dic = {"A" : 1, "B" : 2, "C":3, "D" :4, "E" :5, "F": 6, "G" : 7}
directions = {0: (0, 1) ,1: (0,-1), 2:(-1,-1) ,3:(1,1) ,4:(1,-1) ,5:(-1,1), 6:(-1,0)}

#prevent out of range
def index_exists(index, x):
    return 0<= index < len(x) 
Once = False
def winning_check(x,y, element, list):
    dir = 0
    count = 1
    count1 = 0
    while dir < 7:
        if count1 == 2:
            count = 1
            count1 = 0
        if dir == 6:
           count = 1
          
        for i in range(1,4):
            a =i*(directions[dir][0])
            b = i*(directions[dir][1])
            if index_exists(x+a,list):
                if index_exists(y+b,list[x+a]):
                    if list[x+a][y+b] == element:
                        count += 1    
                    else: 
                        break
                else:
                   break 
        if count >= 4:
            return element          
        dir +=1
        count1 +=1
def who_is_winner(k):
    arr = []
    Rows = 6;
    Columns = 7
    empty = ["0","0","0","0","0","0","0"]
    for i in range(Rows):
            arr.append(empty.copy())
    for i in k:
        pos = dic[i[0]]
        temp = ""
        for r in range(2,len(i)): #to fill array with "Yellow" and "Red"
            temp += i[r]
        for j in range(Rows-1, 0, -1):
            end = False
            if arr[j-1][pos-1] != "0":
                arr[j][pos-1] = temp
                R = j
                end = True
                
            elif j-1 == 0:
                arr[j-1][pos-1] = temp
                R = j-1
               
                end = True
            if end == True:
                break
        t = winning_check(R,pos-1, temp, arr)
        if t == temp:
           return t
    return "Draw"


dic = {"A" : 1, "B" : 2, "C":3, "D" :4, "E" :5, "F": 6, "G" : 7}
directions = {0: (0, 1) ,1: (0,-1), 2:(-1,-1) ,3:(1,1) ,4:(1,-1) ,5:(-1,1), 6:(-1,0)}

#prevent out of range
def index_exists(index, x):
    return 0<= index < len(x) 
Once = False
def winning_check(x,y, element, list):
    dir = 0
    count = 1
    count1 = 0
    while dir < 7:
        if count1 == 2:
            count = 1
            count1 = 0
        if dir == 6:
           count = 1
          
        for i in range(1,4):
            a =i*(directions[dir][0])
            b = i*(directions[dir][1])
            if index_exists(x+a,list):
                if index_exists(y+b,list[x+a]):
                    if list[x+a][y+b] == element:
                        count += 1    
                    else: 
                        break
                else:
                   break 
        if count >= 4:
            return element          
        dir +=1
        count1 +=1
def who_is_winner(k):
    arr = []
    Rows = 6;
    Columns = 7
    empty = ["0","0","0","0","0","0","0"]
    for i in range(Rows):
            arr.append(empty.copy())
    for i in k:
        pos = dic[i[0]]
        temp = ""
        for r in range(2,len(i)): #to fill array with "Yellow" and "Red"
            temp += i[r]
        for j in range(Rows-1, 0, -1):
            end = False
            if arr[j-1][pos-1] != "0":
                arr[j][pos-1] = temp
                R = j
                end = True
                
            elif j-1 == 0:
                arr[j-1][pos-1] = temp
                R = j-1
               
                end = True
            if end == True:
                break
        t = winning_check(R,pos-1, temp, arr)
        if t == temp:
           return t
    return "Draw"
