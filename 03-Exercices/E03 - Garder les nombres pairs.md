---
tags: [exercice, algorithmie, liste, boucle, condition, accumulateur]
statut: termine
---
# E03 - Garder seulement les nombres pairs

## Enonce
On te donne une liste de nombres. Tu dois renvoyer une NOUVELLE liste
contenant seulement les nombres pairs, dans le meme ordre.
Exemple : [3, 7, 2, 9, 4, 6]  ->  [2, 4, 6].

## Mon raisonnement (methode REGT)

R - Reformuler
- Entree : une liste de nombres.
- Sortie : une NOUVELLE liste (pas un nombre), avec seulement les pairs, dans l'ordre.

E - Exemple a la main
Je tiens une liste-memoire vide a cote. Je parcours l'entree ; chaque fois qu'un
nombre est pair, je l'ajoute a ma liste-memoire. A la fin, je rends cette liste.

G - Generaliser (pseudo-code)
```
resultat = liste vide
pour chaque nombre de la liste :
    si nombre est pair :
        ajouter nombre a resultat
renvoyer resultat
```

T - Traduire (Python)
```python
def nombres_pairs(liste):
    resultat = []
    for nombre in liste:
        if nombre % 2 == 0:
            resultat.append(nombre)
    return resultat
```
Code complet et testable : voir E03_nombres_pairs.py.

## Lecons importantes
- Nouveau patron : l'accumulateur est une LISTE. On part de [] et on remplit avec .append().
- Piege majeur : dans `for nombre in liste`, `nombre` est la VALEUR, pas la position.
  Ecrire `liste[nombre]` cherche un element a la position `nombre` -> IndexError.
  On teste donc directement `nombre % 2 == 0`.
- `nombre % 2` = reste de la division par 2 ; reste 0 => pair.
- Les cas vide et "aucun pair" donnent [] gratuitement (on part de [], on n'ajoute rien).
- L'indentation (4 espaces, coherente) definit la structure en Python.

## Verification
- [x] [3, 7, 2, 9, 4, 6] -> [2, 4, 6]
- [x] [1, 3, 5] -> []
- [x] [] -> []

Retour : [[03-Exercices/Exercices - Index|Exercices - Index]]
