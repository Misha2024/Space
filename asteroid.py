import pygame
import random


class Asteroid(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.image = pygame.image.load('graphics/asteroids.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = -self.rect.height
        self.speed = random.randint(2, 5)

        self.asteroids_group = pygame.sprite.Group()

    def update(self):
        self.rect.y += self.speed