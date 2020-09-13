nombre = int(input("Put the number you wanna verify here:"));

racine = round(pow(nombre, 1/2));
calcul =True;

i = 2;

while i < nombre and calcul == True:
    division = nombre % i;
    if (division == 0):
        calcul = False
        print("The number that can divide this is" +    "" + str(i))
        exit
    else:
        i += 1;

if i >= nombre:
    print("It's a prime number'")

#Ca réussit, par exemple 386693 peut etre trouvé premier en moins de 3 secondes!

#25 688 651 est premier, il prend 44 seconde pour trouver ça!