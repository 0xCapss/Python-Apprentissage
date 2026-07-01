---
tags: [algorithmie, complexite, performance]
statut: termine
---
# Complexite O(n) — Pourquoi un code est lent

## L'idee de base

La complexite mesure comment le **temps d'execution grandit** quand la taille des donnees grandit.
On note ca O(...) — on dit "ordre de".

Le `n` = la taille des donnees (nombre d'elements dans une liste, par exemple).

## Les trois niveaux essentiels

| Complexite | Nom | Ce que ca veut dire |
|------------|-----|---------------------|
| O(log n) | logarithmique | On coupe le probleme en deux a chaque etape |
| O(n) | lineaire | On fait un passage sur chaque element |
| O(n²) | quadratique | Pour chaque element, on reparcourt tous les elements |

## Exemples concrets

**O(log n)** — recherche dans une liste triee (on coupe en deux a chaque fois) :
- 1 000 elements → ~10 comparaisons
- 1 000 000 elements → ~20 comparaisons

**O(n)** — parcourir une liste :
```python
for element in liste:
    ...
```
La liste double → le travail double.

**O(n²)** — double boucle imbriquee :
```python
for i in liste:
    for j in liste:   # boucle dans la boucle
        ...
```
La liste double → le travail est multiplie par 4.

## Piege classique : deux boucles separees vs imbriquees

```python
# O(n) — deux boucles separees
for element in liste:
    ...
for element in liste:
    ...
# Total : 2n operations = O(n)

# O(n²) — boucle dans une boucle
for i in liste:
    for j in liste:
        ...
# Total : n*n operations = O(n²)
```

Les constantes disparaissent en complexite : O(2n) = O(n).

## Exemples dans nos exercices

- E06 Compter les occurrences : une boucle → O(n)
- E08 Element le plus frequent : deux boucles separees → O(n) + O(n) = O(n)
- Double boucle naive pour comparer chaque element a tous les autres → O(n²)

Retour : [[02-Algorithmie/Algorithmie - Index|Algorithmie - Index]]
