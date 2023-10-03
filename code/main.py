import pygame as pyg
import sys
from personnage import *
from item import *
from niveau import Niveau
from parametre import *


class Game:
    def __init__(self):
        pyg.init()
        self.screen = pyg.display.set_mode((size_x, size_y))
        self.clock = pyg.time.Clock()

        self.niveau = Niveau()

        pyg.display.set_caption("Zeldouille")

    def run(self):
        while True:
            for event in pyg.event.get():
                if event.type == pyg.QUIT:
                    pyg.quit()
                    print("fermeture du jeu")
                    sys.exit()

            self.screen.fill('black')
            self.niveau.run()
            pyg.display.update()
            self.clock.tick(fps)



if __name__ == "__main__":
    game = Game()
    game.run()
