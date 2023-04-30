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
placar_txt = pygame.font.Font('Resources/Fonts/Half_Bold_Pixel-7/HalfBoldPixel7-2rw3.ttf', 24)

# TEXTO

jogar_novamente = dificuldades.render('Tela inicial', True, ROSA)

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


# ASSETS

## BOTAO

botao_ativo = pygame.image.load('Resources/Sprites/botao_ativo.png')
botao_inativo = pygame.image.load('Resources/Sprites/botao_inativo.png')

## BACKGROUND

pergunta_1 = ajusta_video('pergunta_1')
pergunta_2 = ajusta_video('pergunta_2')
pergunta_3 = ajusta_video('pergunta_3')
pergunta_4 = ajusta_video('pergunta_4')
pergunta_5 = ajusta_video('pergunta_5')
pergunta_6 = ajusta_video('pergunta_6')
pergunta_7 = ajusta_video('pergunta_7')
pergunta_8 = ajusta_video('pergunta_8')
pergunta_9 = ajusta_video('pergunta_9')
pergunta_10 = ajusta_video('pergunta_10')
pergunta_11 = ajusta_video('pergunta_11')
pergunta_12 = ajusta_video('pergunta_12')


class Placar:
    def __init__(self, pontos):
        self.pontos = pontos

    def soma_pontos(self):
        self.pontos += 1

    def mostra_placar(self, tela, posicao_x, posicao_y):
        placar_surf = secondary.render(f'{self.pontos}', False, BRANCO)
        tela.blit(placar_surf, (posicao_x, posicao_y))


placar = Placar(0)


class BotaoInicial:
    def __init__(self, x, y, imagem):
        self.imagem = imagem
        self.rect = self.imagem.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def mostra_botao(self):
        posicao_mouse = pygame.mouse.get_pos()
        clicked = False

        if botao_play.rect.collidepoint(posicao_mouse):
            self.imagem = botao_ativo
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                clicked = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        else:
            self.imagem = botao_inativo
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        screen.blit(self.imagem, (self.rect.x, self.rect.y))
        return clicked


botao_play = BotaoInicial(435, 435, botao_inativo)


class BotaoGeral:
    def __init__(self, x, y, text, cor):
        self.text = text
        self.cor = cor
        self.dificuldade = dificuldades.render(text, True, cor)
        self.x = x
        self.y = y
        self.rect = self.dificuldade.get_rect()
        self.rect.topleft = (self.x, self.y)

        self.clicked = False


    def mostra_botao(self, surface):
        posicao_do_mouse = pygame.mouse.get_pos()
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        clicked = False
        if self.rect.collidepoint(posicao_do_mouse):
            self.cor = ROSA
            self.dificuldade = dificuldades.render(self.text, True, self.cor)
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                clicked = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        else:
            self.cor = BRANCO
            self.dificuldade = dificuldades.render(self.text, True, self.cor)

        surface.blit(self.dificuldade, (self.x, self.y))
        return clicked


facil = BotaoGeral(249, 326, 'Easy', BRANCO)
medio = BotaoGeral(454, 326, 'Medium', BRANCO)
dificil = BotaoGeral(708, 326, 'Hard', BRANCO)
jogar_novamente = BotaoGeral(screen.get_width()/2 - jogar_novamente.get_width()/2, screen.get_height()/2 + 46, 'Jogar novamente', BRANCO)


class Pergunta:
    def __init__(self, background, a, b, c, d, alternativa_correta, cor):
        self.x = 154
        self.y_a = 562
        self.y_b = 598
        self.y_c = 634
        self.y_d = 670
        self.background = background
        self.cor = cor

        self.texto_a = a
        self.texto_b = b
        self.texto_c = c
        self.texto_d = d

        self.alternativa_a = self.texto_a
        self.alternativa_a_surface = alternativas.render(self.alternativa_a, False, self.cor)
        self.alternativa_a_rect = self.alternativa_a_surface.get_rect(topleft=(self.x, self.y_a))

        self.alternativa_b = self.texto_b
        self.alternativa_b_surface = alternativas.render(self.alternativa_b, False, self.cor)
        self.alternativa_b_rect = self.alternativa_b_surface.get_rect(topleft=(self.x, self.y_b))

        self.alternativa_c = self.texto_c
        self.alternativa_c_surface = alternativas.render(self.alternativa_c, False, self.cor)
        self.alternativa_c_rect = self.alternativa_c_surface.get_rect(topleft=(self.x, self.y_c))

        self.alternativa_d = self.texto_d
        self.alternativa_d_surface = alternativas.render(self.alternativa_d, False, self.cor)
        self.alternativa_d_rect = self.alternativa_d_surface.get_rect(topleft=(self.x, self.y_d))

        self.alternativas_text = [self.texto_a, self.texto_b, self.texto_c, self.texto_d]
        self.alternativas_rect = [self.alternativa_a_rect, self.alternativa_b_rect, self.alternativa_c_rect, self.alternativa_d_rect]
        self.alternativas_surface = [self.alternativa_a_surface, self.alternativa_b_surface, self.alternativa_c_surface, self.alternativa_d_surface]

        self.alternativa_correta = alternativa_correta
        self.clicked = True
        self.acertou = False

    def mostra_bg(self, tela):
        frame = self.background.get_frame(pygame.time.get_ticks() / 1000)
        surface = pygame.surfarray.make_surface(frame)
        tela.blit(surface, (0, 0))

    def mostra_alternativas(self, tela):
        tela.blit(self.alternativa_a_surface, self.alternativa_a_rect)
        tela.blit(self.alternativa_b_surface, self.alternativa_b_rect)
        tela.blit(self.alternativa_c_surface, self.alternativa_c_rect)
        tela.blit(self.alternativa_d_surface, self.alternativa_d_rect)

    def checa_interacoes(self):
        posicao_mouse = pygame.mouse.get_pos()
        clicked = False

        if self.alternativa_a_rect.collidepoint(posicao_mouse):
            self.cor = ROSA
            self.alternativa_a_surface = alternativas.render(self.texto_a, False, self.cor)
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                clicked = True
                if self.alternativa_correta == 'A':
                    placar.soma_pontos()
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        else:
            self.cor = BRANCO
            self.alternativa_a_surface = alternativas.render(self.texto_a, False, self.cor)

        if self.alternativa_b_rect.collidepoint(posicao_mouse):
            self.cor = ROSA
            self.alternativa_b_surface = alternativas.render(self.texto_b, False, self.cor)
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                clicked = True
                if self.alternativa_correta == 'B':
                    placar.soma_pontos()
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
                clicked = False
        else:
            self.cor = BRANCO
            self.alternativa_b_surface = alternativas.render(self.texto_b, False, self.cor)
        #
        if self.alternativa_c_rect.collidepoint(posicao_mouse):
            self.cor = ROSA
            self.alternativa_c_surface = alternativas.render(self.texto_c, False, self.cor)
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                clicked = True
                if self.alternativa_correta == 'C':
                    placar.soma_pontos()
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
                clicked = False
        else:
            self.cor = BRANCO
            self.alternativa_c_surface = alternativas.render(self.texto_c, False, self.cor)
        #
        if self.alternativa_d_rect.collidepoint(posicao_mouse):
            self.cor = ROSA
            self.alternativa_d_surface = alternativas.render(self.texto_d, False, self.cor)
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                clicked = True
                if self.alternativa_correta == 'D':
                    placar.soma_pontos()
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
                clicked = False
        else:
            self.cor = BRANCO
            self.alternativa_d_surface = alternativas.render(self.texto_d, False, self.cor)
        return clicked
# Telas


tela_inicial = ajusta_video('tela_inicial_bg')
tela_dificuldade = ajusta_video('tela_dificuldade_bg')
tela_final = pygame.surface.Surface((1080, 720))
tela_final.fill(PRETO)


primeira_pergunta = Pergunta(pergunta_1,
                             '(A) Horse',
                             '(B) Mustang',
                             '(C) Cavallo',
                             '(D) Yegua',
                             'A',
                             BRANCO)
segunda_pergunta = Pergunta(pergunta_2,
                            "(A) Three o'clock",
                            "(B) One o'clock",
                            "(C) Six o'clock",
                            "(D) Eight o'clock",
                            'D',
                            BRANCO)
terceira_pergunta = Pergunta(pergunta_3,
                             "(A) Two",
                             "(B) Seven",
                             "(C) Five",
                             "(D) Ten",
                             "C",
                             BRANCO)
quarta_pergunta = Pergunta(pergunta_4,
                           "(A) Thirteen",
                           "(B) Thirty",
                           "(C) Ten Three",
                           "(D) Three Ten",
                           'A',
                           BRANCO)
quinta_pergunta = Pergunta(pergunta_5,
                           "(A) Book, Time, Door, Shirt",
                           "(B) Book, Clock, Door, Shoe",
                           "(C) Shoe, Door, Clock, Book ",
                           "(D) Shoe, Shirt, Book, Door",
                           'B',
                           BRANCO)
sexta_pergunta = Pergunta(pergunta_6,
                          "(A) Yellow",
                          "(B) Blue",
                          "(C) Purple",
                          "(D) Red",
                          'D',
                          BRANCO)
setima_pergunta = Pergunta(pergunta_7,
                           "(A) White",
                           "(B) Green",
                           "(C) Red",
                           "(D) Purple",
                           'B',
                           BRANCO)
oitava_pergunta = Pergunta(pergunta_8,
                           "(A) Bear",
                           "(B) Snake",
                           "(C) Whale",
                           "(D) Wolf",
                           'D',
                           BRANCO)
nona_pergunta = Pergunta(pergunta_9,
                         "(A) Thair",
                         "(B) These",
                         "(C) Those",
                         "(D) That",
                         'C',
                         BRANCO)
decima_pergunta = Pergunta(pergunta_10,
                           "(A) Their",
                           "(B) This",
                           "(C) Thers",
                           "(D) Thei",
                           'A',
                           BRANCO)
decimaprim_pergunta = Pergunta(pergunta_11,
                                "(A) Pineapple, Pumpkin, Avocado, Banana",
                                "(B) Apple, Orange, Lemon, Watermelon",
                                "(C) Pumpkin, khaki, Lemon, Apple",
                                "(D) Apple, Orange, Guava, Papaya",
                                'B',
                                BRANCO)
decimaseg_pergunta = Pergunta(pergunta_12,
                              "(A) Purple - Yellow",
                              "(B) Blue - Green",
                              "(C) Yellow - Purple",
                              "(D) Black - Orange",
                              'B',
                              BRANCO)

# LISTAS DE PERGUNTAS

perguntas_faceis = [primeira_pergunta, segunda_pergunta, terceira_pergunta, quarta_pergunta]
perguntas_medias = [quinta_pergunta, sexta_pergunta, setima_pergunta, oitava_pergunta]
perguntas_dificeis = [nona_pergunta, decima_pergunta, decimaprim_pergunta, decimaseg_pergunta]


def pinta_tela(tela):
    frame = tela.get_frame(pygame.time.get_ticks() / 1000)
    return pygame.surfarray.make_surface(frame)


fase = tela_inicial
numero = 0
clock = pygame.time.Clock()
while True:

    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    if fase == tela_inicial:
        placar.pontos = 0
        surf = pinta_tela(fase)
        screen.blit(surf, (0, 0))

        if botao_play.mostra_botao():
            fase = tela_dificuldade

    if fase == tela_dificuldade:
        surf = pinta_tela(fase)
        screen.blit(surf, (0, 0))

        if facil.mostra_botao(screen):
            fase = perguntas_faceis

        if medio.mostra_botao(screen):
            fase = perguntas_medias

        if dificil.mostra_botao(screen):
            fase = perguntas_dificeis

    if fase == perguntas_faceis:
        perguntas_faceis[numero].mostra_bg(screen)
        perguntas_faceis[numero].mostra_alternativas(screen)
        if perguntas_faceis[numero].checa_interacoes():
            numero += 1
        if numero > 3:
            fase = tela_final
            numero = 0
        placar.mostra_placar(screen, 1000, 700)

    if fase == perguntas_medias:
        perguntas_medias[numero].mostra_bg(screen)
        perguntas_medias[numero].mostra_alternativas(screen)
        if perguntas_medias[numero].checa_interacoes():
            numero += 1
        if numero > 3:
            fase = tela_final
            numero = 0
        placar.mostra_placar(screen, 1000, 700)

    if fase == perguntas_dificeis:
        perguntas_dificeis[numero].mostra_bg(screen)
        perguntas_dificeis[numero].mostra_alternativas(screen)
        if perguntas_dificeis[numero].checa_interacoes():
            numero += 1
        if numero > 3:
            fase = tela_final
            numero = 0
        placar.mostra_placar(screen, 1000, 700)

    if fase == tela_final:
        screen.fill('black')
        placar.mostra_placar(screen, screen.get_width()/2, screen.get_height()/2)
        if jogar_novamente.mostra_botao(screen):
            numero = 0
            fase = tela_inicial
    pygame.display.update()
