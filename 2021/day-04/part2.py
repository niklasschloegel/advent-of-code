from functools import reduce
from typing import List


class Field:

    def __init__(self, val: int):
        self.val = val
        self.marked = False

    def __repr__(self) -> str:
        repr_str = f'{self.val}'
        if self.marked:
            repr_str += "*"
        return repr_str

    def mark(self):
        self.marked = True


class Board:

    def __init__(self, text_rows: List[str]):
        self.board: List[List[Field]] = []
        for row in text_rows:
            field_row = [Field(int(r)) for r in row.split()]
            self.board.append(field_row)

    def __repr__(self) -> str:
        repr_str = ""
        for row in self.board:
            repr_str += "\t".join([repr(f) for f in row]) + "\n"
        return repr_str

    def check(self, num) -> bool:
        for row in self.board:
            for field in row:
                if field.val == num:
                    field.mark()
                    if self._check_win():
                        return True

    def calc_non_marked_sum(self) -> int:
        return reduce(lambda acc, curr: acc + (curr.val if not curr.marked else 0), [f for sub in self.board for f in sub], 0)

    def _check_win(self) -> bool:
        return self._check_rows() or self._check_cols()

    def _check_rows(self) -> bool:
        return self._check_lst(self.board)

    def _check_cols(self) -> bool:
        return self._check_lst(list(map(list, zip(*self.board))))  # transposed

    def _check_lst(self, lst) -> bool:
        for row in lst:
            row_cnt = 0
            for field in row:
                row_cnt += field.marked
            if row_cnt == 5:
                return True
        return False


class Game:

    def __init__(self, draw_numbers: List[int], boards: List[Board]) -> None:
        self.draw_numbers = draw_numbers
        self.boards = boards

    def __repr__(self) -> str:
        repr_str = f'{repr(self.draw_numbers)}\n\n'
        repr_str += "\n".join([repr(b) for b in self.boards])
        return repr_str

    def play(self):
        winners = []
        for d in self.draw_numbers:
            curr_winners = self._step(d)
            if len(curr_winners):
                winners.extend(curr_winners)
                last_winner = None
                for w in curr_winners:
                    self.boards.remove(w)
                    last_winner = w
                if len(self.boards) == 0:
                    print(last_winner)
                    non_marked_sum = last_winner.calc_non_marked_sum()
                    print(
                        f'{non_marked_sum} unmarked * {d} current number = {non_marked_sum*d}')

    def _step(self, num) -> Board:
        winners = []
        for b in self.boards:
            if b.check(num):
                winners.append(b)
        return winners


with open("input.txt") as input_file:
    input_vals = input_file.read().splitlines()
    draw_nums = [int(i) for i in input_vals[0].split(",")]

    boards = []
    text_rows = []
    for i, inp in enumerate(input_vals):
        if i < 2:
            continue
        if i == len(input_vals)-1:
            text_rows.append(inp)
        if inp == "" or i == len(input_vals)-1:
            boards.append(Board(text_rows))
            text_rows = []
            continue
        text_rows.append(inp)

    game = Game(draw_nums, boards)
    game.play()
