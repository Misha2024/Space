import pygame
import random


class Asteroid(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height, n):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.images = [pygame.image.load('graphics/asteroid 3.png'), pygame.image.load('graphics/asteroid 2.png'),
                       pygame.image.load(
                           'graphics/asteroid 1.png')]
        self.image = self.images[n]
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = -self.rect.height
        self.speed = random.randint(2, 5)
        self.asteroids_group = pygame.sprite.Group()

    def update(self):
        self.rect.y += self.speed


class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen_width):
        super().__init__()
        self.image = pygame.image.load('graphics/enemy.png')
        self.screen_width = screen_width
        x = random.choice([0, screen_width - self.image.get_width()])
        if x == 0:
            self.speed = 5
        else:
            self.speed = -5
        self.rect = self.image.get_rect(topleft=(x, 40))
        self.bullets_group = pygame.sprite.Group()
        self.bullets_ready = True
        self.bullets_time = 0

    def update(self):
        self.rect.x += self.speed
        if self.rect.right > self.screen_width:
            self.kill()
        elif self.rect.left < 0:
            self.kill()
