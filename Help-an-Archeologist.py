#The challenge: https://www.codewars.com/kata/546d15cebed2e10334000ed9/python

import operator as op
ops = {"+": op.add, "-": op.sub, "*":op.mul}
opList = ["+", "-", "*", "="]
def solve_runes(runes):
    first = ""
    second = ""
    operator = ""
    once = False
    j =0
    for i in range(len(runes)):
        if runes[i] == "?":
            if i-1 <=0 and runes[i+1] not in opList:
                j = 1
            if i +1 <len(runes):
                if (runes[i-1] in opList and not runes[i+1] in opList):
                    j = 1
            
        if i < runes.index("="):
            if i != 0 and (not runes[i].isdigit()) and runes[i] != "?" and once == False:
                once = True
                operator = runes[i]
            first += runes[i]
        elif i > runes.index("="):
            second += runes[i]
    
    while j < 10:
        sec = second
        fir = first
        fir = fir.replace("?",str(j))
        sec = int(sec.replace("?",str(j)))
        fir = ops[operator](int(fir[0:fir.index(operator,1)]), int(fir[fir.index(operator,1)+1:]))
        if fir == sec and str(j) not in runes:
            return j
        j+=1
    return -1
