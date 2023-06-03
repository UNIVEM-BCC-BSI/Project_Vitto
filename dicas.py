import pygame
from imports import clique

pygame.init()

imagem_dica_1 = pygame.image.load('images/dica_pergunta_1.png')
imagem_dica_2 = pygame.image.load('images/dica_pergunta_2.png')
imagem_dica_3 = pygame.image.load('images/dica_pergunta_3.png')
imagem_dica_4 = pygame.image.load('images/dica_pergunta_4.png')
imagem_dica_5 = pygame.image.load('images/dica_pergunta_5.png')
imagem_dica_6 = pygame.image.load('images/dica_pergunta_6.png')
imagem_dica_7 = pygame.image.load('images/dica_pergunta_7.png')
imagem_dica_8 = pygame.image.load('images/dica_pergunta_8.png')

dica = pygame.font.Font(None, 26)
dica_txt_surface = dica.render('DICA', False, 'black')
dica_rect = dica_txt_surface.get_rect(center=(40, 21))

fechar_dica_surface = dica.render('(aperte aqui para fechar)', False, 'black')
fechar_dica_rect = fechar_dica_surface.get_rect(center=(540, 443))

class Dica(pygame.sprite.Sprite):

    # ADICIONAR PARÂMETRO PARA IMAGEM 

    def __init__(self, imagem):
        super().__init__()
        self.botao = pygame.Surface((80,42))
        self.dica = pygame.Surface((1080, 475))
        self.image = self.botao
        self.rect = self.image.get_rect()

        self.txt_dica = imagem

        self.mouse_pressionado = False
        
    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        self.image.fill('white')

        if self.image == self.botao:
            self.rect = self.image.get_rect()
            self.rect.topleft = (29, 16)
            self.image.blit(dica_txt_surface, dica_rect)
            if self.rect.collidepoint(mouse_pos):
                if pygame.mouse.get_pressed()[0]:
                    self.mouse_pressionado = True
                else:
                    
                    if self.mouse_pressionado:
                        clique.play()
                        self.mouse_pressionado = False
                        self.image = self.dica
                
                        
        elif self.image == self.dica:
            self.rect = self.image.get_rect()
            self.rect.topleft = (0, 72)
            self.image.blit(self.txt_dica, (0, 0))
            self.image.blit(fechar_dica_surface, fechar_dica_rect)
            if self.rect.collidepoint(mouse_pos):
                if pygame.mouse.get_pressed()[0]:
                    self.mouse_pressionado = True
                else:
                    
                    if self.mouse_pressionado:
                        clique.play()
                        self.mouse_pressionado = False
                        self.image = self.botao


dica_pergunta_1 = Dica(imagem_dica_1)
dica_pergunta_2 = Dica(imagem_dica_2)
dica_pergunta_3 = Dica(imagem_dica_3)
dica_pergunta_4 = Dica(imagem_dica_4)
dica_pergunta_5 = Dica(imagem_dica_5)
dica_pergunta_6 = Dica(imagem_dica_6)
dica_pergunta_7 = Dica(imagem_dica_7)
dica_pergunta_8 = Dica(imagem_dica_8)

dicas = [dica_pergunta_1, dica_pergunta_2, dica_pergunta_3,
         dica_pergunta_4, dica_pergunta_5, dica_pergunta_6,
         dica_pergunta_7, dica_pergunta_8]

dicas_group = pygame.sprite.Group()
dicas_group.add(dica_pergunta_1)

def muda_dica(pergunta_atual):
    dicas_group.remove(all)
    dicas_group.add(dicas[pergunta_atual])