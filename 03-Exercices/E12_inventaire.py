"""
E12 - Inventaire

Utilise un dictionnaire comme inventaire et retourne un tuple
des produits dont la quantite est strictement inferieure au seuil.

Points cles :
- Les tuples sont immuables : on accumule dans une liste, puis tuple().
- Un tuple a un seul element s'ecrit ("valeur",) — la virgule est obligatoire.
- .items() pour parcourir cle et valeur simultanement.
"""


def produits_en_rupture(inventaire, seuil):
    produits_rupture = []
    for produit, quantite in inventaire.items():
        if quantite < seuil:
            produits_rupture.append(produit)
    return tuple(produits_rupture)


# --- Test ---
produits = {"pomme": 10, "banane": 5, "cerise": 42}
resultat = produits_en_rupture(produits, 10)
print(resultat)  # ('banane',)
