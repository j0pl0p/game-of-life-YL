class Board:
    # создание поля
    def __init__(self, width, height):
        self.size = self.width, self.height = width, height
        self.matrix = [[False] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 10

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size