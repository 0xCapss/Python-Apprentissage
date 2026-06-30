---
tags: [notion, python, tuple, dictionnaire]
---
# Tuples et dictionnaires

## Tuples

Un tuple est une sequence **immuable** : une fois cree, on ne peut ni modifier, ni ajouter, ni supprimer d'elements.

```python
coordonnees = (48.8566, 2.3522)
coordonnees[0] = 99.0  # TypeError : tuple ne supporte pas l'assignation
```

**Acces** : meme logique qu'une liste (indice depuis 0, boucle `for`).

**Cas d'usage** : donnees constantes par nature (coordonnees GPS, jours de la semaine, mois de l'annee, couleurs RGB).

**Piege** : `("valeur")` est une string, pas un tuple. La virgule fait le tuple :
```python
type(("banane"))   # str
type(("banane",))  # tuple
```

**Convertir une liste en tuple** :
```python
ma_liste = ["lundi", "mardi"]
mon_tuple = tuple(ma_liste)
```

---

## Dictionnaires

Un dictionnaire stocke des paires **cle : valeur**. Les cles sont uniques.

```python
inventaire = {"pomme": 10, "banane": 5}
```

| Operation | Syntaxe |
|-----------|---------|
| Lire | `inventaire["pomme"]` → `10` |
| Ajouter / modifier | `inventaire["cerise"] = 42` |
| Supprimer (et recuperer) | `inventaire.pop("banane")` → `5` |
| Parcourir cles + valeurs | `for k, v in inventaire.items()` |
| Parcourir cles seules | `for k in inventaire.keys()` |
| Parcourir valeurs seules | `for v in inventaire.values()` |

**Acces par indice impossible** — uniquement par cle.

---

## Comparaison des trois structures sequences

| Structure | Acces | Modifiable |
|-----------|-------|------------|
| Liste | indice numerique | oui |
| Tuple | indice numerique | non |
| Dictionnaire | cle | oui |

Retour : [[01-Python/Python - Index|Python - Index]]
