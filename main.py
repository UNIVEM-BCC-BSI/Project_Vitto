import pygame
from imports import *
from settings import *

pygame.init()

class Main():
    def __init__(self):
        self.background = bg_tela_inicial
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Project Vitto")
        self.play_button = play_inativo
        self.dificuldade = None
        self.bg = None
        self.perguntas = None
        self.pergunta_atual = 0
        self.estado = None
        self.final = None
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.05)
    
    def resultado_da_interacao(self, perguntas, vida_max):
        if perguntas[self.pergunta_atual].checa_interacoes() != None:
            if perguntas[self.pergunta_atual].checa_interacoes() == None: 
                self.pergunta_atual += 1
        if self.pergunta_atual == len(perguntas) or len(vidas) == 0:
            if len(vidas) == 0:
                self.final = 0
            elif len(vidas) < vida_max:
                self.final = 1
            elif len(vidas) == vida_max:
                self.final = 2
            self.estado = 'final'

    def event_loop(self):
        espaco_livre = True
        mouse_position = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            # INTERAÇÃO COM O BOTÃO PLAY

            if self.background == bg_tela_inicial:

                if play_button_rect.collidepoint(mouse_position):
                    self.play_button = play_ativo
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                    if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                        self.background = bg_tela_dificuldades
                else:
                    self.play_button = play_inativo
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

            # SELECIONAR DIFICULDADE

            if self.background == bg_tela_dificuldades:

                if easy_button.text_rect.collidepoint(mouse_position):
                    easy_button.text_surf = (fonte_dificuldades.render(easy_button.text, False, 'white'))
                    if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                        self.dificuldade = 'easy'
                        self.bg = bg_perguntas_easy
                        self.perguntas = perguntas_easy
                        self.background = intro_1
                        coracoes(10)
                        
                else:
                    easy_button.text_surf = fonte_dificuldades.render(easy_button.text, False, easy_button.color)

                if medium_button.text_rect.collidepoint(mouse_position):
                    medium_button.text_surf = (fonte_dificuldades.render(medium_button.text, False, 'white'))
                    if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                        self.dificuldade = 'medium'
                        self.bg = bg_perguntas_medium
                        self.perguntas = perguntas_medium
                        self.background = intro_1
                        coracoes(8)
                else:
                    medium_button.text_surf = fonte_dificuldades.render(medium_button.text, False, medium_button.color)

                if hard_button.text_rect.collidepoint(mouse_position):
                    hard_button.text_surf = (fonte_dificuldades.render(hard_button.text, False, 'white'))
                    if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                        self.dificuldade = 'hard'
                        self.bg = bg_perguntas_hard
                        self.perguntas = perguntas_hard
                        self.background = intro_1
                        coracoes(5)
                else:
                    hard_button.text_surf = fonte_dificuldades.render(hard_button.text, False, hard_button.color)

            # INTRO SCREENS

            if self.background == intro_1:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and espaco_livre:
                    espaco_livre = False
                    self.background = intro_2

            if self.background == intro_2:
                if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                    espaco_livre = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and espaco_livre:
                    espaco_livre = False
                    self.background = intro_3

            if self.background == intro_3:
                if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                    espaco_livre = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and espaco_livre:
                    espaco_livre = False
                    self.background = intro_4

            if self.background == intro_4:
                if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                    espaco_livre = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and espaco_livre:
                    self.background = self.bg[self.pergunta_atual]
                    self.estado = 'jogando'

            # INTERACOES COM ALTERNATIVAS
            if self.estado == 'jogando':
                if self.dificuldade == 'easy' and self.background == self.bg[self.pergunta_atual]:
                    self.resultado_da_interacao(perguntas_easy, 10) 

                elif self.dificuldade == 'medium' and self.background == self.bg[self.pergunta_atual]:
                    self.resultado_da_interacao(perguntas_medium, 8)

                elif self.dificuldade == 'hard' and self.background == self.bg[self.pergunta_atual]:
                    self.resultado_da_interacao(perguntas_hard, 5)

    def show_screen(self):
        if self.estado != 'final':
            self.screen.blit(video_reproduzivel(self.background), (0, 0))
        

        if self.background == bg_tela_inicial:
            self.screen.blit(self.play_button, play_button_rect)

        if self.background == bg_tela_dificuldades:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            self.screen.blit(dificuldade_texto, dificuldade_texto_rect)
            easy_button.mostra_botao(self.screen)
            medium_button.mostra_botao(self.screen)
            hard_button.mostra_botao(self.screen)

        if self.background == intro_1:
            self.screen.blit(press_space, press_space_rect)
        elif self.background == intro_2:
            self.screen.blit(press_space, press_space_rect)
        elif self.background == intro_3:
            self.screen.blit(press_space, press_space_rect)
        elif self.background == intro_4:
            self.screen.blit(press_space, press_space_rect)


        if self.estado == 'jogando':

            if self.dificuldade == 'easy':
                vidas_group.draw(self.screen)
                self.background = bg_perguntas_easy[self.pergunta_atual]
                perguntas_easy[self.pergunta_atual].mostra_alternativas(self.screen)
                 

            elif self.dificuldade == 'medium':
                vidas_group.draw(self.screen)
                self.background = bg_perguntas_medium[self.pergunta_atual]
                perguntas_medium[self.pergunta_atual].mostra_alternativas(self.screen)

            elif self.dificuldade == 'hard':
                vidas_group.draw(self.screen)
                self.background = bg_perguntas_hard[self.pergunta_atual]
                perguntas_hard[self.pergunta_atual].mostra_alternativas(self.screen)
        
        if self.estado == 'final':
            self.background = tela_final[self.final]
            self.screen.blit(self.background, (0, 0))

    def run(self):
        self.event_loop()
        self.show_screen()


main = Main()
clock = pygame.time.Clock()
while True:

    main.run()
    
    pygame.display.update()
    clock.tick(FPS)
