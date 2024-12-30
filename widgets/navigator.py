class Navigator:
    BAR_WIDTH = 10

    def __init__(self):
        pass

    def draw(self, painter, rect):
        painter.fill_white(rect)
        top, bottom = rect.bottom_split(Navigator.BAR_WIDTH, 4)
        painter.draw_border(top, 2, 0)
        painter.draw_rect(bottom, 10)