"""
E06 - Compter les occurrences

Patron de l'accumulateur, version DICTIONNAIRE : on construit un dico {cle: compte}.

Points cles :
- L'accumulateur est un dictionnaire vide {} au depart.
- Piege de la "premiere fois" : compteur[mot] += 1 plante (KeyError) si le tiroir
  n'existe pas encore, car += doit d'abord LIRE la valeur actuelle.
- Solution claire : tester `if mot in compteur` (existe deja) sinon le creer a 1.
- compteur[mot] vise UN tiroir ; compteur tout seul = le dictionnaire entier.
- Liste vide -> dictionnaire vide, gere gratuitement.
"""


def compter_occurrences(liste):
    compteur = {}
    for element in liste:
        if element in compteur:      # le tiroir existe deja
            compteur[element] += 1
        else:                        # premiere fois qu'on voit cet element
            compteur[element] = 1
    return compteur


# Variante pythonique equivalente, avec .get (valeur par defaut 0 si absent) :
def compter_occurrences_get(liste):
    compteur = {}
    for element in liste:
        compteur[element] = compteur.get(element, 0) + 1
    return compteur


# Verifications
print(compter_occurrences(["chat", "chien", "chat", "oiseau", "chat", "chien"]))
# attendu : {'chat': 3, 'chien': 2, 'oiseau': 1}
print(compter_occurrences([]))        # attendu : {}
print(compter_occurrences(["a"]))     # attendu : {'a': 1}
print(compter_occurrences_get(["chat", "chien", "chat"]))  # {'chat': 2, 'chien': 1}
