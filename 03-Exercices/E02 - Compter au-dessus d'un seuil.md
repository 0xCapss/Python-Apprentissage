---
tags: [exercice, algorithmie, liste, boucle, condition]
statut: termine
---
# E02 - Compter les elements au-dessus d'un seuil

## Enonce
On te donne une liste de nombres et un nombre seuil.
Tu dois renvoyer combien d'elements de la liste sont strictement superieurs au seuil.
Exemple : liste = [3, 7, 2, 9, 4], seuil = 4  ->  reponse : 2 (ce sont 7 et 9).

## Mon raisonnement (methode REGT)

R - Reformuler
- Entrees : une liste de nombres ET un nombre seuil (deux parametres).
- Sortie : un nombre entier, le nombre d'elements strictement superieurs au seuil.

E - Exemple a la main
Je parcours la liste, et je tiens un compteur. A chaque nombre, s'il depasse le seuil,
j'ajoute 1 au compteur. A la fin, le compteur est la reponse.

G - Generaliser (pseudo-code)
```
compteur = 0
pour chaque nombre de la liste :
    si nombre > seuil :
        compteur = compteur + 1
renvoyer compteur
```

T - Traduire (Python)
```python
def plus_grand_que_seuil(liste, seuil):
    compteur = 0
    for nombre in liste:
        if nombre > seuil:
            compteur += 1
    return compteur
```
Code complet et testable : voir E02_compter_seuil.py.

## Lecons importantes
- Le cas vide n'a pas toujours la meme bonne reponse :
  pour un maximum, le vide n'a pas de reponse (None) ;
  pour un comptage, le vide a une vraie reponse (0). On ne recopie pas une garde par habitude.
- compteur = 0 doit s'executer A TOUS LES COUPS, avant la boucle.
  Le cacher dans un if provoque une UnboundLocalError sur les listes non vides.
- compteur += 1 = ecriture courte de compteur = compteur + 1.
- Une fois compteur initialise a 0, la liste vide est geree gratuitement (la boucle ne tourne pas).

## Verification
- [x] [3, 7, 2, 9, 4], seuil 4 -> 2
- [x] [1, 1, 1], seuil 5 -> 0
- [x] [], seuil 0 -> 0

Retour : [[03-Exercices/Exercices - Index|Exercices - Index]]
