---
tags: [algorithmie, methode, cle]
---
# Decomposer un probleme - la methode REGT

Quand un enonce te parait trop gros ou que tu ne sais pas par ou commencer,
tu n'as pas un probleme d'intelligence : il te manque un protocole. En voici un.

REGT = Reformuler, Exemple a la main, Generaliser, Traduire.

## R - Reformuler (Entrees vers Sorties)
Reponds a 2 questions, par ecrit :
- Qu'est-ce que je recois ? (les entrees : une liste ? un nombre ? du texte ?)
- Qu'est-ce que je dois renvoyer ? (la sortie : un nombre ? un booleen ? une nouvelle liste ?)

Si tu ne sais pas repondre a ca, tu ne peux pas coder. C'est toujours la 1re etape.

## E - Exemple a la main
Prends un petit cas concret et resous-le avec un stylo, sans penser au code.
Le secret : observe ce que tu fais physiquement. Tu pointes du doigt ? Tu retiens un nombre ?
Tu compares deux choses ? Ces gestes sont l'algorithme.

## G - Generaliser
Transforme tes gestes en etapes repetables :
- Qu'est-ce que je repete ? Ce sera une boucle.
- Qu'est-ce que je dois retenir entre deux etapes ? Ce sera une variable d'etat.
- Quand est-ce que je fais un choix ? Ce sera une condition (if).

Ecris ca en pseudo-code (francais, pas Python) :
```
etat_de_depart = ...
pour chaque element :
    si (condition) :
        mettre a jour l'etat
renvoyer l'etat
```

## T - Traduire
Seulement maintenant, tu ecris du Python, ligne a ligne, a partir du pseudo-code.
Puis tu verifies sur l'exemple de l'etape E.

## Pourquoi ca marche
La plupart des blocages viennent du fait qu'on essaie de coder et de reflechir au
probleme en meme temps. REGT separe les deux : d'abord on pense (R, E, G),
ensuite on ecrit (T). Deux taches plus simples valent mieux qu'une tache impossible.

Retour : [[02-Algorithmie/Algorithmie - Index|Algorithmie - Index]]
