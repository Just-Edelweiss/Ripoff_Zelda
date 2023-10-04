import pygame as pyg
from parametre import *

class Perso(pyg.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pyg.image.load('assets/Player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

        self.direction = pyg.math.Vector2()
        self.speed = 2.5

    def input(self):
        keys = pyg.key.get_pressed()

        if keys[pyg.K_z]:
            self.direction.y = -1
        elif keys[pyg.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pyg.K_q]:
            self.direction.x = -1
        elif keys[pyg.K_d]:
            self.direction.x = 1
        else:
            self.direction.x = 0

    def deplacement(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        
        self.rect.center += self.direction * speed

    def update(self):
        self.input()
        self.deplacement(self.speed)