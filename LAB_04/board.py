class Board:
    def __init__(self, rows=2, cols=2):
        self.rows = rows
        self.cols = cols
        self.horizontal = [[False] * cols for _ in range(rows + 1)]
        self.vertical = [[False] * (cols + 1) for _ in range(rows)]
        self.completed = set()

    def line_dimensions(self, orientation):
        """Return the row and column limits for a line orientation."""
        if orientation == "H":
            return self.rows + 1, self.cols
        if orientation == "V":
            return self.rows, self.cols + 1
        raise ValueError("orientation must be 'H' or 'V'")

    def add_line(self, orientation, row, col):
        if orientation not in {"H", "V"}:
            raise ValueError("orientation must be 'H' or 'V'")

        if orientation == "H":
            line_rows, line_cols = self.line_dimensions(orientation)
            if not (0 <= row < line_rows and 0 <= col < line_cols):
                raise ValueError("horizontal line coordinates are out of range")
            if self.horizontal[row][col]:
                raise ValueError("line has already been used")
            self.horizontal[row][col] = True
        else:
            line_rows, line_cols = self.line_dimensions(orientation)
            if not (0 <= row < line_rows and 0 <= col < line_cols):
                raise ValueError("vertical line coordinates are out of range")
            if self.vertical[row][col]:
                raise ValueError("line has already been used")
            self.vertical[row][col] = True
        self._update_completed()

    def _update_completed(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if (
                    self.horizontal[r][c]
                    and self.horizontal[r + 1][c]
                    and self.vertical[r][c]
                    and self.vertical[r][c + 1]
                ):
                    self.completed.add((r, c))

    def is_complete(self):
        total = self.rows * (self.cols + 1) + self.cols * (self.rows + 1)
        used = sum(map(sum, self.horizontal)) + sum(map(sum, self.vertical))
        return used == total

    def display(self, scores, current):
        print()
        print(f"Scores: P1={scores[0]}  P2={scores[1]} | Turn: P{current + 1}")

        for r in range(self.rows + 1):
            print(".".join("---" if self.horizontal[r][c] else "   " for c in range(self.cols)))
            if r < self.rows:
                middle = []
                for c in range(self.cols + 1):
                    wall = "|" if self.vertical[r][c] else " "
                    middle.append(wall)
                    if c < self.cols:
                        middle.append(" " + ("X" if (r, c) in self.completed else " ") + " ")
                print("".join(middle))
        print()
