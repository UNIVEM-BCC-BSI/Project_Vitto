import pygame
from imports import *
from settings import *


pygame.init()

class Main():
    def __init__(self):
        self.background = bg_tela_inicial
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Project Vitto")
        pygame.display.set_icon(icone)
        self.play_button = play_inativo
        self.exit_button = exit_inativo
        self.dificuldade = None
        self.bg = None
        self.perguntas = None
        self.dicas = None
        self.dicas_group = pygame.sprite.Group()
        self.pergunta_atual = 0
        self.estado = None
        self.final = 0

        self.tempo_inicial = 0
        self.tempo_atual = 0

        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.05)
    
    

    def resultado_da_interacao(self, perguntas, vida_max, dicas):
        if perguntas[self.pergunta_atual].checa_interacoes() != None:
            dicas[self.pergunta_atual].image = dicas[self.pergunta_atual].botao
            if self.pergunta_atual < len(perguntas)-1:
                self.dicas_group.remove(dicas[self.pergunta_atual])
                self.dicas_group.add(dicas[self.pergunta_atual+1])
            if perguntas[self.pergunta_atual].checa_interacoes() == None:
                self.tempo_inicial = pygame.time.get_ticks()
                self.pergunta_atual += 1
        if self.pergunta_atual == len(perguntas) or len(vidas) == 0:
            if len(vidas) == 0:
                morreu.play()
                self.final = 0
            elif 0 < len(vidas) < vida_max:
                ganhou.play()
                self.final = 1
            elif len(vidas) == vida_max:
                ganhou.play()
                self.final = 2
            self.estado = 'final'
            self.dificuldade = None
            self.perguntas = None
            self.dicas = None
            self.dicas_group = pygame.sprite.Group()
            self.pergunta_atual = 0
            self.vidas_group = pygame.sprite.Group()

    def event_loop(self):
        espaco_livre = True
        mouse_position = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            # INTERAÇÃO COM O BOTÃO PLAY

            if self.background == bg_tela_inicial:
                if play_button_rect.collidepoint(mouse_position) or exit_rect.collidepoint(mouse_position):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                    if play_button_rect.collidepoint(mouse_position):
                        self.play_button = play_ativo
                    elif exit_rect.collidepoint(mouse_position):
                        self.exit_button = exit_ativo
                else:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    self.play_button = play_inativo
                    self.exit_button = exit_inativo

                if play_button_rect.collidepoint(mouse_position):
                    if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                        self.background = bg_tela_dificuldades
                        som_clique()
                elif exit_rect.collidepoint(mouse_position):
                    if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                        self.background = bg_tela_dificuldades
                        som_clique()
                        exit()
                # else:
                #     self.play_button = play_inativo
                #     pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

            # SELECIONAR DIFICULDADE

            if self.background == bg_tela_dificuldades:
                
                if easy_button.text_rect.collidepoint(mouse_position):
                    easy_button.text_surf = (fonte_dificuldades.render(easy_button.text, False, 'white'))
                    if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                        som_clique()
                        self.dificuldade = 'easy'
                        self.bg = bg_perguntas_easy
                        self.perguntas = perguntas_easy
                        self.dicas = dicas_easy
                        self.dicas_group.add(self.dicas[0])
                        self.background = intro_1
                        coracoes(10)
                        
                else:
                    easy_button.text_surf = fonte_dificuldades.render(easy_button.text, False, easy_button.color)

                if medium_button.text_rect.collidepoint(mouse_position):
                    medium_button.text_surf = (fonte_dificuldades.render(medium_button.text, False, 'white'))
                    if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                        som_clique()
                        self.dificuldade = 'medium'
                        self.bg = bg_perguntas_medium
                        self.perguntas = perguntas_medium
                        self.dicas = dicas_medium
                        self.dicas_group.add(self.dicas[0])
                        self.background = intro_1
                        coracoes(8)
                else:
                    medium_button.text_surf = fonte_dificuldades.render(medium_button.text, False, medium_button.color)

                if hard_button.text_rect.collidepoint(mouse_position):
                    hard_button.text_surf = (fonte_dificuldades.render(hard_button.text, False, 'white'))
                    if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                        som_clique()
                        self.dificuldade = 'hard'
                        self.bg = bg_perguntas_hard
                        self.perguntas = perguntas_hard
                        self.dicas = dicas_hard
                        self.dicas_group.add(self.dicas[0])
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
                
            if self.background == tela_final[self.final]:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and espaco_livre:
                    espaco_livre = False
                    self.background = bg_tela_inicial
                    self.estado = None
                    self.play_button = play_inativo
                    self.dificuldade = None
                    self.bg = None
                    self.perguntas = None
                    self.pergunta_atual = 0
                    self.estado = None

            # INTERACOES COM ALTERNATIVAS
            if self.estado == 'jogando':
                if self.dificuldade == 'easy' and self.background == self.bg[self.pergunta_atual]:
                    self.resultado_da_interacao(perguntas_easy, 10, self.dicas)

                elif self.dificuldade == 'medium' and self.background == self.bg[self.pergunta_atual]:
                    self.resultado_da_interacao(perguntas_medium, 8, self.dicas)

                elif self.dificuldade == 'hard' and self.background == self.bg[self.pergunta_atual]:
                    self.resultado_da_interacao(perguntas_hard, 5, self.dicas)

    def show_screen(self):
        if self.estado != 'final':
            self.screen.blit(video_reproduzivel(self.background), (0, 0))


        if self.background == bg_tela_inicial:
            self.screen.blit(self.play_button, play_button_rect)
            self.screen.blit(self.exit_button, exit_rect)


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

            self.tempo_atual = (pygame.time.get_ticks())
            tempo = (self.tempo_atual-self.tempo_inicial)//1000


            if self.dificuldade == 'easy':
                vidas_group.draw(self.screen)
                self.background = bg_perguntas_easy[self.pergunta_atual]
                perguntas_easy[self.pergunta_atual].mostra_alternativas(self.screen)
                if tempo > 7:
                    self.dicas_group.draw(self.screen)  
                    self.dicas_group.update()

            elif self.dificuldade == 'medium':
                vidas_group.draw(self.screen)
                self.background = bg_perguntas_medium[self.pergunta_atual]
                perguntas_medium[self.pergunta_atual].mostra_alternativas(self.screen)
                if tempo > 7:
                    self.dicas_group.draw(self.screen)  
                    self.dicas_group.update()

            elif self.dificuldade == 'hard':
                vidas_group.draw(self.screen)
                self.background = bg_perguntas_hard[self.pergunta_atual]
                perguntas_hard[self.pergunta_atual].mostra_alternativas(self.screen)
                if tempo > 7:
                    self.dicas_group.draw(self.screen)  
                    self.dicas_group.update()

        if self.estado == 'final':
            self.background = tela_final[self.final]
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(press_space_to_main, press_space_to_main_rect)


    def run(self):
        self.event_loop()
        self.show_screen()

main = Main()
clock = pygame.time.Clock()
while True:

    main.run()
    
    pygame.display.update()
    clock.tick(FPS)
