"""
E01 - Le plus grand d'une liste
Solution construite avec la methode REGT (session 01).

Une fonction propre a une seule mission : calculer et renvoyer.
L'affichage est laisse au programme qui appelle la fonction.
"""


def plus_grand(liste):
    if len(liste) == 0:       # garde : on intercepte la liste vide avant liste[0]
        return None
    memoire = liste[0]        # variable d'etat : le plus grand vu jusqu'ici
    for nombre in liste:      # on parcourt chaque element
        if nombre > memoire:  # si on trouve mieux...
            memoire = nombre  # ...on met a jour la memoire
    return memoire


# Verifications (l'affichage, c'est le role du programme appelant, pas de la fonction)
print(plus_grand([3, 7, 9, 2, 4]))   # attendu : 9
print(plus_grand([5]))               # attendu : 5
print(plus_grand([-5, -2, -9]))      # attendu : -2 (le piege du depart a 0)
print(plus_grand([]))                # attendu : None (liste vide geree)

# Exemple d'utilisation cote appelant : c'est ici qu'on affiche
resultat = plus_grand([3, 7, 9, 2, 4])
if resultat is None:
    print("La liste est vide, pas de maximum.")
else:
    print(f"Le plus grand nombre est {resultat}")
