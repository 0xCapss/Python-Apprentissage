---
tags: [exercice, algorithmie, dictionnaire, comptage]
statut: termine
---
# E06 - Compter les occurrences

## Enonce
On te donne une liste d'elements (ex: des mots). Tu dois renvoyer un dictionnaire
qui associe chaque element au nombre de fois qu'il apparait.
Exemple : ["chat", "chien", "chat", "oiseau", "chat", "chien"]
       -> {"chat": 3, "chien": 2, "oiseau": 1}

## Mon raisonnement (methode REGT)

R - Reformuler
- Entree : une liste d'elements.
- Sortie : un dictionnaire {element: nombre d'occurrences}.

E - Exemple a la main
Je parcours la LISTE (pas le dictionnaire, que je construis). Pour chaque element,
j'ajoute 1 a son compteur dans le dictionnaire.

G - Generaliser (pseudo-code)
```
compteur = dictionnaire vide
pour chaque element de la liste :
    si element deja present dans compteur :
        compteur[element] = compteur[element] + 1
    sinon :
        compteur[element] = 1
renvoyer compteur
```

T - Traduire (Python)
```python
def compter_occurrences(liste):
    compteur = {}
    for element in liste:
        if element in compteur:
            compteur[element] += 1
        else:
            compteur[element] = 1
    return compteur
```
Variante avec .get : `compteur[element] = compteur.get(element, 0) + 1`
Code complet : voir E06_compter_occurrences.py.

## Lecons importantes
- Accumulateur = un DICTIONNAIRE (voir [[01-Python/Les dictionnaires|note dictionnaires]]).
- Piege de la premiere fois : compteur[mot] += 1 plante (KeyError) si la cle n'existe pas,
  car += doit d'abord lire la valeur actuelle. On gere avec if ... in ... / else, ou .get.
- compteur[mot] = UN tiroir ; compteur seul = tout le dictionnaire (attention au return).
- Erreurs traversees : TypeError (+= sur le dict entier), appel avec 6 args au lieu d'une liste,
  KeyError, return d'un seul tiroir au lieu du dico.
- Liste vide -> {} gratuitement.

## Verification
- [x] ["chat", "chien", "chat", "oiseau", "chat", "chien"] -> {"chat": 3, "chien": 2, "oiseau": 1}
- [x] [] -> {}
- [x] ["a"] -> {"a": 1}

Retour : [[03-Exercices/Exercices - Index|Exercices - Index]]
