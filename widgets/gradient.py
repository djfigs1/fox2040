class Gradient:
    def __init__(self):
        self.use_vertical_splits = True

    def draw(self, painter, rect):
        rects = (
            rect.vertical_split(16)
            if self.use_vertical_splits
            else rect.horizontal_split(16)
        )
        for i in range(16):
            bar = rects[i]
            painter.draw_rect(bar, i)

    def update(self, input_state):
        flip = input_state.a

        if flip:
            self.use_vertical_splits = not self.use_vertical_splits

        return flip
