#CE programme permet d'afficher les information d'un personne
print("Welcome")
#Saisi du nom
print("Entrer votre nom :")
nom = input()
#saisi de l'age
print("Entrer votre age :")
age = input()
#saisi du sexe
print("Entrer votre sexe :")
sexe = input()


if sexe == "masculin":
    print("Bonjour  monsieur "+nom+" votre age est "+age+" et votre sexe est "+ sexe)
elif sexe == "feminin":
    print("Bonjour madame "+nom+" votre age est "+age+" et votre sexe est "+ sexe)
else :
    print("je ne connais pas votre sexe")
