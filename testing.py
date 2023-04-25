import pygame
from moviepy.editor import VideoFileClip
from moviepy.video.fx import all as vfx

pygame.init()
WINDOW_SIZE = (1080, 720)
screen = pygame.display.set_mode(WINDOW_SIZE)

# CORES

BRANCO = (255, 255, 255)
ROSA = (255, 0, 157)
PRETO = (0, 0, 0)

# FONTES

dificuldades = pygame.font.Font('Resources/Fonts/ConnectionII/ConnectionII.otf', 46)
alternativas = pygame.font.Font('Resources/Fonts/ConnectionII/ConnectionII.otf', 24)
secondary = pygame.font.Font('Resources/Fonts/Diary_Of_An_8bit_Mage/Diary of an 8-bit mage.otf', 16)

# TEXTO

easy_inativo = dificuldades.render('Easy', True, BRANCO)
easy_ativo = dificuldades.render('Easy', True, ROSA)
medium = dificuldades.render('Medium', True, ROSA)
hard = dificuldades.render('Hard', True, ROSA)

def ajusta_video(fundo):
    clip = VideoFileClip('Resources/Sprites/' + fundo + '.mp4')
    clip = clip.loop()
    # Define a duração do clipe em segundos
    clip.set_duration(10)
    # Aplica o efeito de espelhamento horizontal e rotação no clipe
    clip = vfx.mirror_x(clip)
    clip = clip.fx(vfx.rotate, 90)
    return clip

def pinta_tela(clip):

    frame = clip.get_frame(pygame.time.get_ticks() / 1000)
    return pygame.surfarray.make_surface(frame)

# Tela Inicial

tela_inicial = ajusta_video('tela_inicial_bg')

tela_dificuldade = pygame.surface.Surface((1080,720))
tela_dificuldade.fill(PRETO)


pergunta_1 = ajusta_video('pergunta_1')
pergunta_2 = ajusta_video('pergunta_2')
pergunta_3 = ajusta_video('pergunta_3')
pergunta_4 = ajusta_video('pergunta_4')
pergunta_5 = ajusta_video('pergunta_5')

# Botoes

botao_ativo = pygame.image.load('Resources/Sprites/botao_ativo.png')
botao_inativo = pygame.image.load('Resources/Sprites/botao_inativo.png')

class BotaoInicial:
    def __init__(self, x, y, imagem):
        self.imagem = imagem
        self.rect = self.imagem.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def mostra_botao(self):
        posicao_mouse = pygame.mouse.get_pos()

        if botao_play.rect.collidepoint(posicao_mouse):
            self.imagem = botao_ativo
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        else:
            self.imagem = botao_inativo
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        screen.blit(self.imagem, (self.rect.x, self.rect.y))
        return self.clicked

botao_play = BotaoInicial(435, 435, botao_inativo)

class Dificuldade:
    def __init__(self, x, y, text, cor):
        self.text = text
        self.cor = cor
        self.dificuldade = dificuldades.render(text, True, cor)
        self.x = x
        self.y = y
        self.rect = self.dificuldade.get_rect()
        self.rect.topleft = (x, y)

        self.clicked = False


    def mostra_dificuldade(self, surface):
        posicao_do_mouse = pygame.mouse.get_pos()
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        if self.rect.collidepoint(posicao_do_mouse):
            self.cor = ROSA
            self.dificuldade = dificuldades.render(self.text, True, self.cor)
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        else:
            self.cor = BRANCO
            self.dificuldade = dificuldades.render(self.text, True, self.cor)

        surface.blit(self.dificuldade, (self.x, self.y))
        return self.clicked

facil = Dificuldade(229, 326, 'Easy', BRANCO)
medio = Dificuldade(414, 326, 'Medium', BRANCO)
dificil = Dificuldade(708, 326, 'Hard', BRANCO)

tela = tela_inicial

tela_facil = [pergunta_1, pergunta_2, pergunta_3, pergunta_4, pergunta_5]
tela_medio = []
tela_dificil = []
clock = pygame.time.Clock()
while True:

    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    if tela == tela_inicial:
        surf = pinta_tela(tela)
        screen.blit(surf, (0, 0))
        if botao_play.mostra_botao():
            tela = tela_dificuldade

    if tela == tela_dificuldade:
        screen.blit(tela_dificuldade, (0, 0))
        if facil.mostra_dificuldade(screen):
            tela = tela_facil
        if medio.mostra_dificuldade(screen):
            tela = tela_medio
        if dificil.mostra_dificuldade(screen):
            tela = tela_dificil

    if tela == tela_facil:
        surf = pinta_tela(tela_facil[0])
        screen.blit(surf, (0, 0))

    if tela == tela_medio:
        pass

    if tela == tela_dificil:
        pass

    pygame.display.update()
