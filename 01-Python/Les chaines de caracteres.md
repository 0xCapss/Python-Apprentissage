---
tags: [python, chaines, str]
---
# Les chaines de caracteres (str)

Une chaine est une suite de caracteres : "bonjour". Elle ressemble a une liste de lettres.

## Operations utiles
```python
len("abc")            # 3 : nombre de caracteres
for c in "abc":       # parcours caractere par caractere : 'a', 'b', 'c'
    print(c)
"abc"[0]              # 'a' : on indexe comme une liste (commence a 0)
"a" + "b"             # 'ab' : concatenation
"abc".upper()         # 'ABC'
"ABC".lower()         # 'abc'
"a,b,c".split(",")    # ['a', 'b', 'c'] : decoupe en liste
```

## Tests sur un caractere (ou une chaine)
```python
"7".isdigit()    # True : que des chiffres
"a".isdigit()    # False
"abc".isalpha()  # True : que des lettres
"abc".startswith("ab")  # True
"chat" in "les chats"   # True : sous-chaine presente
```

## Rappel piege (vu en E03)
for c in chaine donne la VALEUR du caractere, pas sa position.
Pour la position aussi, utiliser [[01-Python/enumerate|enumerate]].

Vu en pratique dans [[03-Exercices/E09 - Mot de passe valide|E09]] (validation d'un mot de passe).

Retour : [[01-Python/Python - Index|Python - Index]]
