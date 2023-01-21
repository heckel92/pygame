import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health=100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.image = pygame.image.load('assets/starship.png')
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 300