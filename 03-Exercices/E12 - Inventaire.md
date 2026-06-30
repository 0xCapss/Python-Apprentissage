---
tags: [exercice, pratique, dictionnaire, tuple]
statut: termine
---
# E12 - Inventaire

## Enonce
Etant donne un inventaire sous forme de dictionnaire `{"pomme": 10, "banane": 5, "cerise": 42}`,
ecrire une fonction `produits_en_rupture(inventaire, seuil)` qui retourne un **tuple**
des noms de produits dont la quantite est strictement inferieure au seuil.

## Mon raisonnement (REGT)

**R** - Entree : un dictionnaire (produit → quantite) et un seuil numerique.
Sortie : un tuple des noms de produits en rupture (quantite < seuil).

**E** - `{"pomme": 10, "banane": 5, "cerise": 42}`, seuil = 10 :
- pomme : 10 < 10 ? Non (strictement inferieur, pas egal).
- banane : 5 < 10 ? Oui → dans le tuple.
- cerise : 42 < 10 ? Non.
- Resultat : `("banane",)`

**G** -
1. Creer une liste vide.
2. Parcourir le dictionnaire avec `.items()`.
3. Si quantite < seuil → ajouter le produit a la liste.
4. Retourner `tuple(liste)`.

**T** - Traduire (Python) : voir E12_inventaire.py

## Lecons importantes
- Un tuple est immuable : impossible d'y ajouter des elements au fur et a mesure.
  Astuce : accumuler dans une liste, puis convertir avec `tuple()`.
- `("valeur",)` != `("valeur")` : la virgule est ce qui fait le tuple, pas les parentheses.
- `.items()` retourne les paires (cle, valeur) pour les parcourir ensemble.

## Verification
- [x] `produits_en_rupture({"pomme": 10, "banane": 5, "cerise": 42}, 10)` → `('banane',)`
- [x] pomme exclue car 10 n'est pas strictement < 10

Notion liee : [[01-Python/Tuples et dictionnaires|Tuples et dictionnaires]]

Retour : [[03-Exercices/Exercices - Index|Exercices - Index]]
