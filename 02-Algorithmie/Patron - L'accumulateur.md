---
tags: [algorithmie, methode, cle, patron]
---
# Le patron de l'accumulateur

Un seul et meme schema resout une enorme quantite de problemes sur les listes.
Une fois que tu le reconnais, tu n'es plus jamais perdu devant un parcours de liste.

## Le squelette
```
accumulateur = valeur de depart (l'etat "vide")
pour chaque element de la liste :
    si (une condition) :
        mettre a jour l'accumulateur avec l'element
renvoyer accumulateur
```

## La seule chose qui change : l'accumulateur
| Probleme | Accumulateur | Depart (etat vide) | Mise a jour |
|---|---|---|---|
| Le plus grand (E01) | un nombre (le max) | le 1er element | si plus grand, on remplace |
| Compter (E02) | un nombre (compteur) | 0 | si condition, on fait +1 |
| Filtrer (E03) | une liste | [] (liste vide) | si condition, on append |
| Moyenne (E04) | DEUX : somme + compteur | 0 et 0 | somme += nombre ; nb += 1, puis somme/nb |
| Sommer | un nombre (somme) | 0 | on ajoute l'element |

## Les 3 questions a se poser face a un nouveau probleme de liste
1. **Quel est mon accumulateur ?** (un nombre ? une liste ? un booleen ?)
2. **Quelle est sa valeur de depart**, son etat "vide" ? (0, [], le 1er element...)
3. **Quand et comment** je le mets a jour a chaque element ?

Reponds a ces 3 questions, et le code s'ecrit presque tout seul.

## Le bonus cache
Si la valeur de depart est bien choisie (0, []), le cas de la **liste vide** est
souvent gere gratuitement : la boucle ne tourne pas, et on renvoie l'etat de depart,
qui est deja la bonne reponse.

## Pieges deja rencontres
- `for x in liste` donne la VALEUR de x, pas sa position. (E03)
- L'initialisation de l'accumulateur doit etre HORS du if, toujours executee. (E02)
- Le cas vide n'a pas la meme reponse selon le probleme : None pour un max, 0/[] pour cumuler. (E01/E02)

Exercices lies : [[03-Exercices/E01 - Le plus grand d'une liste|E01]], [[03-Exercices/E02 - Compter au-dessus d'un seuil|E02]], [[03-Exercices/E03 - Garder les nombres pairs|E03]].

Retour : [[02-Algorithmie/Algorithmie - Index|Algorithmie - Index]]
