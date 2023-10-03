class Item:
    def __init__(self, nom, durability):
        self.nom = nom
        self.durability = durability

    class Potion:
        def __init__(self, type, taille):
            self.type = type
            self.taille = taille
            