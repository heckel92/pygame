import pygame

pygame.init()

pygame.display.set_caption("monpremier jeux")
screen = pygame.display.set_mode((1080,720))

background = pygame.image.load('assets/bg.jpg')
running=True

while running:
    screen.blit(background,(0,0))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            pygame.quit()
            print("fermeture du jeux")
