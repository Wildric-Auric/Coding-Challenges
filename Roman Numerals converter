

a = {
"I" : 1, "V" :5, "X" :10, "L" : 50,"C" :100,"D" :500,"M" :1000, "": 0 #exception
}
b = dict(map(reversed, a.items())) 
    
c = { 2: [1,1], 3:[1,1,1], 4:[1,5], 6:[5,1], 7:[5,1,1], 8:[5,1,1,1], 9:[1,10], }
b.update(c)
class RomanNumerals:    
    def from_roman(HolyNumber):
        Num = 0
        temp = 0
        sum = 0
        isUsed = False # it's set to add last number (due to the messy manner I coded this)
        i=0
        while i < (len(HolyNumber)-1):
            temp = 0
            if a[HolyNumber[i]] >= a[HolyNumber[i+1]]:
                temp += a[HolyNumber[i]]
            else:
                temp = -a[HolyNumber[i]] +  a[HolyNumber[i+1]]
                i+=1
                isUsed = True
            Num +=temp
            i+=1
        if isUsed == False:
            Num +=a[HolyNumber[len(HolyNumber)-1]]    
        return Num
      
    def to_roman(ArabicNumber):
        Num = ""
        n = str(ArabicNumber)
        i = 0
        j = len(n) -1
        while i <len(n):
            temp = int(n[i]) 
            power = 10**j
            if type(b[temp]) is list:
                for e in b[temp]:
                    Num += b[e * power]
         
            else:
                Num += b[temp * power]
            j -=1
            i +=1
        return Num
