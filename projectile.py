import pygame

# definir la classe qui va gerer le projectile du joueur
class Projectile(pygame.sprite.Sprite):

    #definir le contructeur de cette classe
    def __init__(self, player):
        super().__init__()
        self.velocity = 5
        self.player = player
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + (player.image.get_width()/2)
        self.origine_image = self.image
        self.angle = 0

    def rotate(self):
        #tourner le projectile
        self.angle += 8
        self.image = pygame.transform.rotozoom(self.origine_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        # verifier si le projectile entre en collision avec un monstre
        for monster in self.player.game.check_collision(self, self.player.game.all_monster):
            #supprimer le projectile
            self.remove()
            #infliger des degats
            monster.damage(self.player.attack)

        #verifier si notre projectile n'est plus present a l ecran
        if self.rect.x > 1080:
            #supprimer le projectile
            self.remove()
            print('projectile supprimer !')