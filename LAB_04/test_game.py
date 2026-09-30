import unittest
from contextlib import redirect_stdout
from io import StringIO
from unittest.mock import patch

from board import Board
from game import DotsAndBoxes
from rules import completed_boxes, valid_move


def fill_board(board):
    for row in range(board.rows + 1):
        for col in range(board.cols):
            if valid_move(board, "H", row, col):
                board.add_line("H", row, col)
    for row in range(board.rows):
        for col in range(board.cols + 1):
            if valid_move(board, "V", row, col):
                board.add_line("V", row, col)


class ConfigurableBoardTests(unittest.TestCase):
    def run_complete_game(self, size):
        game = DotsAndBoxes(board_size=size)
        moves = [
            *(f"H {row} {col}" for row in range(size + 1) for col in range(size)),
            *(f"V {row} {col}" for row in range(size) for col in range(size + 1)),
        ]

        with patch("builtins.input", side_effect=moves), redirect_stdout(StringIO()):
            game.run()

        return game

    def test_two_by_two_game_flow_uses_configured_board(self):
        game = self.run_complete_game(2)

        self.assertTrue(game.board.is_complete())
        self.assertEqual((game.board.rows, game.board.cols), (2, 2))
        self.assertEqual(sum(game.scores), 4)

    def test_three_by_three_game_flow_uses_configured_board(self):
        game = self.run_complete_game(3)

        self.assertTrue(game.board.is_complete())
        self.assertEqual((game.board.rows, game.board.cols), (3, 3))
        self.assertEqual(sum(game.scores), 9)

    def test_two_by_two_board_completes_boxes_and_game(self):
        board = Board(rows=2, cols=2)
        before = set(board.completed)

        board.add_line("H", 0, 0)
        board.add_line("H", 1, 0)
        board.add_line("V", 0, 0)
        board.add_line("V", 0, 1)

        self.assertEqual(completed_boxes(board, before), 1)
        self.assertEqual(len(board.horizontal), 3)
        self.assertEqual(len(board.horizontal[0]), 2)
        self.assertEqual(len(board.vertical), 2)
        self.assertEqual(len(board.vertical[0]), 3)

        fill_board(board)
        self.assertTrue(board.is_complete())
        self.assertEqual(board.completed, {(0, 0), (0, 1), (1, 0), (1, 1)})

    def test_three_by_three_board_completes_boxes_and_game(self):
        board = Board(rows=3, cols=3)
        fill_board(board)

        self.assertTrue(board.is_complete())
        self.assertEqual(len(board.completed), 9)
        self.assertEqual(len(board.horizontal), 4)
        self.assertEqual(len(board.horizontal[0]), 3)
        self.assertEqual(len(board.vertical), 3)
        self.assertEqual(len(board.vertical[0]), 4)
        self.assertFalse(valid_move(board, "H", 0, 0))
        self.assertFalse(valid_move(board, "V", 2, 3))

    def test_startup_rejects_invalid_size_then_accepts_valid_size(self):
        game = DotsAndBoxes()

        with patch("builtins.input", side_effect=["1", "six", "3"]):
            self.assertEqual(game._select_board_size(), 3)

        game.board_size = 3
        game.board = Board(3, 3)
        self.assertEqual((game.board.rows, game.board.cols), (3, 3))


class GameFlowTests(unittest.TestCase):
    def test_completing_box_scores_and_keeps_same_player_turn(self):
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

        with patch("builtins.input", side_effect=["H 0 0"]), redirect_stdout(StringIO()) as output:
            game.run()

        self.assertEqual(game.scores, [1, 0])
        self.assertEqual(game.current, 0)
        self.assertIn("plays again", output.getvalue())

    def test_completed_game_prints_game_over_and_stops_input(self):
        game = DotsAndBoxes(board_size=2)
        moves = [
            *(f"H {row} {col}" for row in range(3) for col in range(2)),
            *(f"V {row} {col}" for row in range(2) for col in range(3)),
        ]

        with patch("builtins.input", side_effect=moves) as input_mock:
            with redirect_stdout(StringIO()) as output:
                game.run()

        self.assertTrue(game.board.is_complete())
        self.assertIn("Game over!", output.getvalue())
        self.assertEqual(input_mock.call_count, len(moves))


if __name__ == "__main__":
    unittest.main()
