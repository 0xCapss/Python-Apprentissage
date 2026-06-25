---
tags: [python, fondation, fonctions, portee, scope]
---
# Fonctions et portee

## Ce qu'une fonction fait

Une fonction prend des **arguments** en entree, execute des instructions, et renvoie
une valeur avec `return`. Chaque appel est independant.

```python
def ChiffrageCesar(lettre, decalage):
    position = ord(lettre.upper()) - ord('A')
    nouvelle_position = (position + decalage) % 26
    return chr(nouvelle_position + ord('A'))
```

`lettre` et `decalage` sont des **parametres** : ils n'existent qu'a l'interieur de la fonction.

## La portee (scope)

Les variables creees dans une fonction sont **locales** : elles n'existent que pendant
l'execution de la fonction, puis disparaissent.

```python
def ma_fonction():
    x = 42       # variable locale

ma_fonction()
print(x)         # NameError : x n'existe pas ici
```

## Lecture vs assignation

Une fonction **lit** les variables globales sans probleme.
Mais si elle **assigne** (`x = ...`), elle cree une variable locale — pas de modification du global.

```python
x = 10

def ma_fonction():
    x = 99       # variable LOCALE, le global x=10 est intact
    print(x)     # 99

ma_fonction()
print(x)         # 10
```

```
Espace global : x = 10
Espace local (ma_fonction) : x = 99   <- independant
```

## Le piege avec les mutables

Une fonction ne peut pas reassigner un global, mais elle peut **modifier** un objet mutable
(liste, dict) passe en argument — car elle recoit une reference vers le meme objet.

```python
def ajouter(liste, valeur):
    liste.append(valeur)   # modifie l'objet original

nombres = [1, 2, 3]
ajouter(nombres, 4)
print(nombres)             # [1, 2, 3, 4]
```

Si tu ne veux pas modifier l'original, passe une copie : `ajouter(nombres.copy(), 4)`.

## Regles a retenir

1. Parametre = variable locale, disparait apres l'appel.
2. Une fonction lit le global, mais assigner cree un local (le global reste intact).
3. Passer une liste a une fonction = passer une reference. La fonction peut la modifier.

Vu en pratique dans : [[03-Exercices/E01 - Le plus grand d'une liste|E01]] et suivants.

Retour : [[01-Python/Python - Index|Python - Index]]
