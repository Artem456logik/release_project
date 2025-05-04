import pygame
from random import randint
import random
import time
WIDTH = 1200
HEIGHT = 650
SIZE = (WIDTH, HEIGHT)
FPS = 60
Score = 0
Life = 1

pygame.init()

cursor_img = pygame.transform.scale(
    pygame.image.load("pricel.png"),
    (75,75)
)


pygame.mouse.set_visible(False)
cursor_img_rect = cursor_img.get_rect()

bloodstn = pygame.transform.scale(
    pygame.image.load("bloodstn-removebg-preview.png"),
    (50,50)
)

window = pygame.display.set_mode(SIZE)
background = pygame.transform.scale(
    pygame.image.load("background.jpg"),
    SIZE)
gameoverbg = pygame.transform.scale(
    pygame.image.load("endgame.png"),
    SIZE)
victorybg = pygame.transform.scale(
    pygame.image.load("Win.jpg"),
    SIZE
)
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
        self.timer = randint(2,3)
    def update(self):
        self.timer -= 1

bombs = pygame.sprite.Group()

enemy = Enemy("enemy.png", (70,50), (random.randint(50, WIDTH-50), 125), random.randint(1,3))
for i in range(20):
    new_bomb = GameSprite("bombC4.png", (70,50), (random.randint(100, WIDTH-50), random.randint(25,495)), 0)
    while pygame.sprite.spritecollideany(new_bomb,bombs) and pygame.sprite.collide_rect(new_bomb,enemy):
        new_bomb = GameSprite("bombC4.png", (70,50), (random.randint(100, WIDTH-50), random.randint(0,495)), 0)
    bombs.add(new_bomb)


game = True
finish = False
restart = False
starttime = time.time()
currenttime = starttime
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if enemy.rect.collidepoint(event.pos):
                enemy.kill()
                enemy = Enemy("enemy.png", (70,50), (random.randint(50, WIDTH-50), 125), random.randint(1,3))
                Score += 1
    if not finish and not restart:
        window.blit(background, (0,0))
        cursor_img_rect.center = pygame.mouse.get_pos()
        window.blit(cursor_img, cursor_img_rect) 
        enemy.reset(window)
        bombs.draw(window)
        newtime = time.time()
        score_text = medium_font.render("Збито " + str(Score), True, (255,255,255))
        timer_text = medium_font.render("Лишилося: " + str(enemy.timer), True, (255,0,0))
        lifes_text = medium_font.render("Життя " + str(Life), True, (255,255,0))
        victory_text = medium_font.render("Перемога", True, (247,255,0))
        window.blit(score_text, (25,50))
        window.blit(timer_text, enemy.rect)
        window.blit(lifes_text, (25,25))
        if Score >= 10:
            finish = True
            window.blit(victorybg, (0,0))
            window.blit(victory_text, (500,25))
        if newtime - currenttime >= 1:
            enemy.update()
            timer_text = medium_font.render("Лишилося:" + str(enemy.timer), True, (255,255,255))
            currenttime = newtime
        if enemy.timer <= 0:
            finish = True
            window.blit(gameoverbg, (0,0))
    if restart:
        pass


    pygame.display.update()
    clock.tick(FPS)