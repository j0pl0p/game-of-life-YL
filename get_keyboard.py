new_life = True


def get_keyboard(event):
    global running, new_life
    if event.key == pygame.K_SPACE:
        running = False
    if event.key == pygame.K_RETURN:
        running = True
        new_life = not new_life