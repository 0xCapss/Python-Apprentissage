---
tags: [exercice, pratique, chiffrement, analyse, cyber]
statut: termine
---
# E11 - Casser le chiffre de Cesar

## Enonce
On te donne un message chiffre avec le chiffre de Cesar, sans connaitre la cle.
Retrouver le message original. Deux approches : analyse de frequence et force brute.

## Mon raisonnement (REGT)

**R** - Entree : un message chiffre. Sortie : le message dechiffre (et la cle).
On ne connait pas la cle — il faut la retrouver.

**E** - "KHOOR ZRUOG" :
- Frequence : O apparait 3 fois -> suppose O = E -> cle = 14 - 4 = 10.
- Resultat : faux. Sur 10 lettres, la statistique n'est pas fiable.
- Force brute : on teste les 26 cles -> decalage 3 donne "HELLO WORLD".

**G** - Deux strategies :
1. Analyse de frequence : lettre la plus frequente = E (fonctionne sur textes longs).
   cle = position(lettre_frequente) - position('E')
2. Force brute : tester les 26 cles, lire les resultats, choisir le sens.

**T** - Traduire (Python) : voir E11_casser_cesar.py

## Lecons importantes
- L'analyse de frequence ne fonctionne QUE sur des textes suffisamment longs.
  Sur un texte court, la lettre la plus frequente n'est pas forcement E.
- La force brute est toujours fiable sur le Cesar : seulement 26 cles a tester.
- `print(fonction())` affiche None si la fonction n'a pas de `return`.
  Une fonction qui affiche avec `print` en interne n'a pas besoin d'etre enveloppee.
- `range(0, 26)` : 0 inclus, 26 exclu -> donne bien 0 a 25.

## Verification
- [x] bruteforce_cesar("KHOOR ZRUOG") -> affiche "HELLO WORLD" au decalage 3
- [x] Analyse de frequence : echec sur texte court (O != E dans ce cas)
- [x] Force brute : succes sur tous les textes

Notion liee : [[02-Algorithmie/Algo - Chiffre de Cesar|Algo - Chiffre de Cesar]]

Retour : [[03-Exercices/Exercices - Index|Exercices - Index]]
