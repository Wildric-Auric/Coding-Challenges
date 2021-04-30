#Challenge: https://www.codewars.com/kata/54b72c16cd7f5154e9000457

def decode_morse(morse_code):
    list = morse_code.split("   ")
    while "" in list: list.remove("")
    for i in range(len(list)):      
        list[i] = list[i].split()
        for j in range(len(list[i])):
            list[i][j] = MORSE_CODE[list[i][j]]
        list[i] = "".join(list[i])
    list = " ".join(list)
    return list

def decode_bits(bits):
    while bits[0] == '0':
        bits = bits.replace(bits[0:bits.index("1")],"",1)
        bits = bits[::-1]
    zeros = [];
    ones = []
    t0, t1 = 0,0
    for i in bits:
        if i == "0":
            if t1!=0 and t1 not in ones:
                ones.append(t1)
            t1 = 0
            t0 +=1
        else: 
            if t0 != 0 and t0 not in zeros:
                zeros.append(t0)
            t0=0
            t1 +=1
    if t0 != 0 and t0 not in zeros:
       zeros.append(t0)
    if t1!=0 and t1 not in ones:
       ones.append(t1)
       
    zeros.sort()
    ones.sort()
    sum = list(set((ones.copy() + zeros.copy())))
    one = min(sum)
    spaces = ["   "," ", ""]
    num = [7*one, 3*one, one]
    if 3*one*'1' in bits:
        bits = bits.replace(3*one*'1', '-')
    if one*'1' in bits:
        bits = bits.replace(1*one*'1', '.')
    for i in range(len(num)):
        if num[i]*'0' in bits:
            bits = bits.replace(num[i]*'0', spaces[i])
    return (bits) 
