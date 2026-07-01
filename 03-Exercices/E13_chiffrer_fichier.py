def ChiffrageCesar(lettre, decalage):
    position = ord(lettre.upper()) - ord('A')   # A=0, B=1, ... Z=25
    nouvelle_position = (position + decalage) % 26
    return chr(nouvelle_position + ord('A'))


def Chiffrer_Mot(mot, decalage):
    resultat = ""
    for lettre in mot:
        if lettre == " ":
            resultat += " "
            continue
        resultat += ChiffrageCesar(lettre, decalage)
    return resultat


with open("message.txt", 'r') as file:
    contenu = file.read()

with open("message_chiffre.txt", 'w') as file:
    file.write(Chiffrer_Mot(contenu, 3))
