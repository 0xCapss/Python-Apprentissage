"""
E11 - Casser le chiffre de Cesar

Deux approches pour retrouver la cle sans la connaitre :
  1. Analyse de frequence : la lettre la plus courante est probablement E.
     Fonctionne sur les textes longs, peu fiable sur les textes courts.
  2. Force brute : tester les 26 cles possibles et lire les resultats.

Points cles :
- range(0, 26) : 0 inclus, 26 exclu -> donne bien 0 a 25.
- Une fonction qui print en interne ne doit pas etre enveloppee dans print().
"""

from E10_chiffre_cesar import Chiffrer_Mot


# --- Approche 1 : analyse de frequence ---

def frequence_lettres(message):
    compteur = {}
    for lettre in message:
        if lettre == " ":
            continue
        lettre = lettre.upper()
        compteur[lettre] = compteur.get(lettre, 0) + 1
    return compteur


def deviner_cle(message):
    compteur = frequence_lettres(message)
    lettre_max = max(compteur, key=compteur.get)
    cle = (ord(lettre_max) - ord('E')) % 26
    return cle


# --- Approche 2 : force brute ---

def bruteforce_cesar(message):
    for decalage in range(0, 26):
        resultat = Chiffrer_Mot(message, 26 - decalage)
        print(f"Decalage {decalage:2d}: {resultat}")


# --- Tests ---
message = "KHOOR ZRUOG"

print("=== Analyse de frequence ===")
cle_devinee = deviner_cle(message)
print(f"Cle devinee : {cle_devinee}")
print(f"Resultat    : {Chiffrer_Mot(message, 26 - cle_devinee)}")

print()
print("=== Force brute ===")
bruteforce_cesar(message)
