class Navigator:
    BAR_WIDTH = 10

    def __init__(self, pages=None):
        self.pages = [] if not pages else pages
        self._page_index = 0

    def add_page(self, window):
        self.pages.append(window)

    def clear(self):
        self.pages = []

    def next_page(self):
        self._page_index = (self._page_index + 1) % len(self.pages)

    def prev_page(self):
        self._page_index = (self._page_index - 1) % len(self.pages)

    def draw(self, painter, rect):
        painter.fill_white(rect)
        top, bottom = rect.bottom_split(Navigator.BAR_WIDTH, 2)
        top = painter.draw_border(top, 2, 0)
        painter.draw_rect(bottom, 10)

        if len(self.pages) > 0:
            window = self._get_current_page()
            return window.draw(painter, top)

    def _get_current_page(self):
        return self.pages[self._page_index]

    def update(self, input_state):
        return self._get_current_page().update(input_state)