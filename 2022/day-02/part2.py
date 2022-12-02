from argparse import ArgumentParser
from typing import List

debug_enabled = False


def debug(out: str):
    if debug_enabled:
        print(out)


# ----------------------------- SOLUTION CODE -----------------------------
# opponent: A=rock, B=paper, C=scissors

turns = {
    "X": {"A": 3, "B": 1, "C": 2},  # rock – lose
    "Y": {"A": 4, "B": 5, "C": 6},  # paper – draw
    "Z": {"A": 8, "B": 9, "C": 7},  # scissors – win
}


def solve(data: List[str]) -> str:
    total_score = 0
    for l in data:
        opponent, mine = l.split(" ")
        turn = turns[mine]
        total_score += turn[opponent]

    return f"{total_score}"


# --------------------------- END SOLUTION CODE ---------------------------


def main():
    parser = ArgumentParser(description="Solve AoC puzzles")
    parser.add_argument("filename")
    parser.add_argument("-d", "--debug", action="store_true", default=False)

    args = vars(parser.parse_args())
    if not args:
        parser.print_help()
    else:
        file_name = args["filename"]
        global debug_enabled
        debug_enabled = args["debug"]

        with open(file_name) as data:
            solution = solve(data.read().splitlines())
            print(solution)


if __name__ == "__main__":
    main()
