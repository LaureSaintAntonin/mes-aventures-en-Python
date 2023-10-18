# importe le module hashlib pour la construction de l'algorithme de hachage et la clé de hashage
from hashlib import sha256 
# nommer la clé (créer une instance de la classe)
h = sha256()
# utilisation de la update() method pour mettre à jour la clé
# c'est là qu'on inserre le mot de passe que l'on veut asher
h.update(b'motdepassebidon44')
# méthode pour hasher en hexadecimal
hash= h.hexdigest()
# apparition du code ashé dans la console.
print(hash)