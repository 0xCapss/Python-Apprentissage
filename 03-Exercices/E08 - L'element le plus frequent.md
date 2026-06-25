---
tags: [exercice, synthese, dictionnaire, accumulateur, cyber]
statut: termine
---
# E08 (synthese) - L'element le plus frequent

## Contexte
Exercice de SYNTHESE : aucune notion nouvelle, on combine deux exercices connus.
- compter les occurrences avec un dictionnaire (E06)
- trouver un maximum avec un accumulateur (E01 / E05)

Cas reel en cyber : trouver l'IP qui revient le plus dans une liste de logs
(scan, force brute...).

## Enonce
On te donne une liste d'elements. Tu renvoies celui qui apparait le PLUS souvent.
Exemples :
- ["10.0.0.1","10.0.0.2","10.0.0.1","10.0.0.1","10.0.0.2"] -> "10.0.0.1" (3 fois)
- ["a","b","b","c"] -> "b"
- [] -> None

## Mon raisonnement (REGT)
R - Reformuler
- Entree : une liste d'elements.
- Sortie : l'element le plus frequent (une cle), ou None si la liste est vide.

G - Generaliser : le decoupage en DEUX etapes deja connues
1. Construire compteur = {element: nombre d'occurrences}   (E06)
2. Parcourir compteur.items() pour trouver la cle au plus grand compte   (E05)

T - Traduire (Python)
```python
def element_le_plus_frequent(liste):
    compteur = {}
    for element in liste:
        compteur[element] = compteur.get(element, 0) + 1
    meilleur_element = None
    occurence_max = 0
    for element, compte in compteur.items():
        if compte > occurence_max:
            occurence_max = compte
            meilleur_element = element
    return meilleur_element
```
Code complet : voir E08_plus_frequent.py.

## Lecons importantes
- Synthese = decouper en sous-problemes deja maitrises (l'etape G de REGT).
- L'etape 2 parcourt le DICTIONNAIRE (compteur.items()), pas la liste de depart.
- compteur.items() : ne pas oublier les parentheses (on APPELLE la methode).
- On renvoie la CLE gagnante (meilleur_element), pas la derniere cle vue, pas le compte.
- return APRES la boucle (sinon on sort au premier tour).
- Init a 0 est correct ici (un compte vaut toujours >= 1), contraste avec le piege de E01.
- Liste vide -> {} -> meilleur_element reste None. Gere gratuitement.
- Difficulte du jour travaillee : passer de la logique comprise a l'ecriture Python (etape T).

## Verification
- [x] ["10.0.0.1","10.0.0.2","10.0.0.1","10.0.0.1","10.0.0.2"] -> "10.0.0.1"
- [x] ["a","b","b","c"] -> "b"
- [x] [] -> None

Retour : [[03-Exercices/Exercices - Index|Exercices - Index]]
