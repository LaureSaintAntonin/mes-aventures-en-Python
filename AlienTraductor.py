dictionnaireAlien = {"nous": "vorag", "venons": "zangue", "en": "zont", "paix": "argh", 
                    "bonjour": "kodar", "puis-je": "znak-as", "emprunter": "liftit",
                    "un peu": "tzoum", "de": "kirk", "carburant": "kakboumboum", "pour": "griiz",
                    "fusee": "hopsôtt", "s'il vous plait": "selpinne", "ne": "reg", "tirez": "flabil",
                    "pas": "baaaaaaaarn", "bienvenu": "unkip","a": "daragaz", "nos": "mandig",
                    "nouveau": "brang", "seigneurs": "baps", "extraterrestres": "marandjinz"}

phraseFrancais = input("Entre un mot ou une phrase en francais a traduire :")
motsFrancais = phraseFrancais.lower().split()

motsAlien = []
for mot in motsFrancais:
    if mot in dictionnaireAlien:
        motsAlien.append(dictionnaireAlien[mot])
    else:
        motsAlien.append(mot)
        
print("En Alien, on dit :", " ".join(motsAlien))