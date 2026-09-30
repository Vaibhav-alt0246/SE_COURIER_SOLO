import unittest
from contextlib import redirect_stdout
from io import StringIO
from unittest.mock import patch

from board import Board
from game import DotsAndBoxes


class DefensiveAddLineTests(unittest.TestCase):
    def test_defensive_value_error_does_not_change_state_or_end_game(self):
        game = DotsAndBoxes(board_size=2)
        missing = ("H", 0, 0)
        for orientation, row_count, col_count in (
            ("H", game.board.rows + 1, game.board.cols),
            ("V", game.board.rows, game.board.cols + 1),
        ):
            for row in range(row_count):
                for col in range(col_count):
                    if (orientation, row, col) != missing:
                        game.board.add_line(orientation, row, col)

        game.scores = [2, 1]
        game.current = 1
        lines_before = (tuple(map(tuple, game.board.horizontal)), tuple(map(tuple, game.board.vertical)))
        completed_before = set(game.board.completed)
        scores_before = list(game.scores)
        current_before = game.current
        snapshots = []
        original_add_line = game.board.add_line
        calls = 0

        def raise_once_then_add(orientation, row, col):
            nonlocal calls
            calls += 1
            if calls == 1:
                snapshots.append(
                    (
                        tuple(map(tuple, game.board.horizontal)),
                        tuple(map(tuple, game.board.vertical)),
                        set(game.board.completed),
                        list(game.scores),
                        game.current,
                    )
                )
                raise ValueError("defensive rejection")
            return original_add_line(orientation, row, col)

        with patch.object(game.board, "add_line", side_effect=raise_once_then_add):
            with patch("builtins.input", side_effect=["H 0 0", "H 0 0"]):
                with redirect_stdout(StringIO()) as output:
                    game.run()

        self.assertIn("Invalid or already-used move.", output.getvalue())
        self.assertEqual(calls, 2)
        self.assertEqual(
            snapshots[0],
            (lines_before[0], lines_before[1], completed_before, scores_before, current_before),
        )
        self.assertTrue(game.board.is_complete())
        self.assertEqual(sum(game.scores), 4)


if __name__ == "__main__":
    unittest.main()
