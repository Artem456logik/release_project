import pygame
from random import randint

WIDTH = 1200
HEIGHT = 650
SIZE = (WIDTH, HEIGHT)
FPS = 60


window = pygame.display.set_mode(SIZE)
background = pygame.transform.scale(
    pygame.image.load("background.jpg"),
    SIZE)
pygame.display.set_caption("Назва проекту. Автор: ....")
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


game = True
finish = False
restart = False

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False


    if not finish and not restart:
        window.blit(background, (0,0))


    if restart:
        pass
    
    pygame.display.update()
    clock.tick(FPS)