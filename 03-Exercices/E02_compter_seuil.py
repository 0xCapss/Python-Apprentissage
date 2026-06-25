"""
E02 - Compter les elements au-dessus d'un seuil
Meme schema que E01 : une variable d'etat (un compteur) + une boucle + une condition.

Lecons de cet exercice :
- Le cas vide n'a pas la meme bonne reponse selon le probleme :
  pour un maximum -> None (pas de reponse) ; pour un comptage -> 0 (reponse valide).
- L'initialisation (compteur = 0) doit s'executer A TOUS LES COUPS, avant la boucle.
  Si on la cache dans un if, on risque une UnboundLocalError.
- compteur += 1 est l'ecriture courte de compteur = compteur + 1.
"""


def plus_grand_que_seuil(liste, seuil):
    compteur = 0
    for nombre in liste:
        if nombre > seuil:
            compteur += 1
    return compteur


# Verifications
print(plus_grand_que_seuil([3, 7, 2, 9, 4], 4))  # attendu : 2 (7 et 9)
print(plus_grand_que_seuil([1, 1, 1], 5))        # attendu : 0
print(plus_grand_que_seuil([], 0))               # attendu : 0 (liste vide = 0 element)
