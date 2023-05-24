import pygame
from imports import *

pygame.init()
screen = pygame.display.set_mode((1280, 720))

texto = pygame.font.Font(None, 60)
teste = texto.render('00:00', False, 'white')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.fill('black')
    #CORACAO & RELOGIO
    screen.blit(relogio, (20, 20))
    screen.blit(teste, (80, 27))

    screen.blit(coracao, (1200, 650))
    screen.blit(coracao, (1155, 650))
    screen.blit(coracao, (1110, 650))
    screen.blit(coracao, (1065, 650))
    screen.blit(coracao, (1020, 650))

    pygame.display.update()