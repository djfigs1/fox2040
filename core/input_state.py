import badger2040


class InputState:
    def __init__(self, a=False, b=False, c=False, up=False, down=False, user=False):
        self.a = a
        self.b = b
        self.c = c
        self.up = up
        self.down = down
        self.user = user

    @staticmethod
    def from_display(display):
        a_pressed = display.pressed(badger2040.BUTTON_A)
        b_pressed = display.pressed(badger2040.BUTTON_B)
        c_pressed = display.pressed(badger2040.BUTTON_C)
        up_pressed = display.pressed(badger2040.BUTTON_UP)
        down_pressed = display.pressed(badger2040.BUTTON_DOWN)
        user_pressed = display.pressed(badger2040.BUTTON_USER)

        return InputState(
            a_pressed, b_pressed, c_pressed, up_pressed, down_pressed, user_pressed
        )

    def __repr__(self):
        return f"InputState(A={self.a}, B={self.b}, C={self.c}, UP={self.up}, DOWN={self.down}, USR={self.user})"
