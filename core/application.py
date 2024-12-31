import badger2040
from core.painter import Painter
from core.input_state import InputState


class Application:
    def __init__(self, window, screen_rect=None):
        self._display = badger2040.Badger2040()
        self._painter = Painter(self._display)
        self._screen_rect = (
            screen_rect if screen_rect is not None else Painter.create_display_rect()
        )
        self._update_speed = 0
        self._window = window

    def run(self):
        # Initial draw
        self._draw()

        while True:
            self._display.keepalive()
            self._update()
            self._display.halt()

    def _draw(self):
        self._display.clear()

        requested_update_speed = self._window.draw(self._painter, self._screen_rect)
        update_speed = (
            requested_update_speed if requested_update_speed else self._update_speed
        )

        self._display.set_update_speed(update_speed)
        self._display.update()

    def _update(self):
        input_state = InputState.from_display(self._display)
        needs_redraw = self._window.update(input_state)

        if needs_redraw:
            self._draw()
