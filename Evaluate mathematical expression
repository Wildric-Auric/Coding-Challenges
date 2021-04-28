# Challenge: https://www.codewars.com/kata/52a78825cdfc2cfc87000005
#I tried to do this without using recursion or RPN (Reverse Polish Notation)
import operator as ope
ops = {"+": ope.add, "-":ope.sub, "*":ope.mul, "/":ope.truediv}
All = ["-", "+", "*", "/"]
def simple(exp):
    i = 0
    while "--" in exp:
        exp = exp.replace("--", "+")
    while i<len(exp)-1:
        if exp[i] == "+":
            if exp[i] == exp[i+1]:
                exp = exp.replace("++", "+", i)
                i-=1
        i+=1
    while "-+" in exp:
        exp = exp.replace("-+", "-")
    while "+-" in exp:
        exp = exp.replace("+-", "-")
    for i in All:
        if i in exp:
            exp = exp.replace(i, " " + str(i) + " ")
    exp = exp.split()
    i = 0
    #create an array where there are numbers (negatives and positives, separated by their opearators)
    while i in range(len(exp)-1):
        if exp[i] in All and exp[i+1] in All:
            exp[i+1:i+3] = ["".join(exp[i+1: i+3])]
            i-=1
        elif exp[i] not in All:
            exp[i] = exp[i]
        i+=1
    if exp[0] in All:
        exp[ :2] = ["".join(exp[:2])]  
    exp[len(exp)-1] = (exp[len(exp)-1])
    n = 0
    for i in exp[0]:
        if i.isdigit():
            break
        if i == "-":
            n +=1
    #to multiply
    while "*" in exp or "/" in exp:
        i = 1
        while i < len(exp) - 1:
            if exp[i] == "*" or exp[i] == "/" :
                exp[i-1: i+2] = [ops[exp[i]](float(exp[i-1]), float(exp[i+1]))]
                i=-1
            i+=1
    #to add 
    while "+" in exp or "-" in exp:
        i = 1
        while i < len(exp) - 1:
            if exp[i] == "-" or exp[i] == "+" :
                exp[i-1: i+2] = [ops[exp[i]](float(exp[i-1]), float(exp[i+1]))]
                i=-1
            i+=1
    return str(exp[0])

def calculate_paren(k):
    i = len(k)-1
    test = []
    while i > -1:
        if k[i] == "(":
            calculated = simple(k[i+1: k.index(")",i+1)])
            k = k.replace(k[i: k.index(')', i) +1], calculated)
        i-=1
        test.append(k)
    # print(dict.fromkeys(test).keys())
    return k
def calc(expression):
    expression = "".join(expression.split())
    i = 0
    while "--" in expression:
        expression = expression.replace("--", "+")
    while i<len(expression)-1:
        if expression[i] == "+":
            if expression[i] == expression[i+1]:
                expression = expression.replace("+", "", i)
                i-=1
        i+=1
    exp = simple(calculate_paren(expression))
    return float(exp)
