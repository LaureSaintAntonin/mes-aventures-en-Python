import random

femme = ["une scientifique", "une reine", "une policière", "une informaticienne", "une pirate"]
homme = ["un danseur", "un cuisinier", "un robot", "Ripley", "le pere Noel"]
lieu = ["a Vallet", "a l'école", "au bord de la mer", "sur la lune", "dans un sous-marin"]
ellePortait = ["une blouse verte fluo", "un bandeau sur son oeil","des habits troues", "une couronne en papier", "un truc etrange sur son epaule"]
ilPortait = ["un tutu", "un maillot de bain", "des chaussures trop petites pour lui", "un deguissement de sorcier", "un parapluie troue"]
femmeDit = ["Qui es-tu ?", "Ca va etre tout noir !", "j'ai faim", "je pense que nous devrions y aller", "Youpidou !"]
hommeDit = ["abracadabra", "je ne vois rien du tout", "as tu pris ton ticket de metro ?", "pourquoi fais tu ça ?", "j'ai faim !"]
conséquence = ["il fait tout noir", "la planete est sauvee", "l'ordinateur est casse", "des arcs en ciels apparaissent !", "on passe a table"]
mondeDit = ["Mais quel bazard !", "c'est dingue !", "ho non, il est elimine", "Le chat dort, la caravane passe", "et ils vecurent heureux. Ou pas !"]

while True:
    print(random.choice(femme), "a rencontre", random.choice(homme), random.choice(lieu))
    print("Elle portait", random.choice(ellePortait))
    print("Il portait", random.choice(ilPortait))
    print("Elle a dit", random.choice(femmeDit))
    print("Il a dit", random.choice(hommeDit))
    print("La consequence a ete", random.choice(conséquence))
    print("Le monde a dit", random.choice(mondeDit))
    print()
    input("Appuie sur Entree pour rejouer.")
    print()