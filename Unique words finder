import string

text_brut = input("Bonjour, je suis le programme qui évalue la richesse de ton vocabulaire! Ecrit ton text ici:")
text = "".join(t for t in text_brut if t not in ("?", ".", ";", ":", "!", ",", "-")) #You can add here character you want to delete

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
   BOLD = '\033[1m'
   NORMAL = '\033[0m'

print(new_array)
longueur1 = len(new_array)
print("Total number of words:" + str(longueur))
print("The number of unique words is:" + color.BOLD + str(longueur1) + color.NORMAL)





