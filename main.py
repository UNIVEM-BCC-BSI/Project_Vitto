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

# VARIÁVEIS DO JOGO



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
pergunta_6 = ajusta_video('pergunta_6')
pergunta_7 = ajusta_video('pergunta_7')

animais = [pergunta_1]

numeros = [pergunta_2, pergunta_3, pergunta_4]

objetos = [pergunta_5]

cores = [pergunta_6, pergunta_7]

perguntas_tela = [pergunta_1, pergunta_2, pergunta_3, pergunta_4, pergunta_5, pergunta_6, pergunta_7]

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

tela_facil = perguntas_tela
tela_medio = []
tela_dificil = []

class Pergunta:
    def __init__(self, a, b, c, d, resposta_certa, cor):
        self.x = 154
        self.y_a = 562
        self.y_b = 598
        self.y_c = 634
        self.y_d = 670

        self.tela_atual = 0

        self.text_a = a
        self.text_b = b
        self.text_c = c
        self.text_d = d

        self.cor = cor

        self.a = alternativas.render(self.text_a, True, BRANCO)
        self.rect_a = self.a.get_rect()
        self.rect_a.topleft = (self.x, self.y_a)

        self.b = alternativas.render(self.text_b, True, BRANCO)
        self.rect_b = self.b.get_rect()
        self.rect_b.topleft = (self.x, self.y_b)

        self.c = alternativas.render(self.text_c, True, BRANCO)
        self.rect_c = self.c.get_rect()
        self.rect_c.topleft = (self.x, self.y_c)

        self.d = alternativas.render(self.text_d, True, BRANCO)
        self.rect_d = self.d.get_rect()
        self.rect_d.topleft = (self.x, self.y_d)

        self.clicked = False
        self.clicked_a = False
        self.clicked_b = False
        self.clicked_c = False
        self.clicked_d = False

        self.resposta_certa = resposta_certa
        self.acertou = False

    def mostra_alternativas(self, tela):
        mouse = pygame.mouse.get_pos()
        if self.rect_a.collidepoint(mouse):
            self.cor = ROSA
            self.a = alternativas.render(self.text_a, True, self.cor)
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False and self.resposta_certa == 'A':
                self.clicked = True
                self.clicked_a = True
                self.acertou = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        else:
            self.cor = BRANCO
            self.a = alternativas.render(self.text_a, True, self.cor)

        if self.rect_b.collidepoint(mouse):
            self.cor = ROSA
            self.b = alternativas.render(self.text_b, True, self.cor)
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False and self.resposta_certa == 'B':
                self.clicked = True
                self.clicked_b = True
                self.acertou = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        else:
            self.cor = BRANCO
            self.b = alternativas.render(self.text_b, True, self.cor)

        if self.rect_c.collidepoint(mouse):
            self.cor = ROSA
            self.c = alternativas.render(self.text_c, True, self.cor)
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False and self.resposta_certa == 'C':
                self.clicked_c = True
                self.clicked = True
                self.acertou = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        else:
            self.cor = BRANCO
            self.c = alternativas.render(self.text_c, True, self.cor)

        if self.rect_d.collidepoint(mouse):
            self.cor = ROSA
            self.d = alternativas.render(self.text_d, True, self.cor)
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False and self.resposta_certa == 'D':
                self.clicked_d = True
                self.clicked = True
                self.acertou = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        else:
            self.cor = BRANCO
            self.d = alternativas.render(self.text_d, True, self.cor)


        tela.blit(self.a, (self.x, 562))
        tela.blit(self.b, (self.x, 598))
        tela.blit(self.c, (self.x, 634))
        tela.blit(self.d, (self.x, 670))


pergunta_1_alternativas = Pergunta('(A) Horse', '(B) Mustang', '(C) Cavallo', '(D) Yegua', 'A', BRANCO)
pergunta_2_alternativas = Pergunta("(A) Three o'clock", "(B) One o'clock", "(C) Six o'clock", "(D) Eight o'clock", 'D', BRANCO)
pergunta_3_alternativas = Pergunta("(A) Two", "(B) Seven", "(C) Five", "(D) Ten", "C", BRANCO)
pergunta_4_alternativas = Pergunta("(A) Thirteen", "(B) Thirty", "(C) Ten Three", "(D) Three Ten", 'A', BRANCO)
pergunta_5_alternativas = Pergunta("(A) Book, Time, Door, Shirt", "(B) Book, Clock, Door, Shoe", "(C) Shoe, Door, Clock, Book ", "(D) Shoe, Shirt, Book, Door", 'B', BRANCO)
pergunta_6_alternativas = Pergunta("(A) Yellow", "(B) Blue", "(C) Purple", "(D) Red", 'D', BRANCO)
pergunta_7_alternativas = Pergunta("(A) White", "(B) Green", "(C) Red", "(D) Purple", 'B', BRANCO)

perguntas = [pergunta_1_alternativas, pergunta_2_alternativas, pergunta_3_alternativas, pergunta_4_alternativas, pergunta_5_alternativas, pergunta_6_alternativas, pergunta_7_alternativas]

tela_atual = 0
respostas_certas = 0
respostas_certas_surf = secondary.render(f'{respostas_certas}', False, BRANCO)
respostas_certas_rect = respostas_certas_surf.get_rect(topleft = (1000, 700))


def mostra_pontos(respostas_certas):
    respostas_certas_surf = secondary.render(f'{respostas_certas}', False, BRANCO)
    respostas_certas_rect = respostas_certas_surf.get_rect(topleft=(1000, 700))
    screen.blit(respostas_certas_surf, respostas_certas_rect)


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
        surf = pinta_tela(tela_facil[tela_atual])
        screen.blit(surf, (0, 0))
        perguntas[tela_atual].mostra_alternativas(screen)
        mostra_pontos(respostas_certas)
        if perguntas[tela_atual].clicked_a or perguntas[tela_atual].clicked_b or perguntas[tela_atual].clicked_c or perguntas[tela_atual].clicked_d:
            if perguntas[tela_atual].acertou:
                respostas_certas += 1

            if tela_atual < len(perguntas) - 1:
                tela_atual += 1

            else:
                screen.fill(PRETO)

    if tela == tela_medio:
        pass

    if tela == tela_dificil:
        pass

    pygame.display.update()