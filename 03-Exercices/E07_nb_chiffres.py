"""
E07 - Compter les chiffres d'un nombre (boucle while)

Premiere boucle while : le nombre de tours n'est pas connu d'avance.

Outils arithmetiques :
- n % 10  : dernier chiffre de n
- n // 10 : n sans son dernier chiffre (division entiere)

Points cles :
- while repete TANT QUE la condition est vraie ; quelque chose doit la faire
  evoluer vers "faux" a chaque tour, sinon boucle infinie.
- Ici nombre = nombre // 10 fait diminuer nombre vers 0 : c'est ce qui garantit la sortie.
- PIEGE MAJEUR : la boucle MODIFIE 'nombre'. A la sortie, nombre vaut toujours 0.
  Donc une garde sur la valeur d'ENTREE (le cas 0) doit etre testee TOUT EN HAUT,
  avant que la boucle ne change nombre. La tester apres -> toujours vraie -> bug.
"""


def nb_chiffres(nombre):
    if nombre == 0:          # garde sur l'entree, AVANT que la boucle ne modifie nombre
        return 1
    compteur_chiffre = 0
    while nombre != 0:
        nombre = nombre // 10   # on enleve le dernier chiffre : on se rapproche de 0
        compteur_chiffre += 1
    return compteur_chiffre


# Verifications
print(nb_chiffres(4087))  # attendu : 4
print(nb_chiffres(9))     # attendu : 1
print(nb_chiffres(100))   # attendu : 3
print(nb_chiffres(0))     # attendu : 1
