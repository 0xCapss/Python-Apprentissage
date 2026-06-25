---
tags: [exercice, algorithmie, liste, accumulateur, moyenne]
statut: termine
---
# E04 - La moyenne d'une liste

## Enonce
On te donne une liste de nombres. Tu dois renvoyer leur moyenne.
Exemple : [4, 8, 6]  ->  6.0  (car (4 + 8 + 6) / 3 = 18 / 3 = 6).

## Mon raisonnement (methode REGT)

R - Reformuler
- Entree : une liste de nombres.
- Sortie : un nombre (la moyenne), ou None si la liste est vide.

E - Exemple a la main
La moyenne = (somme des elements) / (nombre d'elements). Donc je dois suivre
DEUX choses en parcourant : une somme et un compteur. A la fin, je divise.

G - Generaliser (pseudo-code)
```
si la liste est vide : renvoyer None
somme = 0
nb = 0
pour chaque nombre de la liste :
    somme = somme + nombre
    nb = nb + 1
renvoyer somme / nb
```

T - Traduire (Python)
```python
def calcul_moyenne(liste):
    if len(liste) == 0:
        return None
    somme = 0
    nb = 0
    for nombre in liste:
        somme += nombre
        nb += 1
    return somme / nb
```
Code complet et testable : voir E04_moyenne.py.

## Lecons importantes (beaucoup d'erreurs classiques traversees)
- DEUX accumulateurs peuvent tourner en parallele dans la meme boucle.
- Initialiser somme/nb UNE fois AVANT la boucle :
  - dans la boucle -> remise a zero chaque tour -> resultat faux (renvoie le dernier element).
  - pas du tout -> UnboundLocalError sur somme.
- Le calcul final (division) se fait APRES la boucle, une seule fois (pas dedans).
- Liste vide -> nb = 0 -> ZeroDivisionError. La moyenne du vide n'existe pas : garde + None (comme E01).
- 'liste' (ma variable) n'est pas 'list' (le type Python) : len(list) -> TypeError.
- Dans la vraie vie, on ecrit sum(liste) / len(liste) ; ici on l'a fait a la main pour le mecanisme.

## Verification
- [x] [2, 4, 9] -> 5.0
- [x] [4, 8, 6] -> 6.0
- [x] [10] -> 10.0
- [x] [] -> None

Retour : [[03-Exercices/Exercices - Index|Exercices - Index]]
