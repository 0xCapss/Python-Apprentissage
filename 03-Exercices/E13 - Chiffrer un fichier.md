---
tags: [exercice, pratique, fichiers, cesar]
statut: termine
---
# E13 - Chiffrer un fichier avec Cesar

## Enonce
Lire le contenu d'un fichier `message.txt`, chiffrer ce contenu avec le chiffre de Cesar
(decalage 3), et ecrire le resultat dans un nouveau fichier `message_chiffre.txt`.
S'appuyer sur les fonctions de E10.

## Mon raisonnement (REGT)

**R** - Entree : le fichier `message.txt` (contient `HELLO WORLD`) + un decalage (ici 3).
Sortie : le fichier `message_chiffre.txt` contenant le texte chiffre (`KHOOR ZRUOG`).

**E** - Etapes a la main avec `HELLO WORLD`, decalage 3 :
1. Ouvrir `message.txt` en lecture.
2. Lire le contenu → `HELLO WORLD`.
3. Chiffrer avec decalage 3 → `KHOOR ZRUOG`.
4. Ouvrir `message_chiffre.txt` en ecriture.
5. Ecrire `KHOOR ZRUOG` dedans.

**G** -
```
ouvrir message.txt en lecture
    lire le contenu -> texte

chiffrer texte avec decalage 3 -> texte_chiffre

ouvrir message_chiffre.txt en ecriture
    ecrire texte_chiffre
```

**T** - Traduire (Python) : voir E13_chiffrer_fichier.py

## Lecons importantes
- On reutilise une fonction existante (E10) sans la reecrire : c'est le principe de la composition.
- `file.read()` lit tout le contenu d'un coup sous forme de chaine.
- `with open(...)` ferme automatiquement le fichier a la fin du bloc.
- Pour dechiffrer : meme programme avec decalage = 26 - 3 = 23.

## Verification
- [x] `message.txt` contient `HELLO WORLD`
- [x] `message_chiffre.txt` contient `KHOOR ZRUOG`
- [x] Dechiffrement avec decalage 23 → retourne `HELLO WORLD`

Notion liee : [[03-Exercices/E10 - Le chiffre de Cesar|E10 - Le chiffre de Cesar]]
Notion liee : [[03-Exercices/E12 - Inventaire|E12 - Inventaire]] (manipulation de fichiers)

Retour : [[03-Exercices/Exercices - Index|Exercices - Index]]
