import pygame
import math
from game import Game

pygame.init()


# creer la fenetre
pygame.display.set_caption("EID 2020 SIDOU GAME")
screen = pygame.display.set_mode((1080, 720))

# import, chargement de l arriere plan du jeu
background = pygame.image.load('assets/bg.jpg')

# importer la banniere
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
# math.ceil arondi a l entier suivant (import math)
banner_rect.x = math.ceil(screen.get_width() / 4)

# importer/charger le bouton pour lancer la partie
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)

#importer la musique on click
click = pygame.mixer.Sound('assets/sounds/click.ogg')
 
# charger notre jeu
game = Game()

running = True


# boucle tant que la condition running est vrai
while running:
  
    # appliquer l arriere plan
    screen.blit(background, (0, -200))

    # verifier si le jeu a commencer
    if game.is_playing:              
        # declencher les instructions de la partie via la methode update
        game.update(screen)
    # verifier si notre jeu n'a pas commencer
    else:
        # ajouter mon ecran de bienvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

     # mettre a jour l ecran
    pygame.display.flip()

    # si le joueur ferme la fenetre
    for event in pygame.event.get():
        # event est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
        # detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # detecter si la touche espace est enclencher pour lancer le projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # verification si la souris est en collision avec le bouton jouer
            if play_button_rect.collidepoint(event.pos):
                #click sound
                click.play()
                # mettre le jeu en mode lancer
                game.start()

                # en plus branche exo
