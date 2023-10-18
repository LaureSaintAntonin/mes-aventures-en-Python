import random
choixSortie = "Rien"
while choixSortie != "QUITTER":
    
    print("Tu te trouves dans une pièce obscure d'un mystérieux chateau.")
    print("Tu dois choisir entre 4 portes pour continuer l'aventure")
    choixJoueur = input("choisit 1, 2, 3 ou 4...")
    if choixJoueur == "1":
        print("Tu as trouvé un trésor fabuleux ! Tu est riche !")
        print("BRAVO, TU AS GAGNE !")
    elif choixJoueur == "2":
        print("La porte s'ouvre en grinçant, et un ogre affamé te donne un coup de massue BOING !")
        print("GAME OVER, TU AS PERDU !")
    elif choixJoueur == "3":
        print("Il y a un dragon endormi dans cette pièce.")
        print("Tu peux soit:")
        print("1) Essayer de voler l'or du dragon, à tes risques et périls !")
        print("2) Essayer d'échapper au dragon ! La vie est précieuse...")
        choixDragon = input("Entre 1 ou 2.")
        if choixDragon == "1":
            print("Le dragon se réveille et te mange d'une seule bouchée. Il te trouve délicieux !")
            print("GAME OVER, TU AS PERDU !")
        elif choixDragon == "2":
            print("Tu échappes au dragon, tu sors du chateau et tu revois la lumière du jour !")
            print("BRAVO, TU AS GAGNE !")
        else:
            print("Désolé, tu n'as pas entré 1 ou 2")
    elif choixJoueur == "4":
        print("Tu entres dans une pièce où se trouve un Sphinx !")
        print("Il te demande de deviner à quel nombre il pense, entre 1 et 10.")
        nombre = int(input("Quel nombre choisis tu ?"))
        if nombre == random.randint(1,10):
            print("Déçu, le Sphinx émet un sifflement. Tu as deviné juste.")
            print("Il doit te laisser partir.")
            print("BRAVO, TU AS GAGNE !")
        else:
            print("Le Sphinx te dit que tu n'as pas deviné le bon chiffre.")
            print("Tu es désormais son prisonnier à jamais !")
            print("GAME OVER, TU AS PERDU !")
    else:
        print("désolé, tu n'as pas entré 1, 2, 3 ou 4 !")
    choixSortie = input("Appuie sur enter pour rejouer, ou tape QUITTER pour arréter.")
