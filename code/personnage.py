import random
import pygame as pyg










"""
class Perso(pyg.sprite.Sprite):
    def __init__(self, nom, pv, strength, pv_max=20, chance=3, alive=True):
        super().__init__()
        self.nom = nom
        self.pv = pv
        self.strength = strength
        self.pv_max = pv_max
        self.chance = chance
        self.alive = alive
        self.speed = 5
        self.image = pyg.image.load("../assets/Player.png").convert_alpha()
        self.rect = self.image.get_rect()

    def afficher(self):
        print(self.nom, "a", self.pv, "pv")

    def est_mort(self):
        print(self.nom, "est quoicoudead")
        self.alive = False

    def attaque(self, adversaire):
        print(self.nom, "attaque", adversaire.nom)
        if random.randint(1, 6) < 6:
            adversaire.pv -= self.strength
        else:
            print("quoicoup critique")
            adversaire.pv -= 2 * self.strength
        adversaire.afficher()
        if adversaire.pv <= 0:
            adversaire.est_mort()

    def combat(self, adversaire):
        while self.alive == True and adversaire.alive:
            self.attaque(adversaire)
            adversaire.attaque(self)
        if self.alive == False:
            print(adversaire.nom, "a quoicougagné !")
            print(adversaire.nom, "a", adversaire.pv, "pv")
        else:
            print(self.nom, "a quoicougagné !")
            print(self.nom, "a", self.pv, "pv")

    def heal(self, hp):
        if self.alive:
            self.pv += hp + self.pv
        else:
            print("eh bah non t'es mort")


class ennemie:
    def __init__(self, nom, pv, strength, alive=True):
        self.nom = nom
        self.pv = pv
        self.strenght = strength
        self.alive = alive


def player():
    name = input("Nom du joueur : ")
    p1 = Perso(name, 20, 3)
    
    print("nom :", p1.nom, "\nvie :", p1.pv, "\nforce :", p1.strength)
    p1.combat(p2)


player()"""
