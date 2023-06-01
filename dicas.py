import pygame
from imports import clique

pygame.init()

class Dica(pygame.sprite.Sprite):

    # ADICIONAR PARÂMETRO PARA IMAGEM 

    def __init__(self):
        super().__init__()
        self.botao = pygame.Surface((80,42))
        self.dica = pygame.Surface((1080, 475))
        self.image = self.botao
        self.rect = self.image.get_rect()

        self.mouse_pressionado = False
        
    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        self.image.fill('white')

        if self.image == self.botao:
            self.rect = self.image.get_rect()
            self.rect.topleft = (29, 16)
            if self.rect.collidepoint(mouse_pos):
                if pygame.mouse.get_pressed()[0]:
                    self.mouse_pressionado = True
                else:
                    if self.mouse_pressionado:
                        self.mouse_pressionado = False
                        self.image = self.dica
                
                        
        elif self.image == self.dica:
            self.rect = self.image.get_rect()
            self.rect.topleft = (0, 72)
            if self.rect.collidepoint(mouse_pos):
                if pygame.mouse.get_pressed()[0]:
                    self.mouse_pressionado = True
                else:
                    if self.mouse_pressionado:
                        self.mouse_pressionado = False
                        self.image = self.botao

dica_pergunta_1 = Dica()
dicas_group = pygame.sprite.Group()
dicas_group.add(dica_pergunta_1)