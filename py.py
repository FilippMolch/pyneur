import pygame
import sys
import main
import snak
import random
import data
import neat

class Game(object):
        def __init__(self):
            pygame.init()
            self.score = 0
            self.deth = 0
            self.deth_flag = True
            self.dis = (1000, 600)
            self.disp = pygame.display.set_mode(self.dis)
            self.flag = True
            self.color = (109,109,109)
            self.panel_color = (102, 204, 255)
            self.black = (0, 0, 0)
            self.ln = 0
            self.font = pygame.font.Font('font/mine.ttf', 14)
            self.text = self.font.render("генетический алгоритм", 0, self.black)
            self.text_2 = self.font.render("свободный режим", 0, self.black)
            self.text_3 = self.font.render("счёт: {}".format(self.score), 0, self.black)
            self.text_4 = self.font.render("смерти: {}".format(self.deth), 0, self.black)
            self.text_5 = self.font.render("длина: {}".format(self.ln), 0, self.black)
            self.text_6 = self.font.render("музыка: F1".format(self.ln), 0, self.black)
            self.text_7 = self.font.render("заново: F2".format(self.ln), 0, self.black)
            self.text_8 = self.font.render("просто: F3".format(self.ln), 0, self.black)
            self.text_9 = self.font.render("норм: F4".format(self.ln), 0, self.black)
            self.text_10 = self.font.render("сложно: F5".format(self.ln), 0, self.black)
            self.text_66 = self.font.render("debug: P".format(self.ln), 0, self.black)
            self.text_11 = self.font.render("пауза: Q".format(self.ln), 0, self.black)
            self.text_12 = self.font.render("режимы: F6".format(self.ln), 0, self.black)
            self.o = 149
            self.anim = snak.Anim(self.disp, (255, 0, 0))
            self.move = snak.Move(self.disp, self.anim.head)
            self.io = 9
            self.sn = True
            self.mus = pygame.mixer.Sound('music/eat.ogg')
            self.mus_2 = pygame.mixer.Sound('music/deth.ogg')
            self.mus_3 = pygame.mixer.Sound('music/music.ogg')
            self.speed = 0.1
            self.play = True
            self.play_index = True
            self.play_index_2 = 0
            self.do_flag_dir = ""
            self.i_tebya_unichtoju = 1
            self.mod = 0
            self.pause = False
            self.mod_index = 0
            self.debug = 0
            self.i = 0
            self.dot_1 = 0
            self.dot_2 = 0
            self.dot_3 = 0
            self.dot_4 = 0
            self.dot_5 = 0
            self.dot_6 = 0

            self.dot_1_1 = 0
            self.dot_2_1 = 0
            self.dot_3_1 = 0
            self.dot_4_1 = 0
            self.dot_5_1 = 0
            self.dot_6_1 = 0

            self.dot_1_2 = 0
            self.dot_2_2 = 0
            self.dot_3_2 = 0
            self.dot_4_2 = 0
            self.dot_5_2 = 0
            self.dot_6_2 = 0

            self.dot_1_3 = 0
            self.dot_2_3 = 0
            self.dot_3_3 = 0
            self.dot_4_3 = 0
            self.dot_5_3 = 0
            self.dot_6_3 = 0

            self.outputs = 0
            self.config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, "./config-feedforward.txt")


        def game(self, flag):
            while self.flag:
                self.flag = flag
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT and self.anim.flag_dir != "RIGHT" and not self.pause and not self.mod:
                            self.anim.flag_dir = "LEFT"

                        if event.key == pygame.K_RIGHT and self.anim.flag_dir != "LEFT" and not self.pause and not self.mod:
                            self.anim.flag_dir = "RIGHT"

                        if event.key == pygame.K_UP and self.anim.flag_dir != "DOWN" and not self.pause and not self.mod:
                            self.anim.flag_dir = "UP"

                        if event.key == pygame.K_DOWN and self.anim.flag_dir != "UP" and not self.pause and not self.mod:
                            self.anim.flag_dir = "DOWN"

                        if event.key == pygame.K_F1:
                            if self.play and self.play_index and self.play_index_2 % 2 == 0:
                                self.play_index_2 += 2
                                self.play_index = False
                                self.mus_3.play()
                                self.play = False
                            else:
                                self.play = True
                                self.play_index = True
                                self.mus_3.stop()

                        if event.key == pygame.K_F2:
                            if not self.deth_flag:
                                self.deth_flag = True
                                self.anim.flag_dir = "RIGHT"
                                self.anim.snake = [[120,40],[140,40],[160,40]]
                                self.anim.head = [120,40]
                                self.sn = True
                                self.score = 0

                        if event.key == pygame.K_F3:
                            self.speed = 0.1

                        elif event.key == pygame.K_F4:
                            self.speed = 0.050

                        elif event.key == pygame.K_F5:
                            self.speed = 0.030
                        elif event.key == pygame.K_p:
                            #self.speed = 0.5
                            self.i += 1
                            if self.i % 2 == 0:
                                self.debug = 1
                            else:
                                self.debug = 0

                        elif event.key == pygame.K_q:
                            self.i_tebya_unichtoju += 1
                            if self.i_tebya_unichtoju % 2 == 0:
                                self.do_flag_dir = self.anim.flag_dir
                                self.anim.flag_dir = "PAUSE"
                                self.pause = True
                            else:
                                self.pause = False
                                self.anim.flag_dir = self.do_flag_dir

                        elif event.key == pygame.K_F6:
                            self.mod_index += 1
                            if self.mod_index % 2 == 0:
                                self.mod = 1
                            else:
                                self.mod = 0


                if self.anim.head[0] <= 80 and self.deth_flag:
                    self.mus_2.play()
                    self.anim.flag_dir = "STOP"
                    self.deth += 1
                    self.deth_flag = False
                elif self.anim.head[0] >= 980 and self.deth_flag:
                    self.mus_2.play()
                    self.anim.flag_dir = "STOP"
                    self.deth += 1
                    self.deth_flag = False
                elif self.anim.head[1] <= 00 and self.deth_flag:
                    self.mus_2.play()
                    self.anim.flag_dir = "STOP"
                    self.deth += 1
                    self.deth_flag = False
                elif self.anim.head[1] >= 580 and self.deth_flag:
                    self.mus_2.play()
                    self.anim.flag_dir = "STOP"
                    self.deth += 1
                    self.deth_flag = False

                if self.anim.flag_dir == "STOP":
                    self.sn = False

                if self.sn:
                    self.anim.anim_snak()
                    self.anim.draw_snake(self.speed, 1)
                else:
                    self.anim.draw_snake(self.speed, 0)

                self.anim.move()
                self.ln = len(self.anim.snake)
                self.text_4 = self.font.render("смерти: {}".format(self.deth), 0, self.black)
                self.text_5 = self.font.render("длина: {}".format(self.ln), 0, self.black)
                self.text_3 = self.font.render("счёт: {}".format(self.score), 0, self.black)

                if self.anim.head == list(self.move.arr_eat):
                    self.mus.play()
                    self.score += 50
                    self.move.draw_eat(1)
                    self.anim.eat_sn()

                if self.io == 9:
                    self.io += 1
                    self.move.ran()

                self.move.draw_eat(0)
                main.Field.field(self.disp, self.color)
                main.Field.field_2(self.disp, self.color)

                if self.pause:
                    pygame.draw.rect(self.disp, self.black, (100, 20, 920, 560))

                pygame.draw.rect(self.disp, self.panel_color, (0, 0, 100, 600))
                pygame.draw.rect(self.disp, self.panel_color, (0, 0, 1000, 20))
                pygame.draw.rect(self.disp, self.panel_color, (0, 580, 1000, 600))
                pygame.draw.rect(self.disp, self.panel_color, (980, 0, 600, 1000))

                if self.mod == 1:
                    pygame.draw.rect(self.disp, (90, 90, 90), (100, 0, 220, 20))
                else:
                    pygame.draw.rect(self.disp, (90, 90, 90), (320, 0, 420, 20))

                pygame.draw.line(self.disp, (0, 0, 0), [320, 0], [320, 20], 3)
                self.disp.blit(self.text, (250-self.o, -4))
                self.disp.blit(self.text_2, (488-self.o, -4))
                self.disp.blit(self.text_3, (1, 39))
                self.disp.blit(self.text_4, (1, 59))
                self.disp.blit(self.text_5, (1, 79))
                self.disp.blit(self.text_6, (1, 119))
                self.disp.blit(self.text_7, (1, 159))
                self.disp.blit(self.text_8, (1, 179+20))
                self.disp.blit(self.text_9, (1, 199+20))
                self.disp.blit(self.text_10, (1, 219+20))
                self.disp.blit(self.text_11, (1, 219+60))
                self.disp.blit(self.text_12, (1, 219+100))
                #points
                if self.debug:
                    #down
                    pygame.draw.rect(self.disp, (255, 0, 0), (self.anim.snake[0][0]+10, self.anim.snake[0][1]+30, 2, 2))
                    pygame.draw.rect(self.disp, (255, 0, 0), (self.anim.snake[0][0]+10, self.anim.snake[0][1]+50, 2, 2))
                    pygame.draw.rect(self.disp, (255, 0, 0), (self.anim.snake[0][0]+10, self.anim.snake[0][1]+70, 2, 2))
                    pygame.draw.rect(self.disp, (255, 0, 0), (self.anim.snake[0][0]+10, self.anim.snake[0][1]+90, 2, 2))
                    pygame.draw.rect(self.disp, (255, 0, 0), (self.anim.snake[0][0]+10, self.anim.snake[0][1]+110, 2, 2))
                    pygame.draw.rect(self.disp, (255, 0, 0), (self.anim.snake[0][0]+10, self.anim.snake[0][1]+130, 2, 2))
                    #up
                    pygame.draw.rect(self.disp, (255, 0, 0), (self.anim.snake[0][0]+10, self.anim.snake[0][1]-10, 2, 2))
                    pygame.draw.rect(self.disp, (255, 0, 0), (self.anim.snake[0][0]+10, self.anim.snake[0][1]-30, 2, 2))
                    pygame.draw.rect(self.disp, (255, 0, 0), (self.anim.snake[0][0]+10, self.anim.snake[0][1]-50, 2, 2))
                    pygame.draw.rect(self.disp, (255, 0, 0), (self.anim.snake[0][0]+10, self.anim.snake[0][1]-70, 2, 2))
                    pygame.draw.rect(self.disp, (255, 0, 0), (self.anim.snake[0][0]+10, self.anim.snake[0][1]-90, 2, 2))
                    pygame.draw.rect(self.disp, (255, 0, 0), (self.anim.snake[0][0]+10, self.anim.snake[0][1]-110, 2, 2))
                    #right
                    pygame.draw.rect(self.disp, (255, 0, 0), (self.anim.snake[0][0]+30, self.anim.snake[0][1]+10, 2, 2))
                    pygame.draw.rect(self.disp, (255, 0, 0), (self.anim.snake[0][0]+50, self.anim.snake[0][1]+10, 2, 2))
                    pygame.draw.rect(self.disp, (255, 0, 0), (self.anim.snake[0][0]+70, self.anim.snake[0][1]+10, 2, 2))
                    pygame.draw.rect(self.disp, (255, 0, 0), (self.anim.snake[0][0]+90, self.anim.snake[0][1]+10, 2, 2))
                    pygame.draw.rect(self.disp, (255, 0, 0), (self.anim.snake[0][0]+110, self.anim.snake[0][1]+10, 2, 2))
                    pygame.draw.rect(self.disp, (255, 0, 0), (self.anim.snake[0][0]+130, self.anim.snake[0][1]+10, 2, 2))
                    #left
                    pygame.draw.rect(self.disp, (255, 0, 0), (self.anim.snake[0][0]-10, self.anim.snake[0][1]+10, 2, 2))
                    pygame.draw.rect(self.disp, (255, 0, 0), (self.anim.snake[0][0]-30, self.anim.snake[0][1]+10, 2, 2))
                    pygame.draw.rect(self.disp, (255, 0, 0), (self.anim.snake[0][0]-50, self.anim.snake[0][1]+10, 2, 2))
                    pygame.draw.rect(self.disp, (255, 0, 0), (self.anim.snake[0][0]-70, self.anim.snake[0][1]+10, 2, 2))
                    pygame.draw.rect(self.disp, (255, 0, 0), (self.anim.snake[0][0]-90, self.anim.snake[0][1]+10, 2, 2))
                    pygame.draw.rect(self.disp, (255, 0, 0), (self.anim.snake[0][0]-110, self.anim.snake[0][1]+10, 2, 2))
                try:
                    #down
                    self.dot_1 = self.disp.get_at((self.anim.snake[0][0]+10, self.anim.snake[0][1]+33))
                    self.dot_2 = self.disp.get_at((self.anim.snake[0][0]+10, self.anim.snake[0][1]+53))
                    self.dot_3 = self.disp.get_at((self.anim.snake[0][0]+10, self.anim.snake[0][1]+73))
                    self.dot_4 = self.disp.get_at((self.anim.snake[0][0]+10, self.anim.snake[0][1]+93))
                    self.dot_5 = self.disp.get_at((self.anim.snake[0][0]+10, self.anim.snake[0][1]+113))
                    self.dot_6 = self.disp.get_at((self.anim.snake[0][0]+10, self.anim.snake[0][1]+133))
                    #up
                    self.dot_1_1 = self.disp.get_at((self.anim.snake[0][0]+10, self.anim.snake[0][1]-10))
                    self.dot_2_1 = self.disp.get_at((self.anim.snake[0][0]+10, self.anim.snake[0][1]-30))
                    self.dot_3_1 = self.disp.get_at((self.anim.snake[0][0]+10, self.anim.snake[0][1]-50))
                    self.dot_4_1 = self.disp.get_at((self.anim.snake[0][0]+10, self.anim.snake[0][1]-70))
                    self.dot_5_1 = self.disp.get_at((self.anim.snake[0][0]+10, self.anim.snake[0][1]-90))
                    self.dot_6_1 = self.disp.get_at((self.anim.snake[0][0]+10, self.anim.snake[0][1]-110))
                    #right
                    self.dot_1_2 = self.disp.get_at((self.anim.snake[0][0]+30, self.anim.snake[0][1]+10))
                    self.dot_2_2 = self.disp.get_at((self.anim.snake[0][0]+50, self.anim.snake[0][1]+10))
                    self.dot_3_2 = self.disp.get_at((self.anim.snake[0][0]+70, self.anim.snake[0][1]+10))
                    self.dot_4_2 = self.disp.get_at((self.anim.snake[0][0]+90, self.anim.snake[0][1]+10))
                    self.dot_5_2 = self.disp.get_at((self.anim.snake[0][0]+110, self.anim.snake[0][1]+10))
                    self.dot_6_2 = self.disp.get_at((self.anim.snake[0][0]+130, self.anim.snake[0][1]+10))
                    #left
                    self.dot_1_3 = self.disp.get_at((self.anim.snake[0][0]-10, self.anim.snake[0][1]+10))
                    self.dot_2_3 = self.disp.get_at((self.anim.snake[0][0]-30, self.anim.snake[0][1]+10))
                    self.dot_3_3 = self.disp.get_at((self.anim.snake[0][0]-50, self.anim.snake[0][1]+10))
                    self.dot_4_3 = self.disp.get_at((self.anim.snake[0][0]-70, self.anim.snake[0][1]+10))
                    self.dot_5_3 = self.disp.get_at((self.anim.snake[0][0]-90, self.anim.snake[0][1]+10))
                    self.dot_6_3 = self.disp.get_at((self.anim.snake[0][0]-110, self.anim.snake[0][1]+10))
                except:
                    pass


                self.outputs = data.data(
                    self.dot_1,
                    self.dot_2,
                    self.dot_3,
                    self.dot_4,
                    self.dot_5,
                    self.dot_6,

                    self.dot_1_1,
                    self.dot_2_1,
                    self.dot_3_1,
                    self.dot_4_1,
                    self.dot_5_1,
                    self.dot_6_1,

                    self.dot_1_2,
                    self.dot_2_2,
                    self.dot_3_2,
                    self.dot_4_2,
                    self.dot_5_2,
                    self.dot_6_2,

                    self.dot_1_3,
                    self.dot_2_3,
                    self.dot_3_3,
                    self.dot_4_3,
                    self.dot_5_3,
                    self.dot_6_3,
                )

                pygame.display.update()
                self.disp.fill((33, 33, 33))
                #print(self.outputs)


if __name__ == '__main__':
    game = Game()
    game.game(True)
