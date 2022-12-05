import pygame
import pygame.mouse
from Board import Board


def draw_text(screen, size):
    screen.fill("black")
    font = pygame.font.Font(None, 50)
    text = font.render("Жизнь", True, (100, 255, 100))
    wid = text.get_width()
    x, y = size[0] // 2 - wid // 2, size[1] // 2 - size[1] // 5
    screen.blit(text, (x, y))


def draw_button(screen, size):
    x, y = size[0] // 2 - size[0] // 5, size[1] // 2 + size[1] // 5
    x1, y1 = 2 * size[0] // 5, size[1] // 5
    pygame.draw.rect(screen, (100, 255, 100), (x, y, x1, y1))


def is_pressed(event, butpos, pos):
    # butpos - button upper left corner (x, y)
    # w, h - button width and height
    w, h = pos[0], pos[1]
    px, py = event.pos
    return bool(butpos[0] <= px <= butpos[0] + w and butpos[1] <= py <= butpos[1] + h)


pygame.init()
size = (600, 800)
screen = pygame.display.set_mode(size)
x1, y1, x2, y2 = 300, 300, 500, 400
not_exit = True
while not_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            not_exit = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = size[0] // 2 - size[0] // 5, size[1] // 2 + size[1] // 5
            x1, y1 = 2 * size[0] // 5, size[1] // 5
            is_pressed(event, (x, y), (x1, y1))
    draw_text(screen, size)
    draw_button(screen, size)
    pygame.display.flip()

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
        board.next_gen()
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
