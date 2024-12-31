class SocialBattery:
    def __init__(self):
        self.level = 2

    def draw(self, painter, rect):
        rect = rect.gap(12)
        rect = painter.draw_border(rect, 4, 0)

        segments = rect.horizontal_split(3)
        segments = [painter.draw_border(segment, 2, 2) for segment in segments]
        segments = [segment.gap(2) for segment in segments]

        if self.level == 0:
            paint_level = 6
        elif self.level == 1:
            paint_level = 3
        else:
            paint_level = 0

        for i in range(self.level + 1):
            painter.draw_rect(segments[i], paint_level)

        return 2

    def update(self, input_state):
        new_level = None

        if input_state.a:
            new_level = 0
        elif input_state.b:
            new_level = 1
        elif input_state.c:
            new_level = 2

        should_update = new_level is not None and new_level != self.level
        if should_update:
            self.level = new_level

        return should_update
