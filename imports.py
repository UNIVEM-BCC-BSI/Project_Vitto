import pygame
from moviepy.editor import VideoFileClip
from moviepy.video.fx import all as vfx

AZUL = (62, 114, 188)
BRANCO = (255, 255, 255)

# FONTS

fonte_intro_creditos = pygame.font.Font('fonts/half_bold_pixel_7/half_bold_pixel-7.ttf', 16)
fonte_dificuldades = pygame.font.Font('fonts/connection_ii/ConnectionII.otf', 50)
fonte_dificuldades_titulo = pygame.font.Font('fonts/connection_ii/ConnectionII.otf', 44)
fonte_titulos = pygame.font.Font('fonts/half_bold_pixel_7/half_bold_pixel-7.ttf', 25)
fonte_alternativas = pygame.font.Font('fonts/half_bold_pixel_7/half_bold_pixel-7.ttf', 20)


# SONS


playback = pygame.mixer.music.load('sons/playback.mpeg')

alternativa = pygame.mixer.Sound('sons/alternativas.mpeg')
alternativa.set_volume(0.1)
acertou = pygame.mixer.Sound('sons/acertou.mpeg')
acertou.set_volume(0.1)
errou = pygame.mixer.Sound('sons/errou.mpeg')
errou.set_volume(0.1)
clique = pygame.mixer.Sound('sons/clique.MP3')
clique.set_volume(0.1)
morreu = pygame.mixer.Sound('sons/morreu.mpeg')
morreu.set_volume(0.1)
narracao = pygame.mixer.Sound('sons/narracao.mpeg')
narracao.set_volume(0.1)
ganhou = pygame.mixer.Sound('sons/ganhou.mpeg')
ganhou.set_volume(0.1)

def som_clique():
        clicou = False
        if not clicou:
            clique.play()
            clicou = True
# IMPORTS

def ajusta_video(file):
    clip = VideoFileClip('images/' + file + '.mp4')
    clip = clip.loop()
    clip.set_duration(5)
    clip = vfx.mirror_x(clip)
    clip = clip.fx(vfx.rotate, 90)
    return clip


def video_reproduzivel(file):
    frame = file.get_frame(pygame.time.get_ticks() / 1000)
    return pygame.surfarray.make_surface(frame)


# BACKGROUNDS

bg_tela_inicial = ajusta_video('bg_tela_inicial')
bg_tela_dificuldades = ajusta_video('bg_tela_dificuldades')

intro_1 = ajusta_video('intro_1')
intro_2 = ajusta_video('intro_2')
intro_3 = ajusta_video('intro_3')
intro_4 = ajusta_video('intro_4')

intros = [intro_1, intro_2, intro_3, intro_4]

tela_feliz = pygame.image.load('images/tela_feliz.png')
tela_mal = pygame.image.load('images/tela_mal.png') 
tela_morre = pygame.image.load('images/tela_morre.png') 
tela_final = [tela_morre, tela_mal, tela_feliz]

# BOTOES

play_button_rect = pygame.Rect(379, 480, 312, 135)
play_inativo = pygame.image.load('images/play_inativo.png')
play_inativo = pygame.transform.scale(play_inativo, (312, 135))
play_ativo = pygame.image.load('images/play_ativo.png')
play_ativo = pygame.transform.scale(play_ativo, (312, 135))

# COMPLEMENTO DAS PERGUNTAS

coracao = pygame.image.load('images/coracao.png')
relogio = pygame.image.load('images/relogio.png')

# PERGUNTAS

bg_pergunta_1 = ajusta_video('pergunta_1')
bg_pergunta_2 = ajusta_video('pergunta_2')
bg_pergunta_3 = ajusta_video('pergunta_3')
bg_pergunta_4 = ajusta_video('pergunta_4')
bg_pergunta_5 = ajusta_video('pergunta_5')
bg_pergunta_6 = ajusta_video('pergunta_6')
bg_pergunta_7 = ajusta_video('pergunta_7')
bg_pergunta_8 = ajusta_video('pergunta_8')
bg_pergunta_9 = ajusta_video('pergunta_9')
bg_pergunta_10 = ajusta_video('pergunta_10')
bg_pergunta_11 = ajusta_video('pergunta_11')
bg_pergunta_12 = ajusta_video('pergunta_12')
bg_pergunta_13 = ajusta_video('pergunta_13')
bg_pergunta_14 = ajusta_video('pergunta_14')
bg_pergunta_15 = ajusta_video('pergunta_15')
bg_pergunta_16 = ajusta_video('pergunta_16')
bg_pergunta_17 = ajusta_video('pergunta_17')
bg_pergunta_18 = ajusta_video('pergunta_18')
bg_pergunta_19 = ajusta_video('pergunta_19')
bg_pergunta_20 = ajusta_video('pergunta_20')


class Vida(pygame.sprite.Sprite):
    def __init__(self, imagem, pos_x, pos_y):
        super().__init__()
        self.image = imagem
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]


vidas = []
vidas_group = pygame.sprite.Group()

def coracoes(dificuldade):
    first = 1035
    for i in range(dificuldade):
        vidas.append(Vida(coracao, first - 45*i, 16))
    vidas_group.add(vidas)
        

class BotaoDificuldade(pygame.sprite.Sprite):
    def __init__(self, texto, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.text = texto
        self.x = x
        self.y = y
        self.color = (62, 114, 188)
        self.text_surf = fonte_dificuldades.render(self.text, False, self.color)
        self.text_rect = self.text_surf.get_rect(topleft=(self.x, self.y))

    def mostra_botao(self, screen):
        screen.blit(self.text_surf, self.text_rect)


dificuldade_texto = fonte_dificuldades_titulo.render('DEFINA A DIFICULDADE', False, (62, 114, 188))
dificuldade_texto_rect = dificuldade_texto.get_rect(topleft=(312,234))

easy_button = BotaoDificuldade('Easy', 269, 353)
medium_button = BotaoDificuldade('Medium', 437, 353)
hard_button = BotaoDificuldade('Hard', 685, 353)

press_space = fonte_titulos.render('(press space to continue)', False, 'white')
press_space_rect = press_space.get_rect(center=(540, 670))

press_space_to_main = fonte_titulos.render('(press space to return no main menu)', False, 'white')
press_space_to_main_rect = press_space_to_main.get_rect(center=(540, 670))

# PERGUNTAS

class Pergunta:
    def __init__(self, a, b, c, d, alternativa_correta, cor):
        self.x = 154
        self.y_a = 562
        self.y_b = 598
        self.y_c = 634
        self.y_d = 670
        self.cor = cor

        self.texto_a = a
        self.texto_b = b
        self.texto_c = c
        self.texto_d = d

        self.alternativa_a = self.texto_a
        self.alternativa_a_surface = fonte_alternativas.render(self.alternativa_a, False, self.cor)
        self.alternativa_a_rect = self.alternativa_a_surface.get_rect(topleft=(self.x, self.y_a))

        self.alternativa_b = self.texto_b
        self.alternativa_b_surface = fonte_alternativas.render(self.alternativa_b, False, self.cor)
        self.alternativa_b_rect = self.alternativa_b_surface.get_rect(topleft=(self.x, self.y_b))

        self.alternativa_c = self.texto_c
        self.alternativa_c_surface = fonte_alternativas.render(self.alternativa_c, False, self.cor)
        self.alternativa_c_rect = self.alternativa_c_surface.get_rect(topleft=(self.x, self.y_c))

        self.alternativa_d = self.texto_d
        self.alternativa_d_surface = fonte_alternativas.render(self.alternativa_d, False, self.cor)
        self.alternativa_d_rect = self.alternativa_d_surface.get_rect(topleft=(self.x, self.y_d))

        self.alternativas_text = [self.texto_a, self.texto_b, self.texto_c, self.texto_d]
        self.alternativas_rect = [self.alternativa_a_rect, self.alternativa_b_rect, self.alternativa_c_rect, self.alternativa_d_rect]
        self.alternativas_surface = [self.alternativa_a_surface, self.alternativa_b_surface, self.alternativa_c_surface, self.alternativa_d_surface]

        self.alternativa_correta = alternativa_correta
        self.pressionado = False
        self.acertou = None
        self.hover = False
        self.ultimo_hover = False

    def mostra_alternativas(self, tela):
        tela.blit(self.alternativa_a_surface, self.alternativa_a_rect)
        tela.blit(self.alternativa_b_surface, self.alternativa_b_rect)
        tela.blit(self.alternativa_c_surface, self.alternativa_c_rect)
        tela.blit(self.alternativa_d_surface, self.alternativa_d_rect)

    def checa_interacoes(self):
        mouse_position = pygame.mouse.get_pos()
        if self.alternativa_a_rect.collidepoint(mouse_position):
            
            self.alternativa_a_surface = fonte_alternativas.render(self.alternativa_a, False, AZUL)

            if pygame.mouse.get_pressed()[0]:
                self.pressionado = True
            else:
                if self.pressionado:
                    self.pressionado = False
                    if self.alternativa_correta == 'A':
                        acertou.play()
                        return 0
                    else:
                        errou.play()
                        if len(vidas) > 0:
                            vidas[len(vidas)-1].kill()
                            vidas.pop()
        else:
            self.alternativa_a_surface = fonte_alternativas.render(self.alternativa_a, False, self.cor)
            
        if self.alternativa_b_rect.collidepoint(mouse_position):
            self.alternativa_b_surface = fonte_alternativas.render(self.alternativa_b, False, AZUL)
            if pygame.mouse.get_pressed()[0]:
                self.pressionado = True
            else:
                if self.pressionado:
                    self.pressionado = False
                    if self.alternativa_correta == 'B':
                        acertou.play()
                        return 0
                    else:
                        errou.play()
                        if len(vidas) > 0:
                            vidas[len(vidas)-1].kill()
                            vidas.pop()
        else:
            self.alternativa_b_surface = fonte_alternativas.render(
                self.alternativa_b, False, self.cor)

        if self.alternativa_c_rect.collidepoint(mouse_position):
            self.alternativa_c_surface = fonte_alternativas.render(self.alternativa_c, False, AZUL)
            if pygame.mouse.get_pressed()[0]:
                self.pressionado = True
            else:
                if self.pressionado:
                    self.pressionado = False
                    if self.alternativa_correta == 'C':
                        acertou.play()
                        return 0
                    else:
                        errou.play()
                        if len(vidas) > 0:
                            vidas[len(vidas)-1].kill()
                            vidas.pop()
        else:
            self.alternativa_c_surface = fonte_alternativas.render(
                self.alternativa_c, False, self.cor)

        if self.alternativa_d_rect.collidepoint(mouse_position):
            self.alternativa_d_surface = fonte_alternativas.render(self.alternativa_d, False, AZUL)
            if pygame.mouse.get_pressed()[0]:
                self.pressionado = True
            else:
                if self.pressionado:
                    self.pressionado = False
                    if self.alternativa_correta == 'D':
                        acertou.play()
                        return 0
                    else:
                        errou.play()
                        if len(vidas) > 0:
                            vidas[len(vidas)-1].kill()
                            vidas.pop()
        else:
            self.alternativa_d_surface = fonte_alternativas.render(
                self.alternativa_d, False, self.cor)
        
        if self.alternativa_a_rect.collidepoint(mouse_position) or self.alternativa_b_rect.collidepoint(mouse_position) or self.alternativa_c_rect.collidepoint(mouse_position) or self.alternativa_d_rect.collidepoint(mouse_position):
            if self.hover == False:
                alternativa.play()
                self.hover = True
        else:
            if self.hover == True:
                self.hover = False

        

pergunta1 = Pergunta('(A) Horse',
                     '(B) Mustang',
                     '(C) Cavallo',
                     '(D) Yegua',
                     'A',
                     BRANCO)
pergunta2 = Pergunta("(A) Stone",
                     "(B) Hermes",
                     "(C) Snake",
                     "(D) Medusa",
                     'C',
                    BRANCO)
pergunta3 = Pergunta(
                     "(A) Birds fly west and horses run east",
                     "(B) The birds fly for west and horses run fo the east",
                     "(C) Birds fly oest and horses run lest",
                     "(D) Birds fly to west so the horses run to east",
                     "A",
                     BRANCO)
pergunta4 = Pergunta(
                     "(A) She is beautiful",
                     "(B) He are handsome",
                     "(C) She to are amazing",
                     "(D) We to be crazy",
                     'A',
                     BRANCO)
pergunta5 = Pergunta(
                    "(A) Books, are, is",
                    "(B) Teaches, is are",
                    "(C) Runs, is, is",
                    "(D) Draws, are, are",
                    'B',
                    BRANCO)
pergunta6 = Pergunta(
                    "(A) Drive, of",
                    "(B) Take, of",
                    "(C) Drive, from",
                    "(D) See, about",
                    'C',
                    BRANCO)
pergunta7 = Pergunta(
                    "(A) Does, does",
                    "(B) Do, does",
                    "(C) Does, do",
                    "(D) Do, do",
                    'B',
                    BRANCO)
pergunta8 = Pergunta(
                    "(A) I don't think so",
                    "(B) He's not being good",
                    "(C) No, I am not",
                    "(D) I have been good!",
                    'D',
                    BRANCO)
pergunta9 = Pergunta(
                    "(A) Beak",
                    "(B) Snake",
                    "(C) Whale",
                    "(D) Wolf",
                    'D',
                    BRANCO)
pergunta10 = Pergunta(
                    "(A) Though",
                    "(B) Those",
                    "(C) Thers",
                    "(D) Thei",
                    'B',
                    BRANCO)
pergunta11 = Pergunta(
                    "(A) Thair",
                    "(B) This",
                    "(C) Those",
                    "(D) That",
                    'C',
                    BRANCO)
pergunta12 = Pergunta(
                    "(A) Pineapple, pumpkin, avocado, banana",
                    "(B) Apple, orange, lemon, apple",
                    "(C) Pumpkin, khaki, lemon, apple",
                    "(D) Apple, orange, guava, papaya",
                    'B',
                    BRANCO)
pergunta13 = Pergunta(
                    "(A) Three o'clock",
                    "(B) One o'clock",
                    "(C) Six o'clock",
                    "(D) Eight o'clock",
                    'D',
                    BRANCO)
pergunta14 = Pergunta(
                    "(A) Two",
                    "(B) Seven",
                    "(C) Five",
                    "(D) Ten",
                    'C',
                    BRANCO)
pergunta15 = Pergunta(
                    "(A) Thirteen",
                    "(B) Thirty",
                    "(C) Ten Three",
                    "(D) Three Ten",
                    'A',
                    BRANCO)
pergunta16 = Pergunta(
                    "(A)  Book, clock, door, shoe",
                    "(B) Book, time, door, shirt",
                    "(C) Shoe, door, clock, book",
                    "(D) Shoe, shirt, book, door",
                    'A',
                    BRANCO)
pergunta17 = Pergunta(
                    "(A) Yellow",
                    "(B) Blue",
                    "(C) Purple",
                    "(D) Red",
                    'D',
                    BRANCO)
pergunta18 = Pergunta(
                    "(A) White",
                    "(B) Green",
                    "(C) Purple",
                    "(D) Red",
                    'B',
                    BRANCO)
pergunta19 = Pergunta(
                    "(A) Purple - Yellow",
                    "(B) Blue - Green",
                    "(C) Yellow - Purple",
                    "(D) Black - Orange",
                    'C',
                    BRANCO)
pergunta20 = Pergunta(
                    "(A) Yellow - Black",
                    "(B) Orange - Green",
                    "(C) Black - Red",
                    "(D) Black - Purple",
                    'C',
                    BRANCO)

perguntas_easy = [pergunta1, pergunta2, pergunta3, pergunta4, pergunta5, pergunta6, pergunta7, pergunta8, pergunta9, pergunta10]
perguntas_medium = [pergunta11, pergunta12, pergunta13, pergunta14, pergunta15, pergunta16, pergunta17, pergunta18]
perguntas_hard = [pergunta19, pergunta20]

bg_perguntas_easy = [bg_pergunta_1, bg_pergunta_2, bg_pergunta_3, bg_pergunta_4, bg_pergunta_5, bg_pergunta_6, bg_pergunta_7, bg_pergunta_8, bg_pergunta_9, bg_pergunta_10]
bg_perguntas_medium = [bg_pergunta_11, bg_pergunta_12, bg_pergunta_13, bg_pergunta_14, bg_pergunta_15, bg_pergunta_16, bg_pergunta_17, bg_pergunta_18]
bg_perguntas_hard = [bg_pergunta_19, bg_pergunta_20]

dicas_easy = []
dicas_medium = []
dicas_hard = []
