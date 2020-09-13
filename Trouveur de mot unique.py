import string

text_brut = input("Bonjour, je suis le programme qui juge la richesse de ton vocabulaire! Ecrit ton text ici:")
text = "".join(t for t in text_brut if t not in ("?", ".", ";", ":", "!", ",", "-"))

array = text.split();
i = 0;
longueur = len(array);


new_array = []
while i < longueur:
    # print("i is equal to" + str(i))

    if array[i] not in new_array:
        plus = [array[i]]
        new_array.extend(plus)

    i += 1

else:
    exit

class color:
   GRAS = '\033[1m'
   NORMAL = '\033[0m'

print(new_array)
longueur1 = len(new_array)
print("Le nombre total de mots est:" + str(longueur))
print("Le nombre de mots uniques reflétant la richesse de votre vocabulaire est:" + color.GRAS + str(longueur1) + color.NORMAL)





