---
tags: [python, dictionnaire, structure]
---
# Les dictionnaires

## Idee
Une structure qui associe une CLE a une VALEUR. Image : une rangee de tiroirs etiquetes.
L'etiquette = la cle (que tu choisis), le contenu = la valeur.

Difference avec une liste :
- liste : les etiquettes sont imposees, ce sont les positions 0, 1, 2...
- dictionnaire : tu choisis les etiquettes (un mot, un nom, un id...).

## Operations de base
```python
d = {}                 # dictionnaire vide (accolades)
d["chat"] = 3          # creer / ecrire le tiroir "chat" avec la valeur 3
d["chat"] = 5          # remplacer la valeur du tiroir "chat"
x = d["chat"]          # lire la valeur du tiroir "chat"
"chat" in d            # True si la cle "chat" existe
d.keys()               # les cles
d.values()             # les valeurs
d.items()              # les couples (cle, valeur), pratique pour parcourir
```

## Parcourir un dictionnaire
```python
for cle, valeur in d.items():
    print(cle, "->", valeur)
```

## Piege majeur : la cle qui n'existe pas encore
Lire ou faire += sur une cle absente leve une KeyError.
```python
d = {}
d["chat"] += 1         # KeyError : il faut LIRE d["chat"] qui n'existe pas
```
Deux solutions :
```python
# 1) tester l'existence
if "chat" in d:
    d["chat"] += 1
else:
    d["chat"] = 1

# 2) .get avec valeur par defaut (raccourci tres courant)
d["chat"] = d.get("chat", 0) + 1
```

## Pourquoi c'est utile (et tres present en cyber)
Compter des occurrences (IP dans des logs, codes HTTP, mots de passe frequents),
associer un identifiant a des infos, faire des correspondances/lookup rapides.

Vu en pratique dans [[03-Exercices/E06 - Compter les occurrences|E06]].

Retour : [[01-Python/Python - Index|Python - Index]]
