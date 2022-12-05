def is_pressed(event):
    # butpos - button upper left corner (x, y)
    # w, h - button width and height
    px, py = event.pos
    return bool(butpos[0] <= px <= butpos[0] + w and butpos[1] <= py <= butpos[1] + h)