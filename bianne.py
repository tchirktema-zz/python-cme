#ce programme permet de voir si une annee est bisexitile

annee = input("Entrer l'annee : ")

#conversion de l'annee en entier
annee = int(annee)

if annee%400 == 0:
    print(str(annee)+ " est bisexitile")
elif annee%4 == 0:
    if annee%100 != 0:
        print(  str(annee)+ " est bisexitile")
    else :
        print( str(annee)+ " n'est bisexitile")

else:
    print( str(annee)+ " n' est bisexitile")
