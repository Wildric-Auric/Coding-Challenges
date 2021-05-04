#Challenge: https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/python


def snail(array):
    #I know it"s messy
    if array == [[]]:
        return []
    if len(array) == 1 and len([array[0]]) == 1:
        return [array[0][0]]
    print(array)
    result =[]
    end = False
    while end == False:
        i = 0
        j = 0

        while i < len(array[0]):
             result.append(array[0][i])
             array[0].pop(i)
        array.pop(0)
        i = len(array) -1

        while j < len(array):
            result.append(array[j][len(array[j])-1])
            array[j].pop(len(array[j])-1)
            j+=1
        while i >= 0:
            result.append(array[len(array)-1][i])
            array[len(array)-1].pop(i)
            i = len(array[len(array)-1]) -1
        array.pop(len(array)-1)
        j = len(array) -1
        while j >= 0:
            result.append(array[j][0])
            array[j].pop(0)
            j-=1
        if array == [[]] or array == []:
            end = True
        if len(array) == 1:
            end = True
            result.append(array[0][0])
    return result
