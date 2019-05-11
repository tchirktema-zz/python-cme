import os
import time
exit = ''
while exit !='q' :
    
    os.system('clear') 
    menu = ("Attieke + poission ","Alloco + poulet","Placali + kplo")
    print('---------------------')
    print('| Restaurant lagune |')
    print('---------------------')
    print('Menu : ')
    print(" 1 -"+menu[0])
    print(" 2 -"+menu[1])
    print(" 3 -"+menu[2])
    print("Appuier sur q pour quitter ")

    #choix du menu
    choix = input('Faite votre choix[1 a 3] : ')
    if choix == 'q':
        break
    else:
        choix = int(choix)

    if choix == 1:
        print("Menu "+menu[0]+ " Prix : 1000 FCFA/plat")
        nombre_de_plat = input("Combien de plat voulez-vous ? : ")
        nombre_de_plat = int(nombre_de_plat)
        prix_total = nombre_de_plat * 1000

        print("Votre facture est  : "+ str(prix_total))

    elif choix == 2:
        print("Menu "+menu[1]+ " Prix : 2000 FCFA/plat")
        nombre_de_plat = input("Combien de plat voulez-vous ? : ")
        nombre_de_plat = int(nombre_de_plat)
        prix_total = nombre_de_plat * 2000

        print("Votre facture est  : "+ str(prix_total))

    elif choix == 3:
        print("Menu "+menu[2]+ " Prix : 3000 FCFA/plat")
        nombre_de_plat = input("Combien de plat voulez-vous ? : ")
        nombre_de_plat = int(nombre_de_plat)
        prix_total = nombre_de_plat * 3000

        print("Votre facture est  : "+ str(prix_total))
        
    else:
        print('Choix invalid ....!!!')

    print("Le restaurant lagune vous souhaite un bon appetit")
    time.sleep(5)