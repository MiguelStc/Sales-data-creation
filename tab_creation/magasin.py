class produit:
    def __init__(
        self, rayon, marque, prix_achat, prix_vente, fournisseur, ID, bio, tva, nom
    ):

        self.rayon = rayon
        self.marque = marque
        self.prix_achat = prix_achat
        self.prix_vente = prix_vente
        self.fournisseur = fournisseur
        self.ID = ID
        self.bio = bio
        self.tva = tva
        self.nom = nom


class client:
    def __init__(self, nom, prenom, numTel, email, codePostal, adresse, age, sexe, rrv):
        self.nom = nom
        self.prenom = prenom
        self.numTel = numTel
        self.email = email
        self.codePostal = codePostal
        self.adresse = adresse
        self.age = age
        self.sexe = sexe
        self.rrv = rrv
