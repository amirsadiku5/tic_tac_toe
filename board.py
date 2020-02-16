class Board:
    _EMPTY = ' '
    CIRCLE = 'o'
    CROSS = 'x'

    def __init__(self):
        # This creates a matrix of space strings of dimensions 3x3
        self._board_state = [[Board._EMPTY for _ in range(3)] for _ in range(3)]

    def set_position(self, position: str, value: str):
        """
        Sets a position on the board
        :param position: Position on the board, for example 'b2'
        :param value: Value to be set, either circle or cross
        :return: True if the position was successfully set, false otherwise
        """
        if (len(position) != 2) or (value not in [Board.CIRCLE, Board.CROSS]):
            return False

        try:
            row, column = self._get_position(position)
            if self._board_state[row][column] == Board._EMPTY:
                self._board_state[row][column] = value
                return True

        except ValueError:
            pass

        return False

    def is_win(self, position: str):
        """
        Calculates if a given position corresponds to a winning position
        :param position: Position in string format (for example "a1")
        :return: True if the position is a win, False otherwise
        """
        try:
            row_idx, col_idx = self._get_position(position)
        except ValueError:
            return False

        full_row = self._board_state[row_idx]
        full_column = [row[col_idx] for row in self._board_state]

        if self._is_winning_line(full_row) or self._is_winning_line(full_column):
            return True

        first_diagonal_indices = [(idx, idx) for idx in range(3)]
        second_diagonal_indices = [(idx, 2 - idx) for idx in range(3)]
        if (row_idx, col_idx) in first_diagonal_indices:
            diagonal = [self._board_state[r][c] for r, c in first_diagonal_indices]
            return self._is_winning_line(diagonal)

        if (row_idx, col_idx) in second_diagonal_indices:
            diagonal = [self._board_state[r][c] for r, c in second_diagonal_indices]
            return self._is_winning_line(diagonal)

        return False

    def is_full(self):
        """
        Determines whether all positions of the board have been used
        :return: True if the board is full, False otherwise
        """
        linear_board = [c for row in self._board_state for c in row]
        return all(c != Board._EMPTY for c in linear_board)

    @staticmethod
    def _is_winning_line(line):
        if len(line) == 0:
            return False

        return all((val == line[0]) and (val != Board._EMPTY) for val in line)

    @staticmethod
    def _get_position(position: str):
        """
        Calculates the row and column from a position string
        :return: A tuple with the position
        :raises: ValueException if the position is not in the right format
        """
        row = 'abc'.index(position[0].lower())
        column = '123'.index(position[1])
        return row, column

    def __str__(self):
        """
        :return: A string representation of the current state of the board
        """
        def to_line(matrix_row):
            return f'|{matrix_row[0]:^3} | {matrix_row[1]:^3} | {matrix_row[2]:^3}|'

        board_lines = [to_line(line) for line in self._board_state]
        separator_line = ''.join(['-' for c in board_lines[0]])

        # Create the leading position strings (A, B, C)
        left_chars = '  A B C '
        leading_strings = [f'{c:3}' for c in left_chars]

        # Create the string at the top that indicates (1, 2, 3), note that we don't want the | characters
        top_string = to_line([1, 2, 3]).replace('|', ' ')

        rows = [top_string] + board_lines
        separators = [separator_line] * 4
        separated_rows = _interleave([rows, separators])

        rows_with_leading_positions = [''.join(tup) for tup in zip(leading_strings, separated_rows)]

        return '\n'.join(rows_with_leading_positions)


def _interleave(list_of_lists):
    """
    Takes a list of lists in the form [[a,b,c], [d,e,f], [g,h,i]]
    and produces a single interleaved list: [a,d,g,b,e,h,c,f,i]
    :param list_of_lists: A list of lists to interleave
    :return: A single interleaved list
    """
    return [value for tup in zip(*list_of_lists) for value in tup]
