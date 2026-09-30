from board import Board
from rules import valid_move, completed_boxes

class DotsAndBoxes:
    def __init__(self, board_size=None):
        self.board_size = board_size
        self.board = Board(board_size, board_size) if board_size is not None else Board()
        self.current = 0
        self.scores = [0, 0]

    def _select_board_size(self):
        while True:
            raw = input("Choose board size (2-5 boxes per side): ").strip()
            try:
                size = int(raw)
            except ValueError:
                print("Invalid board size. Enter a number from 2 to 5.")
                continue

            if 2 <= size <= 5:
                return size

            print("Invalid board size. Enter a number from 2 to 5.")

    def run(self):
        if self.board_size is None:
            self.board_size = self._select_board_size()
            self.board = Board(self.board_size, self.board_size)

        print("Dots and Boxes")
        print("Enter moves as H row col or V row col.")
        print("Rows and columns start at 0.")
        print("Example: H 0 1")

        while not self.board.is_complete():
            self.board.display(self.scores, self.current)
            raw = input(f"Player {self.current + 1}, move: ").strip().upper()
            parts = raw.split()

            if len(parts) != 3:
                print("Invalid format.")
                continue

            orientation, row, col = parts
            if not row.isdigit() or not col.isdigit():
                print("Row and column must be numbers.")
                continue

            row, col = int(row), int(col)
            if not valid_move(self.board, orientation, row, col):
                print("Invalid or already-used move.")
                continue

            before = set(self.board.completed)
            try:
                self.board.add_line(orientation, row, col)
            except ValueError:
                print("Invalid or already-used move.")
                continue
            newly_completed = completed_boxes(self.board, before)

            if newly_completed:
                self.scores[self.current] += newly_completed
                print(f"Player {self.current + 1} completed {newly_completed} box(es) and plays again.")
            else:
                self.current = 1 - self.current

        self.board.display(self.scores, self.current)
        print("Game over!")
        if self.scores[0] == self.scores[1]:
            print("The game is a draw.")
        else:
            winner = 1 if self.scores[0] > self.scores[1] else 2
            print(f"Player {winner} wins!")
