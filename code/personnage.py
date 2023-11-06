import pygame as pyg
from parametre import *

class Perso(pyg.sprite.Sprite):
    def __init__(self, pos, groups, sprites_barriere):
        super().__init__(groups)
        self.image = pyg.image.load('assets/player/animation_bas/bas_1.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(-24, 0)

        self.import_player_assets()

        self.direction = pyg.math.Vector2()
        self.speed = 5

        self.attaque = False
        self.attaque_cooldown = 400 # in millisecond
        self.attaque_time = None

        self.sprites_barriere = sprites_barriere

    def import_player_assets(self):
        chemin_perso = 'assets/player/'
        self.animations = {
            'haut':[], 'bas':[], 'droite':[],'gauche':[],
        }

        for animation in self.animations.keys():
            print(animation)

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

        if keys[pyg.K_SPACE] and not self.attaque:
            self.attaque = True
            self.attaque_time = pyg.time.get_ticks()
            print('attaque')

    def deplacement(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        
        self.hitbox.x += self.direction.x * speed
        self.collision('horizontale')
        self.hitbox.y += self.direction.y * speed
        self.collision('verticale')
        self.rect.center = self.hitbox.center

    
    def collision(self, direction):
        if direction == 'horizontale':
            for sprite in self.sprites_barriere:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0: # se déplacer à droite
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0: # se déplacer à gauche
                        self.hitbox.left = sprite.hitbox.right

        if direction == 'verticale':
            for sprite in self.sprites_barriere:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0: # se déplacer en bas
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0: # se déplacer en haut
                        self.hitbox.top = sprite.hitbox.bottom

    def cooldown(self):
        temps_acctuel = pyg.time.get_ticks()

        if self.attaque:
            if temps_acctuel - self.attaque_time >= self.attaque_cooldown:
                self.attaque = False

    def update(self):
        self.input()
        self.deplacement(self.speed)