---
tags: [algorithmie, chiffrement, chaines, modulo]
---
# Le chiffre de Cesar

Premier algorithme de chiffrement : decaler chaque lettre d'un nombre fixe dans l'alphabet.
Le principe est simple, la subtilite est le bouclage.

## Principe

Chaque lettre est remplacee par la lettre situee N rangs plus loin dans l'alphabet.
Quand on depasse Z, on recommence depuis A.

Exemple avec decalage = 2 :
- A -> C, B -> D, Z -> B
- CHAT -> EJCV

## La formule cle

```
nouvelle_position = (position + decalage) % 26
```

- `position` = rang de la lettre dans l'alphabet (A=0, B=1, ... Z=25)
- `% 26` gere le bouclage automatiquement (Python garantit un resultat positif)
- Pour convertir : `position = ord(lettre) - ord('A')` et `lettre = chr(position + ord('A'))`

## Le dechiffrement

Dechiffrer = chiffrer avec le decalage inverse.

```
dechiffrer(mot, d) = chiffrer(mot, 26 - d)
```

`26 - 2 = 24` : chiffrer de 24 rangs en avant = reculer de 2 rangs.
Pas besoin d'une fonction separee.

## Pieges a eviter

- `ord('a')` != `ord('A')` : toujours convertir en majuscule avant de calculer (`lettre.upper()`).
- Le modulo doit entourer TOUT le calcul `(position + decalage) % 26`, pas juste `position`.
- Les espaces (et ponctuation) ne sont pas des lettres : les traiter comme cas particulier.

## Lien avec Python

- `ord(c)` : caractere -> code ASCII
- `chr(n)` : code ASCII -> caractere
- `str.upper()` : convertit en majuscule
- `% 26` : reste de la division par 26 (toujours >= 0 en Python)

Exercice lie : [[03-Exercices/E10 - Le chiffre de Cesar|E10 - Le chiffre de Cesar]]

Retour : [[02-Algorithmie/Algorithmie - Index|Algorithmie - Index]]
