import pygame
import random

#creer une classe qui va gerer la notion de monstre sur notre jeu
class Monster(pygame.sprite.Sprite):
#monster herite de la classe sprite comme element graphique
    def __init__(self, game):
        #appelle de la classe sprite pour la charger lors de la creation du monstre
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540
        self.velocity = random.randint(1,3)


    def damage(self, amount):
        #infliger les degats
        self.health -= amount

        #verifier si le nb de point de vie est inf ou egal a 0
        if self.health <= 0:
            #reapparaitre comme un nouveau monstre
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1,3)
            self.health = self.max_health

    def update_health_bar(self, surface):
        # definition de la couleur de jauge de vie (vert clair) couleur code RGB voir https://htmlcolorcodes.com/fr/
        #bar_color = (111, 210, 46)
        #def de la couleur d arriere plan de la jauge
        #back_bar_color = (60, 60, 60)

        #definir la position de la jauge de vie, largeur et epaisseur
        #bar_position = [x, y, width, height]
        #bar_position = [self.rect.x + 10, self.rect.y -20, self.health, 5]
        #def de la position de l arriere plan de la jauge de vie
        #back_bar_position = [self.rect.x + 10, self.rect.y -20, self.max_health, 5]

        #dessin de larriere plan de barre de vie
        pygame.draw.rect(surface, (60, 60, 60), [self.rect.x + 10, self.rect.y -20, self.max_health, 5])
        #dessin de la barre de vie
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y -20, self.health, 5])


    def forward(self):
        #le deplacement se fait que s il n'y a pas de collision avec un group de joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        #si le monstre est en collision avec le joueur
        else:
            #ingliger des degats au joueur
            self.game.player.damage(self.attack)