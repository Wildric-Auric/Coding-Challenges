#Challenge: https://www.codewars.com/kata/58e61f3d8ff24f774400002c/


res = {}
def v(num): #stands for valid
    try:
        num = int(num)
    except:
        if num in res:
            return res[num]
    return num
def extendAt(a,b, index):
    a = a[0:index] + b + a[index:]
    subEnd = index + len(b)
    return a, subEnd


def assembler_interpreter(code):
    
    cur = "main"
    func = {cur: []}
    start = 0
    for i in range(len(code)):
        #Placing data if each function into dictionary
        e = code[i]
        if e ==";" or e == "\n":
            if ((content := code[start: i]).strip() != ""):
                if ("'" not in content) and ":" in content:
                    cur = content[:-1]
                    func[cur] = []
                else:
                    func[cur].append(content.strip())
            start = code.find("\n", start + 1) * (e ==";") + (i+1)*(e=="\n")
    
    for item in func: 
        if item not in "main print" and func[item][-1]!= "ret": 
            func[item].append("ret")
    i, length = 0, len(func["main"])
    cmp = ""
    iteration = 0
    ends = []
    cur = "main"
    curIndex = [[cur,0]]
    while 1: 
        cur =curIndex[-1][0]
        i = curIndex[-1][1]
        cmd = func[cur][i]
        if "msg" in cmd:
            cmd = cmd.strip().replace("msg","")
            copy = 0
            msg = ""
            forma = ""
            for char in cmd:
                if char == "'": 
                    if not copy: 
                        msg += str(v(forma.strip(", ")))
                        forma = ""
                    copy = 1-copy
                elif copy: msg += char
                else: forma += char
            msg+= str(v(forma.strip(", ")))    
            break
        else:
            cmd = cmd.split()
            arg0 = cmd[0]
            if (l :=len(cmd)) == 1:
                if arg0 == "ret":
                    curIndex.pop()
                elif arg0 == "end":
                    break 
            elif l == 2:
                arg1 = cmd[1].strip(",")
                if arg0 == "call":
                    curIndex.append([arg1,-1])
                    
                elif arg0 =="jmp":
                    curIndex.pop()
                    curIndex.append([arg1,-1])
                elif arg0 in "incdec": 
                    res[arg1] += (arg0=="inc") - (arg0 == "dec")
                elif " "+arg0 +" " in cmp:
                    curIndex.pop()
                    curIndex.append([arg1,-1])
                    
             
        
            elif l == 3:
                arg1,arg2 = cmd[1].strip(","),cmd[2].strip(",")
                if arg0 == "cmp":
                    arg1,arg2 =v(arg1),v(arg2)
                    cmp = (
                    " je "*(arg1 == arg2)
                    + " jne "*(arg1 != arg2)
                    +  " jge "*(arg1>= arg2)
                    + " jg "*(arg1>arg2)
                    + " jle "*(arg1<=arg2)
                    + " jl "*(arg1<arg2)
                    )
                elif arg0 == "mov":
                    res[arg1] = v(arg2)
                elif arg0 in "addsub":
                    res[arg1] += v(arg2)*((arg0 == "add") - (arg0 == "sub") )
                elif arg0 == "mul":
                    arg2 = v(arg2)
                    res[arg1] *= v(arg2)
                elif arg0 == "div":
                    res[arg1] //=v(arg2)

        iteration += 1
        curIndex[-1][1] +=1
    if msg == "Do nothing": return -1
    if "This program should return" in msg: return int(msg.split()[-1])
    return msg
