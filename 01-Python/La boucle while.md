---
tags: [python, boucle, while]
---
# La boucle while

## Idee
Repeter un bloc TANT QU'une condition est vraie. A utiliser quand on ne connait
PAS d'avance le nombre de tours (contrairement au for sur une liste).

```python
while condition:
    # corps, repete tant que condition est vraie
```
Python verifie la condition AVANT chaque tour. Des qu'elle devient fausse, on sort.

## La regle d'or : eviter la boucle infinie
Avec un for sur une liste, la fin est garantie (liste finie).
Avec un while, C'EST TOI le responsable : quelque chose dans le corps doit faire
evoluer la condition vers "faux" a chaque tour, sinon le programme tourne sans fin.

```python
n = 3
while n > 0:
    print(n)
    n = n - 1     # <-- sans cette ligne, n reste 3 : boucle infinie
```

## Piege : la boucle modifie ses variables
Si la condition (ou le corps) change une variable, sa valeur d'origine est perdue
apres la boucle. Pour tester la valeur d'ENTREE, on le fait AVANT la boucle.
Exemple vu dans [[03-Exercices/E07 - Compter les chiffres|E07]] : la garde sur le
cas 0 doit etre tout en haut, car la boucle ramene 'nombre' a 0 a la fin de tous les cas.

## for ou while ?
- Nombre de tours connu / parcourir une collection -> for.
- Repeter jusqu'a ce qu'une condition change (entree utilisateur, calcul iteratif) -> while.

Retour : [[01-Python/Python - Index|Python - Index]]
