import pygame
import random

#creer une classe qui va gerer la notion de comet sur notre jeu
class Comet(pygame.sprite.Sprite):
#Comet herite de la classe sprite comme element graphique
    def __init__(self, game):
        #appelle de la classe sprite pour la charger lors de la creation de la Comet
        super().__init__()
        self.game = game
        self.attack = 10
        self.image = pygame.image.load('assets/comet.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 1000)
        self.rect.y = 0
        self.velocity = random.randint(1,3)

    def down(self):
        #le deplacement se fait que s il n'y a pas de collision avec un group de joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.y += self.velocity
        #si la comet est en collision avec le joueur
        else:
            #ingliger des degats au joueur
            self.game.player.damage(self.attack)
            #suppression de la comet
            self.rect.x = random.randint(0, 1000)
            self.rect.y = 0
            self.velocity = random.randint(1,3)
        
        #print(self.rect.y)

        #verifier si la comet n'est plus present a l ecran
        if self.rect.y >= 500:
           #reinitialiser le projectile
           self.rect.x = random.randint(0, 1000)
           self.rect.y = 0
           print('comet reinit !')
