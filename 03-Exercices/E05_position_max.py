"""
E05 - La position du plus grand

Nouveau besoin : connaitre la POSITION pendant le parcours, pas seulement la valeur.
Outil : enumerate, qui donne (position, valeur) a chaque tour.

Points cles :
- for position, nombre in enumerate(liste) : deux variables remplies a chaque tour.
- On suit DEUX memoires : la meilleure valeur (pour comparer) et sa position (la reponse).
- Meme piege qu'en E01 : initialiser meilleur_valeur avec liste[0], jamais 0
  (sinon une liste toute negative renvoie une mauvaise position).
- Comparaison stricte > : en cas d'egalite, on garde la PREMIERE position.
  Avec >=, on garderait la derniere. Le choix de l'operateur decide du comportement.
"""


def position_du_plus_grand(liste):
    meilleur_position = 0
    meilleur_valeur = liste[0]
    for position, nombre in enumerate(liste):
        if nombre > meilleur_valeur:
            meilleur_valeur = nombre
            meilleur_position = position
    return meilleur_position


# Verifications
print(position_du_plus_grand([3, 7, 2, 9, 4]))  # attendu : 3
print(position_du_plus_grand([-5, -2, -9]))     # attendu : 1 (max -2)
print(position_du_plus_grand([10]))             # attendu : 0
print(position_du_plus_grand([5, 5, 1]))        # attendu : 0 (egalite -> premier)
