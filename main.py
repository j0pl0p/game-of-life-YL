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


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Main window")
    size = width, height = 1500, 800
    screen = pygame.display.set_mode(size)
    running = True
    fps = 100
    clock = pygame.time.Clock()
    b_color = (0, 0, 0)
    while running:
        screen.fill(b_color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
