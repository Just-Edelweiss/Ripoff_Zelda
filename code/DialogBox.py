import pygame

class DialogBox:
    def __init__(self):
        self.box = pygame.image.load('assets/boite_dialog.png')
        self.box = pygame.transform.scale(self.box, (700,100))
    def affiche_boite(self,screen):
        screen.blit(self.box,(120,480))
