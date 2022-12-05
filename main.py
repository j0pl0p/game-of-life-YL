import pygame as pg
import pygame.mouse
from pygame.locals import *


class Board:
    def __init__(self):
        self.matrix = [[bool, ...], ...]

    def get_cell(self, coords: (int, int)) -> (int, int):
        pass

    def set_life(self, event: pg.event):
        if event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            if event.button == 1:
                self.matrix[self.get_cell(pos)] = True
            elif event.button == 3:
                self.matrix[self.get_cell(pos)] = False
