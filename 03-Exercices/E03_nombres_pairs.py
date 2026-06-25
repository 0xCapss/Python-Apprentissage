"""
E03 - Garder seulement les nombres pairs

Nouveau patron : l'accumulateur est une LISTE (et non un nombre).
On part d'une liste vide et on la remplit avec .append() pendant le parcours.

Points cles :
- for nombre in liste : 'nombre' est la VALEUR de l'element, pas sa position.
  Donc on teste 'nombre % 2 == 0', surtout pas 'liste[nombre]' (-> IndexError).
- nombre % 2 donne le reste de la division par 2 ; reste 0 => nombre pair.
- liste vide et 'aucun pair' renvoient [] gratuitement : on part de [] et on n'ajoute rien.
- L'indentation (4 espaces) definit la structure du code en Python.
"""


def nombres_pairs(liste):
    resultat = []                  # accumulateur : une liste, vide au depart
    for nombre in liste:           # nombre = la valeur de l'element
        if nombre % 2 == 0:        # pair si le reste de la division par 2 est 0
            resultat.append(nombre)  # on ajoute a la fin de la liste resultat
    return resultat


# Verifications
print(nombres_pairs([3, 7, 2, 9, 4, 6]))  # attendu : [2, 4, 6]
print(nombres_pairs([1, 3, 5]))           # attendu : []
print(nombres_pairs([]))                  # attendu : []
