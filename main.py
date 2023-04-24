import pygame
from moviepy.editor import VideoFileClip
from moviepy.video.fx import all as vfx


pygame.init()
WINDOW_SIZE = (1080, 720)
screen = pygame.display.set_mode(WINDOW_SIZE)

# FONTES

connection = pygame.font.Font('Resources/Fonts/ConnectionII/ConnectionII.otf', 21)
secondary = pygame.font.Font('Resources/Fonts/Diary_Of_An_8bit_Mage/Diary of an 8-bit mage.otf', 16)

# CORES

BRANCO = (255, 255, 255)
ROSA = (255, 0, 157)

class TelaInicial:
    def __init__(self, fundo):
        self.fundo = fundo
        self.botao_inativo = pygame.image.load('Resources/Sprites/botao_inativo.png')
        self.botao_ativo = pygame.image.load('Resources/Sprites/botao_ativo.png')
        self.botao = self.botao_inativo

    def ajusta_video(self):
        clip = VideoFileClip('Resources/Sprites/' + self.fundo + '.mp4')
        clip = clip.loop()
        # Define a duração do clipe em segundos
        clip.set_duration(10)
        # Aplica o efeito de espelhamento horizontal e rotação no clipe
        clip = vfx.mirror_x(clip)
        clip = clip.fx(vfx.rotate, 90)
        self.fundo = clip

    def pinta_tela(self, canva):

        frame = self.fundo.get_frame(pygame.time.get_ticks() / 1000)
        surf = pygame.surfarray.make_surface(frame)
        surf.blit(self.botao, (435, 435))
        canva.blit(surf, (0, 0))

    def calcula_regra(self, posicao_do_mouse, evts):
        if 435 < posicao_do_mouse[0] < 635 and 435 < posicao_do_mouse[1] < 535:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            self.botao = self.botao_ativo
            if evts.type == pygame.MOUSEBUTTONUP and evts.button == 1:
                pass
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            self.botao = self.botao_inativo

class BgPergunta:
    def __init__(self, fundo):
        self.fundo = fundo

    def ajusta_video(self):
        clip = VideoFileClip('Resources/Sprites/' + self.fundo + '.mp4')
        clip = clip.loop()
        # Define a duração do clipe em segundos
        clip.set_duration(10)
        # Aplica o efeito de espelhamento horizontal e rotação no clipe
        clip = vfx.mirror_x(clip)
        clip = clip.fx(vfx.rotate, 90)
        self.fundo = clip

    def pinta_background(self, canva):
        frame = self.fundo.get_frame(pygame.time.get_ticks() / 1000)
        surf = pygame.surfarray.make_surface(frame)
        canva.blit(surf, (0, 0))

    def calcula_regra(self, posicao_do_mouse, evts):
        pass

class Pergunta:
    def __init__(self, a, b, c, d, resposta_certa):
        self.alternativa_A_inativo = connection.render(a, True, BRANCO)
        self.alternativa_A_ativo = connection.render(a, True, ROSA)
        self.alternativa_A = self.alternativa_A_inativo

        self.alternativa_B_inativo = connection.render(b, True, BRANCO)
        self.alternativa_B_ativo = connection.render(b, True, ROSA)
        self.alternativa_B = self.alternativa_B_inativo

        self.alternativa_C_inativo = connection.render(c, True, BRANCO)
        self.alternativa_C_ativo = connection.render(c, True, ROSA)
        self.alternativa_C = self.alternativa_C_inativo

        self.alternativa_D_inativo = connection.render(d, True, BRANCO)
        self.alternativa_D_ativo = connection.render(d, True, ROSA)
        self.alternativa_D = self.alternativa_D_inativo

        self.alternativa_A_hovered = False
        self.alternativa_B_hovered = False
        self.alternativa_C_hovered = False
        self.alternativa_D_hovered = False

        self.resposta_correta = 'A'

    def pinta_alternativas(self, canva):
        canva.blit(self.alternativa_A, (154, 562))
        canva.blit(self.alternativa_B, (154, 598))
        canva.blit(self.alternativa_C, (154, 634))
        canva.blit(self.alternativa_D, (154, 670))

    def calcula_regras(self, posicao_do_mouse):

        self.is_hovered(posicao_do_mouse)

        if self.alternativa_A_hovered:
            self.alternativa_A = self.alternativa_A_ativo
        else:
            self.alternativa_A = self.alternativa_A_inativo

        if self.alternativa_B_hovered:
            self.alternativa_B = self.alternativa_B_ativo
        else:
            self.alternativa_B = self.alternativa_B_inativo

        if self.alternativa_C_hovered:
            self.alternativa_C = self.alternativa_C_ativo
        else:

            self.alternativa_C = self.alternativa_C_inativo
        if self.alternativa_D_hovered:
            self.alternativa_D = self.alternativa_D_ativo
        else:
            self.alternativa_D = self.alternativa_D_inativo

    def is_hovered(self, posicao_do_mouse):
        if (154 < posicao_do_mouse[0] < self.alternativa_A.get_width() + 154) and (562 < posicao_do_mouse[1] < 562 + self.alternativa_A.get_height()):
            self.alternativa_A_hovered = True
        else:
            self.alternativa_A_hovered = False

        if (154 < posicao_do_mouse[0] < self.alternativa_B.get_width() + 154) and (598 < posicao_do_mouse[1] < 598 + self.alternativa_B.get_height()):
            self.alternativa_B_hovered = True
        else:
            self.alternativa_B_hovered = False

        if (154 < posicao_do_mouse[0] < self.alternativa_C.get_width() + 154) and (634 < posicao_do_mouse[1] < 634 + self.alternativa_C.get_height()):
            self.alternativa_C_hovered = True
        else:
            self.alternativa_C_hovered = False

        if (154 < posicao_do_mouse[0] < self.alternativa_D.get_width() + 154) and (670 < posicao_do_mouse[1] < 670 + self.alternativa_D.get_height()):
            self.alternativa_D_hovered = True
        else:
            self.alternativa_D_hovered = False


# --------------------------------------------------------------


# Tela Inicial

tela_inicial = TelaInicial('tela_inicial_bg')
tela_inicial.ajusta_video()

# Perguntas

bg_pergunta_1 = BgPergunta('pergunta_1')
bg_pergunta_1.ajusta_video()
pergunta_1 = Pergunta('(A) Horse', '(B) Mustang', '(C) Cavallo', '(D) Yegua', 'A')

bg_pergunta_2 = BgPergunta('pergunta_2')
bg_pergunta_2.ajusta_video()
pergunta_2 = Pergunta("(A) Three o'clock", "(B) One o'clock", "(C) Six o'clock", "(D) Eight o'clock", 'D')

bg_pergunta_3 = BgPergunta('pergunta_3')
bg_pergunta_3.ajusta_video()
pergunta_3 = Pergunta("(A) Two", "(B) Seven", "(C) Five", "(D) Ten", "C")

bg_pergunta_4 = BgPergunta('pergunta_4')
bg_pergunta_4.ajusta_video()
pergunta_4 = Pergunta("(A) Thirteen", "(B) Thirty", "(C) Ten Three", "(D) Three Ten", 'A')

bg_pergunta_5 = BgPergunta('pergunta_5')
bg_pergunta_5.ajusta_video()
pergunta_5 = Pergunta("(A) Book, Clock, Door, Shoe", "(B) Book, Time, Door, Shirt", "(C) Shoe, Door, Clock, Book ", "(D) Shoe, Shirt, Book, Door", 'A')

tela_final = pygame.image.load('Resources/Sprites/tela_final.jpg')

telas = [tela_inicial, bg_pergunta_1, bg_pergunta_2, bg_pergunta_3, bg_pergunta_4, bg_pergunta_5, tela_final]
tela_atual = 0


clock = pygame.time.Clock()
while True:
    tela = telas[tela_atual]
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        eventos = event
        if event.type == pygame.KEYUP:
            if eventos.key == pygame.K_RIGHT:
                tela_atual += 1
                if tela_atual == len(telas):
                    tela_atual = 1
            elif eventos.key == pygame.K_LEFT:
                tela_atual -= 1
                if tela_atual < 0:
                    tela_atual = len(telas) - 1

        if tela == tela_inicial:
            if tela_inicial.botao == tela_inicial.botao_ativo and event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                tela_atual += 1

        elif tela == bg_pergunta_1:
            if pergunta_1.alternativa_A_hovered and event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                tela_atual += 1

        elif tela == bg_pergunta_2:
            if pergunta_2.alternativa_D_hovered and event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                tela_atual += 1

        elif tela == bg_pergunta_3:
            if pergunta_3.alternativa_C_hovered and event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                tela_atual += 1

        elif tela == bg_pergunta_4:
            if pergunta_4.alternativa_A_hovered and event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                tela_atual += 1

        elif tela == bg_pergunta_5:
            if pergunta_5.alternativa_A_hovered and event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                tela_atual += 1

    posicao_mouse = pygame.mouse.get_pos()
    if tela == telas[0]:
        tela_inicial.calcula_regra(posicao_mouse, eventos)
        tela_inicial.pinta_tela(screen)

    elif tela == telas[1]:
        bg_pergunta_1.pinta_background(screen)
        pergunta_1.calcula_regras(posicao_mouse)
        pergunta_1.pinta_alternativas(screen)

    elif tela == telas[2]:
        bg_pergunta_2.pinta_background(screen)
        pergunta_2.calcula_regras(posicao_mouse)
        pergunta_2.pinta_alternativas(screen)

    elif tela == telas[3]:
        bg_pergunta_3.pinta_background(screen)
        pergunta_3.calcula_regras(posicao_mouse)
        pergunta_3.pinta_alternativas(screen)

    elif tela == telas[4]:
        bg_pergunta_4.pinta_background(screen)
        pergunta_4.calcula_regras(posicao_mouse)
        pergunta_4.pinta_alternativas(screen)

    elif tela == telas[5]:
        bg_pergunta_5.pinta_background(screen)
        pergunta_5.calcula_regras(posicao_mouse)
        pergunta_5.pinta_alternativas(screen)
    elif tela == tela_final:
        screen.blit(tela, (0, 0))

    pygame.display.flip()
    pygame.display.update()
