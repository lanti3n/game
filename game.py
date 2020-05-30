import pygame
from player import Player
from monster import Monster

#crere une seconde classe qui va representer le jeu

class Game:

    def __init__(self):
        #definir si le jeu a commencer
        self.is_playing = False
        #genere le joueur, on cree un groupe Sprite de joueur 
        #car c la seule solution pour gerer les collisions lorsque le monstre entre en collision avec le joueur
        #spritecollide ne peut que comparer une entite avec un groupe d entite
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        #groupe de monster
        self.all_monster = pygame.sprite.Group()
        self.pressed = {}
        self.over = pygame.mixer.Sound('assets/sounds/game_over.ogg')


    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()

    def game_over(self):
        #remettre le jeu a neuf, retirer les monstres, remettre le joueur a 100 de vie et remettre le jeu en attente
        self.all_monster = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False
        self.over.play()

    def update(self, screen):
           #appliquer l image du joueur
        screen.blit(self.player.image, self.player.rect)

        #actualiser la barre de vie du joueur
        self.player.update_health_bar(screen)

        #recuperer les projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        #recuperer les monstres du jeu
        for monster in self.all_monster:
            monster.forward()
            monster.update_health_bar(screen)

        #appliquer l ensemble des images de mon groupe de projectiles
        self.player.all_projectiles.draw(screen)

        #appliquer l'ensemble des images du group de monster
        self.all_monster.draw(screen)

        #verifier si le joueur souhaite aller a gauche ou a droite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0 :
            self.player.move_left()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        self.all_monster.add(Monster(self))