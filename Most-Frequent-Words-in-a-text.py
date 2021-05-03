#Challenge: https://www.codewars.com/kata/51e056fe544cf36c410000fb

def sort_matrice(d):
    #To sort martices 
    t = []
    for i in range(len(d)):
        t.append(d[i][1])
    for k in range(1, len(t)):
        temp = t[k]
        j = k
        while j > 0 and temp < t[j-1]:
            t[j], t[j-1] = t[j-1], t[j]
            d[j], d[j-1] = d[j-1], d[j]
            j -=1
            t[j]= temp
    return d

def top_3_words(text):
    
    forbidden = ["?", ".", ";", ":", "!", ",", "-", "/",'"'," - " "'", "_"]
    for i in forbidden:
        text = text.replace(i, " ") # Convert every unsuseful character to space which can be converted to list after
    arr = (text.lower()).split()
  
    result = []
    result = list(set(arr)) #To get a list of unique values only
    for i in result:
        end = False
        for j in i:
            if j.isalpha(): # to prevent problem of apostrophe and something like that
                end = True;
        if end == False:
            result.pop(result.index(i))
           
    for i in range(len(result)):
        result[i] = [result[i],0] #Make martrice of each element with zeros in columns
    for i in range(len(result)):
        for j in arr:
            if result[i][0] == j:
                result[i][1] += 1 #Make column increase by one each time it finds another j element
    result = sort_matrice(result)
    result.reverse()
    if len(result)>3:
        for i in range(3,len(result)):
            result.pop() #deletes all elements after the third
    result1 = []
    for i in result: #Thought I needed the element and also it's number... So this will just take only the numbers
        result1.append(i[0])
    return result1
