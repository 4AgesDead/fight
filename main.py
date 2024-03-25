import pygame
import os
import sys
import random

pygame.init()
current_path = os.path.dirname(__file__)
os.chdir(current_path)
WIDTH = 1200
HEIGHT = 800
FPS = 60
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
lvl = 'menu'
lvl_game = 1
score = 0
font = pygame.font.SysFont('aria', 40)

from load import *

def game():
    sc.fill('grey')
    backgroud.update()
    pygame.display.update()
class BackGroud:
    def __init__(self):
        self.timer = 0
        self.frame = 0
        self.image = backgroud_image
    def update(self):
        self.timer +=2
        sc.blit(self.image[self.frame], (0,0))
        if self.timer / FPS > 0.1:
            self.frame = 0
        else:
            self.frame += 1
        self.timer = 0
class Player_1(pygame.sprite.Sprite):
    def __init__(self,image_lists):
        pygame.sprite.Sprite.__init__(self)
        self.image_lists =image_lists
        self.image = self.image_lists['idle'][0]
        self.currect_list_image = self.image_lists['idle']
        self.rect =self.image.get_rect()
        self.anime_idle = True
        self.anime_run = False
        self.anime_atk = False
        self.frame = 0
        self.timer_anime = 0
        self.dir  = 'right'
        self.hp = 100
        self.jump_step = -20
        self.jump = False
        self.flag_damage =False
        self.mask = pygame.mask.from_surface(self.image)
        self.mask_list =[]
        self.rect.center = (200, 380)
        self.hp_bar = 'blue'
        self.key = pygame.key.get_pressed()
    def move(self):
        if self.key[pygame.K_d]:
            self.rect.x += 2
            self.anime_idle = False
            if not self.anime_run:
                self.anime_run = True
        elif self.key[pygame.K_a]:
            self.rect.x -= 2
            self.anime_idle = False
            if not self.anime_atk:
                self.anime_run = True
        else:
            if not self.anime_atk:
                self.anime_idle = True
            self.anime_run = False


def restart():
    global  backgroud
    backgroud =BackGroud()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    game_lvl()
    clock.tick(FPS)
