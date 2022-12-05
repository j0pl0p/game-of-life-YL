import pygame as pg
import pygame.mouse
from pygame.locals import *
from copy import deepcopy


class Board:
    # создание поля
    def __init__(self, width, height):
        self.size = self.width, self.height = width, height
        self.matrix = [[False] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def get_cell(self, pos):
        '''pos: (width_pixel, height_pixel)
        return None, None если клетка не в поле'''
        width, height = pos
        width -= self.left
        height -= self.top
        if (0 <= width <= self.width * self.cell_size
                and 0 <= height <= self.height * self.cell_size):
            return width // self.cell_size, height // self.cell_size
        return None, None

    def set_life(self, event: pg.event) -> None:
        if event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            x, y = self.get_cell(pos)
            if x is not None and y is not None:
                if event.button == 1:
                    self.matrix[x][y] = True
                elif event.button == 3:
                    self.matrix[x][y] = False

    def render(self, screen):
        '''рисует доску на экране screen'''
        for i in range(self.height):
            for j in range(self.width):
                if self.matrix[i][j]:
                    pygame.draw.rect(screen, (250, 250, 250),
                                     (i * self.cell_size,
                                      j * self.cell_size,
                                      self.cell_size,
                                      self.cell_size))
                else:
                    pygame.draw.rect(screen, (250, 250, 250),
                                     (i * self.cell_size,
                                      j * self.cell_size,
                                      self.cell_size,
                                      self.cell_size), 2)

    def next_cell_gen(self, x: int, y: int) -> bool:
        neighbors = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if x != 0 or y != 0:
                    try:
                        neighbors += self.matrix[x + i][y + j]
                    except IndexError:
                        continue
        if self.matrix[x][y]:
            return neighbors == 2 or neighbors == 3
        else:
            return neighbors == 3

    def next_gen(self) -> None:
        matrix = []
        for i in range(self.width):
            matrix.append([])
            for j in range(self.height):
                matrix[i].append(self.next_cell_gen(i, j))
        self.matrix = deepcopy(matrix)
