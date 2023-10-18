print("Au départ, il y a un troupeau de 50 ponettes dans un petit pré qu'il faut transferer dans un grand pré.")
print(" Chacune à leur tour, les deux cavalières ramènent obligatoirement entre 1 et 6 ponettes dans le grand pré.")
print("Celle qui ramène la dernière ponette a gagné !!")


def saisie_ponettes():
	while True:
		ponettes_ramenees = int(input("Combien voulez-vous ramener de ponettes pour ce trajet (entre 1 et 6) ? "))
		if 1 <= ponettes_ramenees <= 6:
			return ponettes_ramenees
		else:
			print("Veuillez saisir un nombre entre 1 et 6.")


def jeu_ponettes():
	ponettes_restantes = 50

	while ponettes_restantes > 0:
		print("Cavalière 1 -")
		ponettes_ramenees = saisie_ponettes()

		if ponettes_ramenees <= ponettes_restantes:
			ponettes_restantes -= ponettes_ramenees
			print("Il reste", ponettes_restantes, "ponettes à transférer.")
		else:
			print("Vous ne pouvez pas ramener autant de ponettes. Il en reste", ponettes_restantes)

		if ponettes_restantes == 0:
			print("Félicitations ! Cavalière 1 a ramené toutes les ponettes.")
			break

		print("Cavalière 2 -")
		ponettes_ramenees = saisie_ponettes()

		if ponettes_ramenees <= ponettes_restantes:
			ponettes_restantes -= ponettes_ramenees
			print("Il reste", ponettes_restantes, "ponettes à transférer.")
		else:
			print("Vous ne pouvez pas ramener autant de ponettes. Il en reste", ponettes_restantes)

	print("Félicitations ! Cavalière 2 a ramené toutes les ponettes.")


jeu_ponettes()

# Proposer un mode multi-joueur. Demander à l’utilisateur, combien il y a de joueur et gérer la partie en conséquence.

# Libre à vous de faire une interface graphique à votre goût !
