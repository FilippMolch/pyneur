import pygame
from time import sleep
from spawn import x_rand, y_rand
import py

class Move(object):
    def __init__(self, display, head):
        self.display = display
        self.head = head
        self.x = 0
        self.y = 0
        self.arr_eat = (0, 0)
        self.i = 0

    def ran(self):
        self.x = x_rand()
        self.y = y_rand()

    def draw_eat(self, index):
        if index == 0:
            pygame.draw.rect(self.display, (255, 0, 0), (self.x, self.y, 20, 20))
            self.arr_eat = (self.x, self.y)
        else:
            self.ran()
            pygame.draw.rect(self.display, (255, 0, 0), (self.x, self.y, 20, 20))
            self.arr_eat = (self.x, self.y)


class Anim(object):
    def __init__(self, display, red):
        self.snake = [[120,40],[140,40],[160,40]]
        self.head = [120,40]
        self.x = self.snake[0][0]
        self.y = self.snake[0][1]
        self.green = (0,204,0)
        self.display = display
        self.flag_dir = 'RIGHT'
        self.red = red
        self.x_r = x_rand()
        self.y_r = y_rand()
        self.k = (self.x_r, self.y_r)
        self.eat = []
        self.kok = 0
        self.n = 20

    def draw_snake(self, n, kok):
        self.n = n
        self.kok = kok
        if self.kok == 1:
            if self.flag_dir == 'RIGHT':
                self.head[0] += 20
                sleep(n)
            if self.flag_dir == 'LEFT':
                self.head[0] -= 20
                sleep(n)
            if self.flag_dir == 'UP':
                self.head[1] -= 20
                sleep(n)
            if self.flag_dir == 'DOWN':
                self.head[1] += 20
                sleep(n)

    def anim_snak(self):
        self.snake.insert(0, list(self.head))
        self.snake.pop()

    def eat_sn(self):
        self.snake.insert(0, list(self.head))

    def move(self):
        for i in self.snake:
            pygame.draw.rect(self.display, self.green,(i[0], i[1], 20, 20))

    def sn_dam(self):
        for i in self.snake:
            print(i)
