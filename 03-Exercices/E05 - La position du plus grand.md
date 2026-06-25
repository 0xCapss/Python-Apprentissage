---
tags: [exercice, algorithmie, liste, indice, enumerate]
statut: termine
---
# E05 - La position du plus grand

## Enonce
On te donne une liste de nombres. Tu dois renvoyer la POSITION (l'indice)
du plus grand element, pas sa valeur.
Exemple : [3, 7, 2, 9, 4]  ->  3  (le plus grand, 9, est a la position 3).
Les positions commencent a 0.

## Nouvel outil : enumerate
`for position, nombre in enumerate(liste)` donne a chaque tour la position ET la valeur.
Sur [3, 7, 2, 9, 4] : (0,3), (1,7), (2,2), (3,9), (4,4).
Indispensable quand l'algorithme a besoin de savoir OU il se trouve, pas juste quoi.

## Mon raisonnement (methode REGT)

R - Reformuler
- Entree : une liste de nombres.
- Sortie : un entier, la position du plus grand element.

E - Exemple a la main
Je parcours en gardant deux choses : la plus grande valeur vue, et sa position.
Quand je trouve mieux, je mets a jour les deux. A la fin, je renvoie la position.

G - Generaliser (pseudo-code)
```
meilleur_position = 0
meilleur_valeur = premier element
pour (position, nombre) dans la liste numerotee :
    si nombre > meilleur_valeur :
        meilleur_valeur = nombre
        meilleur_position = position
renvoyer meilleur_position
```

T - Traduire (Python)
```python
def position_du_plus_grand(liste):
    meilleur_position = 0
    meilleur_valeur = liste[0]
    for position, nombre in enumerate(liste):
        if nombre > meilleur_valeur:
            meilleur_valeur = nombre
            meilleur_position = position
    return meilleur_position
```
Code complet et testable : voir E05_position_max.py.

## Lecons importantes
- enumerate donne (position, valeur) a chaque tour : la solution en UN seul passage.
- On suit deux memoires : la valeur (pour comparer) et la position (la reponse).
- Meme piege qu'en E01 : initialiser meilleur_valeur avec liste[0], pas 0
  (sinon liste toute negative -> mauvaise position).
- Reflexe pro de reutilisation : on a d'abord pense a reutiliser plus_grand (E01),
  mais elle rend la valeur, pas la position -> il fallait l'approche directe.
- Comparaison > stricte : en cas d'egalite, on garde la PREMIERE position
  (avec >= on garderait la derniere). L'operateur decide du comportement.

## Verification
- [x] [3, 7, 2, 9, 4] -> 3
- [x] [-5, -2, -9] -> 1
- [x] [10] -> 0
- [x] [5, 5, 1] -> 0 (egalite : premier)

Retour : [[03-Exercices/Exercices - Index|Exercices - Index]]
