import pygame.mouse
from pygame.locals import *
from Board import Board

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Main window")
    size = width, height = 1500, 800
    screen = pygame.display.set_mode(size)
    running = True
    fps = 100
    clock = pygame.time.Clock()
    b_color = (0, 0, 0)

    board = Board(20, 20)

    while running:
        screen.fill(b_color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        board.render(screen)
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
