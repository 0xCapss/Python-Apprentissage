"""
E04 - La moyenne d'une liste

Palier : DEUX accumulateurs en parallele (somme + nombre d'elements),
combines a la fin par une division.

Points cles (beaucoup d'erreurs classiques rencontrees et corrigees) :
- On accumule a la main (somme += nombre, nb += 1) plutot que sum()/len(),
  pour muscler le patron. (Dans la vraie vie : sum(liste) / len(liste).)
- Initialiser somme = 0 et nb = 0 UNE fois, AVANT la boucle.
  Dans la boucle -> remise a zero a chaque tour (resultat faux).
  Pas du tout -> UnboundLocalError.
- Le calcul final (la division) se fait APRES la boucle, une seule fois.
- Liste vide : nb = 0 -> division par zero (ZeroDivisionError).
  La moyenne du vide n'existe pas, donc on renvoie None (garde, comme E01).
- Attention aux noms : 'liste' (ma variable) n'est pas 'list' (le type Python).
"""


def calcul_moyenne(liste):
    if len(liste) == 0:        # garde : pas de moyenne pour une liste vide
        return None
    somme = 0                  # accumulateur 1 : la somme
    nb = 0                     # accumulateur 2 : le nombre d'elements
    for nombre in liste:
        somme += nombre
        nb += 1
    return somme / nb          # division finale, une seule fois, apres la boucle


# Verifications
print(calcul_moyenne([2, 4, 9]))  # attendu : 5.0
print(calcul_moyenne([4, 8, 6]))  # attendu : 6.0
print(calcul_moyenne([10]))       # attendu : 10.0
print(calcul_moyenne([]))         # attendu : None
