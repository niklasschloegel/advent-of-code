from argparse import ArgumentParser
from typing import List

debug_enabled = False


def debug(out: str):
    if debug_enabled:
        print(out)


# ----------------------------- SOLUTION CODE -----------------------------
# opponent: A=rock, B=paper, C=scissors

win_turns = {
    "X": {"win": "C", "draw": "A", "score": 1},  # rock
    "Y": {"win": "A", "draw": "B", "score": 2},  # paper
    "Z": {"win": "B", "draw": "C", "score": 3},  # scissors
}


def solve(data: List[str]) -> str:
    total_score = 0
    for l in data:
        opponent, mine = l.split(" ")
        turn = win_turns[mine]

        score = turn["score"]
        if turn["win"] == opponent:
            score += 6
        elif turn["draw"] == opponent:
            score += 3
        total_score += score

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
