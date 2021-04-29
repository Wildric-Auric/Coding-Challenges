#The challenge: https://www.codewars.com/kata/59d582cafbdd0b7ef90000a0

def split(txt):
    l = txt.split("\n")
    for i in range(len(l)):
        l[i] = l[i][l[i].index(":")+2:] #Less optimized than next one i think but less lines
    return l
    
    

def convertDate(string):
    string = string.split(".")
    return int(string[0])*365 + int(string[1])*30 + int(string[2])

class passport:
    def __init__(self, ID, NATION, NAME, DOB, SEX, ISS, EXP):
        self.ID, self.NATION, self.NAME, self.DOB, self.SEX, self.ISS, self.EXP = ID, NATION, NAME, DOB, SEX, ISS, EXP
    
class asylum:
    def __init__(self, NAME, NATION, ID, HEIGHT, WEIGHT, EXP):
        self.NAME, self.NATION, self.ID, self.HEIGHT, self.WEIGHT, self.EXP = NAME, NATION, ID, HEIGHT, WEIGHT, EXP
     
class permit:
    def __init__(self, NAME, NATION, ID, PURPOSE, DURATION, HEIGHT, WEIGHT, EXP):
        self.NAME, self.NATION, self.ID, self.PURPOSE, self.DURATION, self.HEIGHT, self.WEIGHT, self.EXP = NAME, NATION, ID, PURPOSE, DURATION, HEIGHT, WEIGHT, EXP

class IDC:
    def __init__(self, NAME, DOB, HEIGHT, WEIGHT):
      self.NAME, self.DOB, self.HEIGHT, self.WEIGHT = NAME, DOB, HEIGHT, WEIGHT
      
class vaccine:
    def __init__(self, NAME, ID, VACCINES):
        self.NAME, self.ID, self.VACCINES = NAME, ID, VACCINES
    
class wp:  
    def __init__(self,NAME, FIELD, EXP):
        self.NAME, self.FIELD, self.EXP = NAME, FIELD, EXP
        
class da:
    def __init__(self, NAME, NATION, ID, ACCESS):
        self.NAME, self.NATION, self.ID, self.ACCESS = NAME, NATION, ID, ACCESS

class citizen:
    all = []
    def __init__(self, Nationality, isAllowed, rID, rAccessPermit, rVaccines): #r stands for required
         self.all.append(self)
         self.Nationality, self.isAllowed, self.rID,self.rAccessPermit, self.rVaccines =  Nationality, isAllowed, rID, rAccessPermit, rVaccines

#Initialize an object of eachnationality
#Arstotzka, Antegria, Impor, Kolechia, Obristan, Republia, and United Federation
fromArstotzka = citizen("Arstotzka", False, False, False, [])
fromAntegria= citizen("Antegria", False, False, False, [])
fromImpor = citizen("Impor", False, False, False, [])
fromKolechia = citizen("Kolechia", False, False, False, [])
fromObristan = citizen("Obristan", False, False, False, [])
fromRepublia = citizen("Republia", False, False, False, [])
fromUnitedFederation = citizen("United Federation", False, False, False, [])


wanted = []
workPass = False
date = 11*30 + 22 + 1982*365


class Inspector:
    def receive_bulletin(a,bulletin):
        global workPass
        if 'Entrants' in bulletin:
            bulletin = bulletin.replace('Entrants', 'Arstotzka, Antegria, Impor, Kolechia, Obristan, Republia, United Federation')
        if 'Foreigners' in bulletin:
            bulletin = bulletin.replace('Foreigners', 'Antegria, Impor, Kolechia, Obristan, Republia, United Federation')
        Instructions = bulletin.split("\n")
        for element in Instructions:
            if 'Wanted' not in element:
                for c in citizen.all:
                    if c.Nationality in element:
                        if 'Allow' in element:
                            c.isAllowed = True
                        elif 'Deny' in element:
                            c.isAllowed = False
                        if 'access permit' in element:
                            c.rAccessPermit = True
                        if 'no longer' in element:
                            c.rVaccines.pop(c.rVaccines.index(element[element.index('require')+ len('require')+1:element.index('vaccination')-1]))
                        elif 'vaccination' in element:
                            c.rVaccines.append(element[element.index('require')+ len('require')+1: element.index('vaccination')-1])
                        if 'ID card' in element:
                            c.rID = True
            else: wanted.append(element[element.index(":")+2:])
            if 'work pass' in element:
                workPass = True
            
       
    def inspect(a,person):
        print(person)
        global workPass
        a = ""
        if 'passport' not in person:
            return 'Entry denied: missing required passport.'
        thisPassport = passport(*split(person["passport"]))
        for c in citizen.all:
            if thisPassport.NATION == c.Nationality:
                thisCitizen = c
        #Passport Check--------------------------------------
        temp = thisPassport.NAME.split(", ")
        temp[0], temp[1] = temp[1], temp[0]
        temp = " ".join(temp)
        if temp in wanted:
            return 'Detainment: Entrant is a wanted criminal.'
    
        if convertDate(thisPassport.EXP) < date:
            a = 'Entry denied: passport expired.'
        if not thisCitizen.isAllowed:
            a = 'Entry denied: citizen of banned nation.'
        #Check permit----------------------------------------
        if thisCitizen.rAccessPermit:
            if 'access_permit' in person:
                
                thisPermit = permit(*split(person['access_permit']))
                print(thisPermit.ID, thisPassport.ID)
                if thisPermit.NAME != thisPassport.NAME:
                    return 'Detainment: name mismatch.'
                if thisPermit.NATION != thisPassport.NATION:
                    return 'Detainment: nationality mismatch.'
                if thisPermit.ID != thisPassport.ID:
                    print("hey")
                    return 'Detainment: ID number mismatch.'
                if convertDate(thisPermit.EXP) < date:
                    a = 'Entry denied: access permit expired.'
            elif 'grant_of_asylum' in person:
                thisGrant = asylum(*split(person['grant_of_asylum']))
                if thisGrant.NAME != thisPassport.NAME:
                    return 'Detainment: name mismatch.'
                if thisGrant.NATION != thisPassport.NATION:
                    return 'Detainment: nationality mismatch.'
                if thisGrant.ID != thisPassport.ID:
                    return 'Detainment: ID number mismatch.'
                if convertDate(thisGrant.EXP) < date:
                    a= 'Entry denied: grant of asylum expired.'
            elif 'diplomatic_authorization' in person:
                thisDA = da(*split(person['diplomatic_authorization']))
                if thisDA.NAME != thisPassport.NAME:
                    return 'Detainment: name mismatch.'
                if thisDA.NATION != thisPassport.NATION:
                    return 'Detainment: nationality mismatch.'
                if thisDA.ID != thisPassport.ID:
                    return 'Detainment: ID number mismatch.'
                if 'Arstotzka' not in thisDA.ACCESS:
                    a= 'Entry denied: invalid diplomatic authorization.'
            else: a = 'Entry denied: missing required access permit.'
       
        #Check ID card---------------------------------------
        if thisCitizen.rID:
            if 'ID_card' not in person:
                a= 'Entry denied: missing required ID card.'
            else: 
                thisID = IDC(*split(person["ID_card"]))
                if thisID.NAME != thisPassport.NAME:
                    return 'Detainment: name mismatch.'
                if thisID.DOB != thisPassport.DOB:
                    return 'Detainment: date of birth mismatch.'
        #Check Work Pass-------------------------------------
        if workPass and 'thisPermit' in locals():
            if thisPermit.PURPOSE == 'WORK' and 'work_pass' not in person:
                a = 'Entry denied: missing required work pass.'
            elif thisPermit.PURPOSE == 'WORK': 
                thisWP = wp(*split(person["work_pass"]))
                if thisWP.NAME != thisPassport.NAME:
                    return 'Detainment: name mismatch.'
                if convertDate(thisWP.EXP) < date:
                    a ='Entry denied: work pass expired.'
        
        #Check Vaccination-----------------------------------
        if thisCitizen.rVaccines != []:
            if 'certificate_of_vaccination' not in person:
                a = 'Entry denied: missing required certificate of vaccination.'
            else:
                thisCer = vaccine(*split(person['certificate_of_vaccination']))
                for x in thisCitizen.rVaccines:
                    if x not in thisCer.VACCINES:
                        a = 'Entry denied: missing required vaccination.'
                    else: break
                if thisCer.ID != thisPassport.ID:
                    return 'Detainment: ID number mismatch.'
                if thisCer.NAME != thisPassport.NAME:
                    return 'Detainment: name mismatch.'
        if a !="":
            return a
        return 'Glory to Arstotzka.' * (thisPassport.NATION == 'Arstotzka') +'Cause no trouble.' * (thisPassport.NATION != 'Arstotzka')
