---
tags: [python, boucle, liste]
---
# enumerate

## A quoi ca sert
Parcourir une liste en ayant a la fois la POSITION (indice) et la VALEUR de chaque element.

## Syntaxe
```python
for position, valeur in enumerate(liste):
    ...
```
A chaque tour, enumerate fournit un couple (position, valeur).
Sur ["a", "b", "c"] : (0, "a"), (1, "b"), (2, "c").

## Quand l'utiliser
- Quand l'algo a besoin de savoir OU il se trouve, pas seulement quelle valeur.
- Exemples : trouver la position d'un element, comparer un element a son voisin, etc.

## Sans enumerate (a eviter)
On peut maintenir un compteur a la main, mais c'est plus lourd et source d'erreurs :
```python
position = 0
for valeur in liste:
    ...
    position += 1
```
enumerate fait ce travail proprement pour toi.

## Piege a connaitre
`for valeur in liste` donne la VALEUR, pas la position.
Ecrire `liste[valeur]` dans ce cas est une erreur frequente (IndexError). Voir [[03-Exercices/E03 - Garder les nombres pairs|E03]].

Vu en pratique dans [[03-Exercices/E05 - La position du plus grand|E05]].

Retour : [[01-Python/Python - Index|Python - Index]]
