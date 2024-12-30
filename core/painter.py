import badger2040
from core.rect import Rect


class Painter:
    def __init__(self, display):
        self.display = display

    @staticmethod
    def create_display_rect():
        return Rect.of_size(badger2040.WIDTH, badger2040.HEIGHT)

    def fill_black(self, rect):
        self.draw_rect(rect, 0)

    def fill_white(self, rect):
        self.draw_rect(rect, 15)

    def draw_border(self, rect, length, color=-1):
        top, bottom, left, right = rect.gap_rects(length)
        self.draw_rect(top, color)
        self.draw_rect(bottom, color)
        self.draw_rect(left, color)
        self.draw_rect(right, color)

        return rect.gap(length)

    def draw_rect(self, rect, color=-1):
        if color > -1:
            self.display.set_pen(color)

        self.display.rectangle(
            round(rect.x), round(rect.y), round(rect.width), round(rect.height)
        )
