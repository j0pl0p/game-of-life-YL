class Board:
    # создание поля
    def __init__(self, width, height):
        self.size = self.width, self.height = width, height
        self.matrix = [[False] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 10

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
