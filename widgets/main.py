from widgets.painter import Painter
from widgets.navigator import Navigator
import badger2040

display = badger2040.Badger2040()
painter = Painter(display)
navigator = Navigator()
screen_rect = Painter.create_display_rect()

display.clear()

navigator.draw(painter, screen_rect)

display.update()

while True:
    # Sometimes a button press or hold will keep the system
    # powered *through* HALT, so latch the power back on.
    display.keepalive()

    # If on battery, halt the Badger to save power, it will wake up if any of the front buttons are pressed
    display.halt()
