---
tags: [exercice, algorithmie, liste]
statut: termine
---
# E01 - Le plus grand d'une liste

## Enonce
On te donne une liste de nombres, par exemple [3, 7, 2, 9, 4].
Tu dois renvoyer le plus grand. Ici : 9.
Contrainte pedagogique : interdit d'utiliser max(). Le but est de comprendre
ce que max() fait vraiment a l'interieur.

## Mon raisonnement (methode REGT)

R - Reformuler
- Entree : une liste de nombres.
- Sortie : un seul nombre, le plus grand de la liste.

E - Exemple a la main
Je parcours la bande de papier un nombre a la fois, de gauche a droite.
Je garde en memoire le plus grand vu jusqu'ici. A chaque nouveau nombre,
je le compare a ma memoire : s'il est plus grand, il devient ma nouvelle memoire.
Trace sur [3, 7, 2, 9, 4] : memoire = 3, puis 7, puis 7, puis 9, puis 9. Reponse : 9.

G - Generaliser (pseudo-code)
```
memoire = premier element de la liste
pour chaque nombre de la liste :
    si nombre > memoire :
        memoire = nombre
renvoyer memoire
```

T - Traduire (Python)
```python
def plus_grand(liste):
    memoire = liste[0]
    for nombre in liste:
        if nombre > memoire:
            memoire = nombre
    return memoire
```
Code complet et testable : voir E01_plus_grand.py dans ce meme dossier.

## Idees cles retenues
- Variable d'etat : une memoire qui garde le "meilleur jusqu'ici".
- Initialiser avec liste[0] et non 0 : sinon une liste toute negative donnerait un faux resultat.
- "Pour chaque element" = une boucle for (bornee, elle s'arrete a la fin de la liste).

## Verification
- [x] Teste sur [3, 7, 9, 2, 4], attendu 9, obtenu 9
- [x] Teste sur [5], attendu 5, obtenu 5
- [x] Teste sur [-5, -2, -9], attendu -2, obtenu -2 (piege du depart a 0 evite)
- [x] Liste vide [] : geree par une garde en debut de fonction, renvoie None

## Cas limite (liste vide)
Sans protection, liste[0] sur une liste vide leve une IndexError (code teste).
Solution : une garde tout en haut de la fonction.
```python
if len(liste) == 0:
    return None
```
Idees retenues :
- Une garde intercepte un cas problematique des l'entree de la fonction.
- Du code place apres un return est du code mort : jamais execute.
- "texte" + nombre leve une TypeError ; pour inserer une valeur dans du texte, on utilise une f-string : f"... {variable} ...".
- Une fonction calcule et renvoie ; l'affichage est le role du programme appelant.

Retour : [[03-Exercices/Exercices - Index|Exercices - Index]]
