class Gradient:
    def __init__(self):
        pass

    def draw(self, painter, rect):
        rects = rect.vertical_split(16)
        for i in range(16):
            bar = rects[i]
            painter.draw_rect(bar, i)