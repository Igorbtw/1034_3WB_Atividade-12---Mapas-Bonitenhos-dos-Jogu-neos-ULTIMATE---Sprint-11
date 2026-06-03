import pygame, sys
from pygame.locals import QUIT

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Hello World!')
clock = pygame.time.Clock()
tile_size = 60
tile_size_joguinho = 64
tileset = pygame.image.load("plataform_tileset.png")
collider_caixa = pygame.Rect(0, 0, 0, 0)
can_walk = True