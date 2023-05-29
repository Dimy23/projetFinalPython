class Album:
    def __init__(self, id, titre, nomAuteur, annee, prenomAuteur, nbreChansons):
        self.id = id
        self.titre = titre
        self.nomAuteur = nomAuteur
        self.annee = annee
        self.prenomAuteur = prenomAuteur
        self.nbreChansons = nbreChansons
        int(nbreChansons)