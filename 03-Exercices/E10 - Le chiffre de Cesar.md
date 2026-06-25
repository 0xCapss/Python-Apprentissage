---
tags: [exercice, pratique, chiffrement, chaines, modulo, cyber]
statut: termine
---
# E10 - Le chiffre de Cesar

## Enonce
Ecrire une fonction qui chiffre un mot avec le chiffre de Cesar.
Entree : un mot (chaine) et un decalage (entier). Sortie : le mot chiffre.
- chiffrer("CHAT", 2) -> "EJCV"
- chiffrer("HELLO WORLD", 2) -> "JGNNQ YQTNF"
- Pour dechiffrer : chiffrer("JGNNQ YQTNF", 26 - 2) -> "HELLO WORLD"

## Mon raisonnement (REGT)

**R** - Entree : une chaine + un entier. Sortie : une chaine chiffree.
Chaque lettre est remplacee par la lettre N rangs plus loin. A la fin de l'alphabet, on boucle.

**E** - A la main avec CHAT, decalage 2 :
C(2) -> E(4), H(7) -> J(9), A(0) -> C(2), T(19) -> V(21) -> EJCV

**G** - Formule : `nouvelle_position = (position + decalage) % 26`
avec `position = ord(lettre) - ord('A')`.
Le % 26 gere le bouclage. En Python, le modulo est toujours positif donc le dechiffrement
(soustraction) fonctionne aussi sans condition speciale.

**T** - Traduire (Python) : voir E10_chiffre_cesar.py

## Lecons importantes
- `ord` convertit une lettre en nombre, `chr` fait l'inverse.
- `lettre.upper()` avant le calcul : sinon les minuscules donnent des positions erronees.
- Le modulo doit entourer `(position + decalage)` entier, pas juste `position`.
- Dechiffrer = chiffrer avec `26 - decalage` : une seule fonction suffit.
- Cas particulier espace : le detecter et le conserver tel quel (pas une lettre).

## Verification
- [x] ChiffrageCesar('A', 2) -> 'C'
- [x] ChiffrageCesar('Z', 3) -> 'C'  (test du bouclage)
- [x] Chiffrer_Mot("CHAT", 2) -> "EJCV"
- [x] Chiffrer_Mot("chat", 2) -> "EJCV"  (test minuscules)
- [x] Chiffrer_Mot("HELLO WORLD", 2) -> "JGNNQ YQTNF"  (test espace)
- [x] Chiffrer_Mot("JGNNQ YQTNF", 26 - 2) -> "HELLO WORLD"  (test dechiffrement)

Notion liee : [[02-Algorithmie/Algo - Chiffre de Cesar|Algo - Chiffre de Cesar]]

Retour : [[03-Exercices/Exercices - Index|Exercices - Index]]
