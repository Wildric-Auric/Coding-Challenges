def next_bigger(n):
    txt = str(n)
    result = []
    array = []
    for i in txt:
        array.append(int(i))
    array.reverse()
    i = 1
    j = 0
    temp = 0
    end = False
    while i < len(array) and end == False:
        j = 0
        while j < i and end == False:
            if array[i] < array[j]:
                temp = i
                array[j], array[i] = array[i], array[j]
                j = 0
                last = 0
                end = True
            j+=1
        i+=1
    while j < temp:
        while last < j:
            if array[j] > array[last]:
                array[j], array[last] = array[last], array[j]
                last = -1
                j = -1
            last += 1
        j+=1
    array.reverse()
    result = int("".join([str(num) for num in array]))
    if result == n:
        return -1
        
    return result
def next_bigger(n):
    txt = str(n)
    result = []
    array = []
    for i in txt:
        array.append(int(i))
    array.reverse()
    i = 1
    j = 0
    temp = 0
    end = False
    while i < len(array) and end == False:
        j = 0
        while j < i and end == False:
            if array[i] < array[j]:
                temp = i
                array[j], array[i] = array[i], array[j]
                j = 0
                last = 0
                end = True
            j+=1
        i+=1
    while j < temp:
        while last < j:
            if array[j] > array[last]:
                array[j], array[last] = array[last], array[j]
                last = -1
                j = -1
            last += 1
        j+=1
    array.reverse()
    result = int("".join([str(num) for num in array]))
    if result == n:
        return -1
        
    return result
