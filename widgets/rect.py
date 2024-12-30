class Rect:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    @staticmethod
    def of_size(width, height):
        return Rect(0, 0, width, height)

    def top_split(self, length, gap_length=0):
        return self.vertical_flex([length, -1], gap_length)

    def bottom_split(self, length, gap_length=0):
        return self.vertical_flex([-1, length], gap_length)

    def left_split(self, length, gap_length=0):
        return self.horizontal_flex([length, -1], gap_length)

    def right_split(self, length, gap_length=0):
        return self.horizontal_flex([-1, length], gap_length)

    def gap(self, length):
        return self.padding(length, length, length, length)

    def gap_rects(self, length):
        return self.padding_rects(length, length, length, length)

    def padding(self, top=0, bottom=0, left=0, right=0):
        vertical_padding = top + bottom
        horizontal_padding = left + right
        new_x = self.x + left
        new_y = self.y + top
        new_width = self.width - horizontal_padding
        new_height = self.height - vertical_padding

        return Rect(new_x, new_y, new_width, new_height)

    def padding_rects(self, top=0, bottom=0, left=0, right=0):
        vertical_padding = top + bottom
        lr_height = self.height - vertical_padding
        lr_start_y = self.y + top

        top = Rect(self.x, self.y, self.width, top)

        bottom_start_y = self.y + (self.height - bottom)
        bottom = Rect(self.x, bottom_start_y, self.width, bottom)

        left = Rect(self.x, lr_start_y, left, lr_height)

        right_start_x = self.x + (self.width - right)
        right = Rect(right_start_x, lr_start_y, right, lr_height)

        return top, bottom, left, right

    def vertical_split(self, number_splits, gap_length=0):
        return self.vertical_flex([-1] * number_splits, gap_length)

    def horizontal_split(self, number_splits, gap_length=0):
        return self.horizontal_flex([-1] * number_splits, gap_length)

    def vertical_flex(self, flexes, gap_length=0):
        new_rects = []
        for y, length in Rect._split_segments(self.y, self.height, flexes, gap_length):
            rect = Rect(self.x, y, self.width, length)
            new_rects.append(rect)

        return new_rects

    def horizontal_flex(self, flexes, gap_length=0):
        new_rects = []
        for x, length in Rect._split_segments(self.x, self.width, flexes, gap_length):
            rect = Rect(x, self.y, length, self.height)
            new_rects.append(rect)

        return new_rects

    @staticmethod
    def _split_segments(start, total_length, flexes, gap_length=0):
        x = start
        segments = []
        total_gap_length = max(len(flexes) - 1, 0) * gap_length
        total_length -= total_gap_length

        for length in Rect._split_lengths(total_length, flexes):
            segments.append((x, length))
            x += length + gap_length

        return segments

    @staticmethod
    def _split_lengths(total_length, flexes):
        total_flex = 0
        total_fixed = 0

        for val in flexes:
            if val < 0:
                val = -val
                total_flex += val
            else:
                total_fixed += val

        flex_length = total_length - total_fixed

        lengths = []
        for val in flexes:
            length = None

            if val < 0:
                val = -val
                flex_percentage = val / total_flex
                length = flex_percentage * flex_length
            else:
                length = val

            lengths.append(length)

        return lengths

    def __repr__(self):
        s = f"Rect({self.x}, {self.y}, {self.width}, {self.height})"

        return s
