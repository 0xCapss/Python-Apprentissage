"""
E09 - Mot de passe valide ?

Pratique "cyber" : valider un mot de passe selon deux regles.
  Regle 1 : au moins 8 caracteres.
  Regle 2 : contient au moins un chiffre.

Notions :
- len(chaine) : nombre de caracteres.
- for caractere in chaine : on parcourt une chaine caractere par caractere.
- caractere.isdigit() : True si le caractere est un chiffre.

Points cles :
- Erreur de frontiere : "au moins 8" = len < 8 pour rejeter (8 est accepte, donc pas <=).
- Une fonction de validation renvoie True/False, pas None, pas un print.
- ASYMETRIE importante :
  * trouver UN chiffre suffit pour conclure True (return tout de suite).
  * pour conclure False, il faut avoir verifie TOUS les caracteres -> le return False
    se place APRES la boucle, pas dedans (sinon on abandonne des la 1re lettre).
- Entre deux codes corrects, choisir le plus lisible (ici, return False simple
  plutot qu'un for...else que peu de gens connaissent).
"""


def mot_de_passe_valide(password):
    if len(password) < 8:           # regle 1 : trop court -> invalide
        return False
    for caractere in password:      # regle 2 : chercher un chiffre
        if caractere.isdigit():
            return True             # un chiffre trouve -> valide
    return False                    # boucle finie sans chiffre -> invalide


# Verifications
print(mot_de_passe_valide("abc"))           # False (trop court)
print(mot_de_passe_valide("abcdefgh"))      # False (pas de chiffre)
print(mot_de_passe_valide("abcdef12"))      # True
print(mot_de_passe_valide("motdepasse9"))   # True
print(mot_de_passe_valide("azerty123"))     # True
