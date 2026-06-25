---
tags: [exercice, algorithmie, while, arithmetique]
statut: termine
---
# E07 - Compter les chiffres d'un nombre

## Enonce
On te donne un entier positif (ex: 4087). Tu dois renvoyer son NOMBRE de chiffres.
Exemple : 4087 -> 4 ;  9 -> 1 ;  100 -> 3.
Contrainte : interdit de convertir en texte (pas de str(n) ni len()).

## Outils
- n % 10  : dernier chiffre de n        (4087 % 10 = 7)
- n // 10 : n sans son dernier chiffre   (4087 // 10 = 408) -- division entiere

## Mon raisonnement (methode REGT)

R - Reformuler
- Entree : un entier positif.
- Sortie : un entier, son nombre de chiffres.

E - Exemple a la main
J'enleve les chiffres un par un (// 10) en comptant, jusqu'a tomber sur 0.
4087 -> 408 -> 40 -> 4 -> 0 : 4 retraits, donc 4 chiffres.

G - Generaliser (pseudo-code)
```
si nombre vaut 0 : renvoyer 1
compteur = 0
tant que nombre != 0 :
    nombre = nombre // 10
    compteur = compteur + 1
renvoyer compteur
```

T - Traduire (Python)
```python
def nb_chiffres(nombre):
    if nombre == 0:
        return 1
    compteur_chiffre = 0
    while nombre != 0:
        nombre = nombre // 10
        compteur_chiffre += 1
    return compteur_chiffre
```
Code complet : voir E07_nb_chiffres.py.

## Lecons importantes
- while = repeter TANT QUE, quand le nombre de tours est inconnu d'avance.
- Boucle infinie : il faut que quelque chose (ici nombre // 10) rapproche de la sortie.
- PIEGE MAJEUR vecu : la boucle modifie 'nombre', qui vaut toujours 0 a la sortie.
  Donc la garde sur le cas d'entree 0 doit etre TOUT EN HAUT, pas dans/apres la boucle
  (sinon elle se declenche a chaque fois et renvoie toujours 1).
- Reflexe a garder : "cette variable vaut quoi, a quel moment ?"

Voir aussi [[01-Python/La boucle while|note : la boucle while]].

## Verification
- [x] 4087 -> 4
- [x] 9 -> 1
- [x] 100 -> 3
- [x] 0 -> 1 (gere par la garde)

Retour : [[03-Exercices/Exercices - Index|Exercices - Index]]
