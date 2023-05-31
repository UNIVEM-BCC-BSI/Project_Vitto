import pygame
from imports import *
from settings import *

pygame.init()

class Main():
    def __init__(self):
        self.background = bg_tela_inicial
        self.screen = pygame.display.set_mode(size)
        self.play_button = play_inativo
        self.vidas = 0
        self.dificuldade = None
        self.bg = None
        self.perguntas = None
        self.pergunta_atual = 0

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
                        self.vidas = 10
                        self.dificuldade = 'easy'
                        self.bg = bg_perguntas_easy
                        self.perguntas = perguntas_easy
                        self.background = intro_1
                else:
                    easy_button.text_surf = fonte_dificuldades.render(easy_button.text, False, easy_button.color)

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

            # INTERACOES COM ALTERNATIVAS

            if self.dificuldade == 'easy':
                if self.pergunta_atual == 0:
                    if perguntas_easy[0].checa_interacoes():
                        vidas[len(vidas)-1].kill()
                        vidas.pop()
                        self.pergunta_atual += 1
                        self.background = bg_pergunta_2
                    else:
                        print('acertou')
                elif self.pergunta_atual == 1:
                    if perguntas_easy[1].checa_interacoes():
                        vidas[len(vidas)-1].kill()
                        vidas.pop()
                        self.pergunta_atual += 1
                        self.background = bg_pergunta_3
                elif self.pergunta_atual == 2:
                    if perguntas_easy[2].checa_interacoes():
                        vidas[len(vidas)-1].kill()
                        vidas.pop()
                        self.pergunta_atual += 1
                        self.background = bg_pergunta_4
                elif self.pergunta_atual == 3:
                    if perguntas_easy[3].checa_interacoes():
                        vidas[len(vidas)-1].kill()
                        vidas.pop()
                        self.pergunta_atual += 1
                        self.background = bg_pergunta_5
                elif self.pergunta_atual == 4:
                    if perguntas_easy[4].checa_interacoes():
                        vidas[len(vidas)-1].kill()
                        vidas.pop()
                        self.pergunta_atual += 1
                        self.background = bg_pergunta_6
                elif self.pergunta_atual == 5:
                    if perguntas_easy[5].checa_interacoes():
                        vidas[len(vidas)-1].kill()
                        vidas.pop()
                        self.pergunta_atual += 1
                        self.background = bg_pergunta_7
                elif self.pergunta_atual == 6:
                    if perguntas_easy[6].checa_interacoes():
                        vidas[len(vidas)-1].kill()
                        vidas.pop()
                        self.pergunta_atual += 1
                        self.background = bg_pergunta_8
                elif self.pergunta_atual == 7:
                    if perguntas_easy[7].checa_interacoes():
                        vidas[len(vidas)-1].kill()
                        vidas.pop()
                        self.pergunta_atual += 1
                        self.background = bg_pergunta_9
                elif self.pergunta_atual == 8:
                    if perguntas_easy[8].checa_interacoes():
                        vidas[len(vidas)-1].kill()
                        vidas.pop()
                        self.pergunta_atual += 1
                        self.background = bg_pergunta_10
                elif self.pergunta_atual == 9:
                    if perguntas_easy[9].checa_interacoes():
                        vidas[len(vidas)-1].kill()
                        vidas.pop()

    def show_screen(self):
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

        if self.dificuldade == 'easy':
            if self.background == bg_pergunta_1:
                if self.pergunta_atual == 0:
                    self.screen.blit(relogio, (20, 15))
                    vidas_group.draw(self.screen)
                    perguntas_easy[0].mostra_alternativas(self.screen)
            elif self.background == bg_pergunta_2:
                if self.pergunta_atual == 1:
                    self.screen.blit(relogio, (20, 15))
                    vidas_group.draw(self.screen)
                    perguntas_easy[1].mostra_alternativas(self.screen)
            elif self.background == bg_pergunta_3:
                if self.pergunta_atual == 2:
                    self.screen.blit(relogio, (20, 15))
                    vidas_group.draw(self.screen)
                    perguntas_easy[2].mostra_alternativas(self.screen)
            elif self.background == bg_pergunta_4:
                if self.pergunta_atual == 3:
                    self.screen.blit(relogio, (20, 15))
                    vidas_group.draw(self.screen)
                    perguntas_easy[3].mostra_alternativas(self.screen)
            elif self.background == bg_pergunta_5:
                if self.pergunta_atual == 4:
                    self.screen.blit(relogio, (20, 15))
                    vidas_group.draw(self.screen)
                    perguntas_easy[4].mostra_alternativas(self.screen)
            elif self.background == bg_pergunta_6:
                if self.pergunta_atual == 5:
                    self.screen.blit(relogio, (20, 15))
                    vidas_group.draw(self.screen)
                    perguntas_easy[5].mostra_alternativas(self.screen)
            elif self.background == bg_pergunta_7:
                if self.pergunta_atual == 6:
                    self.screen.blit(relogio, (20, 15))
                    vidas_group.draw(self.screen)
                    perguntas_easy[6].mostra_alternativas(self.screen)
            elif self.background == bg_pergunta_8:
                if self.pergunta_atual == 7:
                    self.screen.blit(relogio, (20, 15))
                    vidas_group.draw(self.screen)
                    perguntas_easy[7].mostra_alternativas(self.screen)
            elif self.background == bg_pergunta_9:
                if self.pergunta_atual == 8:
                    self.screen.blit(relogio, (20, 15))
                    vidas_group.draw(self.screen)
                    perguntas_easy[8].mostra_alternativas(self.screen)
            elif self.background == bg_pergunta_10:
                if self.pergunta_atual == 9:
                    self.screen.blit(relogio, (20, 15))
                    vidas_group.draw(self.screen)
                    perguntas_easy[9].mostra_alternativas(self.screen)

    def run(self):
        self.event_loop()
        self.show_screen()


main = Main()
clock = pygame.time.Clock()
while True:

    main.run()
    pygame.display.update()
    clock.tick(FPS)
