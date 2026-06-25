---
tags: [exercice, pratique, chaines, condition, cyber]
statut: termine
---
# E09 - Mot de passe valide ?

## Enonce
On te donne un mot de passe (chaine). Renvoyer True s'il est valide, False sinon.
Regles : 1) au moins 8 caracteres, ET 2) au moins un chiffre.
- "abc" -> False ; "abcdefgh" -> False ; "abcdef12" -> True ; "motdepasse9" -> True

## Outils chaines
- len(mot) : nombre de caracteres.
- for caractere in mot : parcours caractere par caractere.
- caractere.isdigit() : True si le caractere est un chiffre.

## Mon raisonnement (REGT)
R - Entree : une chaine. Sortie : un booleen (True/False).
G - Deux regles a verifier : la longueur (facile, len), puis la presence d'un chiffre (parcours + drapeau).

T - Traduire (Python)
```python
def mot_de_passe_valide(password):
    if len(password) < 8:
        return False
    for caractere in password:
        if caractere.isdigit():
            return True
    return False
```
Code complet : voir E09_mot_de_passe.py.

## Lecons importantes
- Erreur de frontiere : "au moins 8" -> rejeter si len < 8 (8 est accepte, donc pas <=).
- Une fonction de validation renvoie True/False, pas None ni un print.
- ASYMETRIE des conclusions :
  - trouver UN chiffre suffit -> return True immediatement ;
  - conclure False exige d'avoir verifie TOUS les caracteres -> return False APRES la boucle,
    jamais dans un else qui abandonne des la 1re lettre.
- Entre deux codes corrects, choisir le plus lisible (return False simple plutot que for...else).

## Verification
- [x] "abc" -> False
- [x] "abcdefgh" -> False
- [x] "abcdef12" -> True
- [x] "motdepasse9" -> True
- [x] "azerty123" -> True

Retour : [[03-Exercices/Exercices - Index|Exercices - Index]]
