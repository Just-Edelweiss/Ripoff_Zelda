import pygame as pyg
from parametre import *
from support import import_fichier

class Perso(pyg.sprite.Sprite):
    def __init__(self, pos, groups, sprites_barriere):
        super().__init__(groups)
        self.image = pyg.image.load('assets/player/animation_bas/bas_1.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(-24, 0)

        self.import_player_assets()
        self.status = 'down'
        self.frame_index = 0
        self.animation_speed = 0.15

        self.direction = pyg.math.Vector2()
        self.speed = 5

        self.attaque = False
        self.attaque_cooldown = 400 # en millisecond
        self.attaque_time = None

        self.sprites_barriere = sprites_barriere

    def import_player_assets(self):
        chemin_perso = 'assets/player/'
        self.animations = {
            'haut':[], 'bas':[], 'droite':[],'gauche':[],
        }

        for animation in self.animations.keys():
            full_path = chemin_perso + animation
            self.animations[animation] = import_fichier(full_path)

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

    def get_status(self):

		# idle
        if self.direction.x == 0 and self.direction.y == 0:
            if not 'idle' in self.status and not 'attack' in self.status:
                self.status = self.status + '_idle'

        if self.attacking:
            self.direction.x = 0
            self.direction.y = 0
            if not 'attack' in self.status:
                if 'idle' in self.status:
                    self.status = self.status.replace('_idle','_attack')
                else:
                    self.status = self.status + '_attack'
        else:
            if 'attack' in self.status:
                self.status = self.status.replace('_attack','')

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

    def animate(self):
	    animations = self.animations[self.status]
 
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)

    def update(self):
        self.input()
        self.cooldowns()
        self.get_status()
        self.animate()
        self.deplacement(self.speed)