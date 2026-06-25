---
tags: [python, fondation, variables, types, memoire]
---
# Variables et types

## Une variable : un nom, pas une boite

En Python, une variable est une **etiquette** qui pointe vers un objet en memoire.
Ce n'est pas une boite qui contient une valeur — c'est une fleche vers un objet.

```python
x = 42        # Python cree l'objet 42 en memoire, x pointe dessus
x = "bonjour" # Python cree un nouvel objet, x pointe maintenant dessus
              # l'objet 42 est abandonne
```

`id(x)` retourne l'adresse memoire de l'objet pointe par x.

## Le typage dynamique

En Python, le type appartient a la valeur, pas au nom.
On ne declare pas le type : Python le deduit tout seul.

```python
x = 42        # x pointe vers un int
x = "bonjour" # x pointe maintenant vers un str — meme nom, type different
```

## Les 6 types fondamentaux

| Type | Exemple | Mutable |
|------|---------|---------|
| `int` | `42` | Non |
| `float` | `3.14` | Non |
| `str` | `"bonjour"` | Non |
| `bool` | `True / False` | Non |
| `list` | `[1, 2, 3]` | Oui |
| `dict` | `{"cle": val}` | Oui |

## Mutable vs immutable

**Mutable** : l'objet peut etre modifie en place (meme adresse memoire, contenu change).
**Immutable** : toute "modification" cree un nouvel objet (nouvelle adresse).

```python
# str est immutable
s = "bonjour"
s2 = s
s += " monde"  # nouvel objet cree, s pointe dessus
print(s2)      # "bonjour" — l'ancien objet n'a pas change

# list est mutable
a = [1, 2, 3]
b = a          # b et a pointent vers le MEME objet
b.append(4)
print(a)       # [1, 2, 3, 4] — a "voit" le changement
```

## Le piege de la reference partagee

Quand tu ecris `b = a` avec une liste, tu n'as pas deux listes — tu as deux etiquettes
sur la meme liste. Modifier l'une modifie l'autre.

```
a ──┐
    ──► [1, 2, 3]
b ──┘
```

**Solution** : faire une copie explicite.
```python
b = a.copy()  # nouvel objet independant
```

## Pourquoi ca compte

Ce modele explique des bugs courants :
- Passer une liste a une fonction et la voir modifiee de l'exterieur.
- Croire avoir copie une liste alors qu'on a juste copie la reference.

Retour : [[01-Python/Python - Index|Python - Index]]
