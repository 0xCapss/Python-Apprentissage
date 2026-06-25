"""
E10 - Le chiffre de Cesar

Premier algorithme de chiffrement : decaler chaque lettre d'un nombre fixe.
Formule : nouvelle_position = (position + decalage) % 26

Notions :
- ord(c) : caractere -> code ASCII  (ord('A') = 65)
- chr(n) : code ASCII -> caractere  (chr(65) = 'A')
- str.upper() : convertit en majuscule avant calcul
- % 26 : gere le bouclage de l'alphabet (toujours >= 0 en Python)

Points cles :
- Appliquer .upper() sur l'entree, pas la sortie.
- Le modulo entoure (position + decalage) en entier.
- Dechiffrer = chiffrer avec (26 - decalage) : pas besoin d'une 2e fonction.
- Les espaces sont conserves tels quels (cas particulier dans la boucle).
"""


def ChiffrageCesar(lettre, decalage):
    position = ord(lettre.upper()) - ord('A')   # A=0, B=1, ... Z=25
    nouvelle_position = (position + decalage) % 26
    return chr(nouvelle_position + ord('A'))


def Chiffrer_Mot(mot, decalage):
    resultat = ""
    for lettre in mot:
        if lettre == " ":                        # conserver les espaces
            resultat += " "
            continue
        resultat += ChiffrageCesar(lettre, decalage)
    return resultat


# Verifications
print(Chiffrer_Mot("CHAT", 2))                  # EJCV
print(Chiffrer_Mot("chat", 2))                  # EJCV  (minuscules)
print(Chiffrer_Mot("HELLO WORLD", 2))           # JGNNQ YQTNF
print(Chiffrer_Mot("JGNNQ YQTNF", 26 - 2))     # HELLO WORLD  (dechiffrement)
