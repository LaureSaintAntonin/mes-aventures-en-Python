aliens = 2
motDePasse = "ALIENS"

print("VITE ! Des aliens envahissent la planète")
print("Tu dois activer la plateforme de défense mondiale !")
print("Jespère que tu connais le mot de passe...")
print()
print("------------------------------------------------------")
print("     BIENVENUE DANS LE RESEAU DE DEFENSE MONDIALE     ")
print("------------------------------------------------------")
deviner = input("Entrer le mot de passe : ").upper()
while deviner != motDePasse:
    print()
    print("MOT DE PASSE INCORRECT")
    print()
    aliens = aliens ** 2
    print ("Il y a", aliens, "aliens sur Terre. Réessaie !")
    if aliens > 7400000000:
        break
    print()
    print("Indice mot de passe : les créatures qui nous attaquent.")
    print()
    deviner = input("Vite Vite ! Entre le mot de passe : ").upper()
    print()
    print("deuxième indice mot de passe : ils sont nombreux !")
    print()
    deviner = input("Vite ! Entre le mot de passe : ").upper()
    
if aliens > 7400000000:
    print("NOOOOON ! Les aliens sont plus nombreux que nous !!! TOUT est perdu !!!")
else:
    print("HOURRA !!! Nous avons gagné le combat ! La Terre et l'Humanité sont sauvées !")
        
