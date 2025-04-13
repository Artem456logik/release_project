import pygame
from random import randint
import random
import time
WIDTH = 1200
HEIGHT = 650
SIZE = (WIDTH, HEIGHT)
FPS = 60


window = pygame.display.set_mode(SIZE)
background = pygame.transform.scale(
    pygame.image.load("background.jpg"),
    SIZE)
pygame.display.set_caption("ШУТЕР 2Д")
clock = pygame.time.Clock()

pygame.font.init()
medium_font = pygame.font.SysFont("Helvetica", 24)
big_font = pygame.font.SysFont("Impact", 50)


pygame.mixer.init()

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, filename:str, size:tuple[int,int], coords: tuple[int,int], speed:int):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(filename), size)
        self.rect = self.image.get_rect(center=coords)
        self.speed = speed

    def reset(self, window:pygame.Surface):
        window.blit(self.image, self.rect)

class Enemy(GameSprite):
    def __init__(self, filename: str, size: tuple[int, int], coords: tuple[int, int], speed: int):
        super().__init__(filename, size, coords, speed )
        self.timer = randint(5,8)
    def update(self):
        self.timer -= 1

enemy = Enemy("enemy.png", (70,50), (random.randint(50, WIDTH-50), 125), random.randint(1,3))


game = True
finish = False
restart = False
starttime = time.time()
currenttime = starttime
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    if not finish and not restart:
        window.blit(background, (0,0))
        enemy.reset(window)
        newtime = time.time()
        if newtime - currenttime >= 1:
            enemy.update()
    if restart:
        pass
    

    pygame.display.update()
    clock.tick(FPS)