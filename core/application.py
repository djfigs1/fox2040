import badger2040
from core.painter import Painter

class Application:
    def __init__(self, window):
        self._display = badger2040.Badger2040()
        self._painter = Painter(self._display)
        self._screen_rect = Painter.create_display_rect()
        self._window = window

    def run(self):
        self._draw()

        while True:
            self._display.keepalive()
            self._display.halt()

    def _draw(self):
        self._display.clear()
        self._window.draw(self._painter, self._screen_rect)
        self._display.update()


