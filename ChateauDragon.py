print("Tu te trouves dans une pièce obscure d'un mystérieux chateau.")
print("Tu dois choisir entre 3 portes pour continuer l'aventure")
choixJoueur = input("choisit 1, 2, ou 3...")
if choixJoueur == "1":
        print("Tu as trouvé un trésor fabuleux ! Tu est riche !")
        print("BRAVO, TU AS GAGNE !")
elif choixJoueur == "2":
        print("La porte s'ouvre en grinçant, et un ogre affamé te donne un coup de massue BOING !")
        print("GAME OVER, TU AS PERDU !")
elif choixJoueur == "3":
        print("Il y a un dragon endormi dans cette pièce.")
        print("Le dragon se réveille et te mange d'une seule bouchée. Il te trouve délicieux.")
        print("GAME OVER, TU AS PERDU !")
else:
        print("désolé, tu n'as pas entré 1, 2 ou 3 !")
print("Lance à nouveau le jeu pour réessayer.")
