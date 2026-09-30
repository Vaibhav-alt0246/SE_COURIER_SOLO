def valid_move(board, orientation, row, col):
    if orientation not in {"H", "V"}:
        return False

    line_rows, line_cols = board.line_dimensions(orientation)
    if not (0 <= row < line_rows and 0 <= col < line_cols):
        return False

    lines = board.horizontal if orientation == "H" else board.vertical
    return not lines[row][col]


def completed_boxes(board, before):
    return len(board.completed - before)
