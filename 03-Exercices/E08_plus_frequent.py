"""
E08 (synthese) - L'element le plus frequent

Aucune notion nouvelle : on COMBINE deux exercices deja faits.
  Etape 1 = compter les occurrences avec un dictionnaire (E06).
  Etape 2 = trouver la cle au plus grand compte (patron du max, E05).

Cas reel cyber : reperer l'IP (ou le mot de passe, l'URL...) qui revient le plus
dans une liste issue de logs.

Points cles :
- Decouper un gros probleme en deux sous-problemes deja connus = methode REGT, etape G.
- Etape 2 parcourt le DICTIONNAIRE (compteur.items()), pas la liste d'origine.
- compteur.items() avec les parentheses : on APPELLE la methode pour obtenir les couples.
- On renvoie la CLE gagnante (meilleur_ip), pas la derniere cle vue, ni le compte.
- Init occurence_max = 0 est correct ici car un compte vaut toujours >= 1 (contraste avec E01).
- Liste vide -> dictionnaire vide -> aucune mise a jour -> meilleur_ip reste None. Gere gratuitement.
"""


def element_le_plus_frequent(liste):
    # Etape 1 : compter
    compteur = {}
    for element in liste:
        compteur[element] = compteur.get(element, 0) + 1

    # Etape 2 : trouver la cle au plus grand compte
    meilleur_element = None
    occurence_max = 0
    for element, compte in compteur.items():
        if compte > occurence_max:
            occurence_max = compte
            meilleur_element = element
    return meilleur_element


# Verifications
print(element_le_plus_frequent(["10.0.0.1", "10.0.0.2", "10.0.0.1", "10.0.0.1", "10.0.0.2"]))  # 10.0.0.1
print(element_le_plus_frequent(["a", "b", "b", "c"]))  # b
print(element_le_plus_frequent([]))                    # None
