import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('ЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫ')
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
