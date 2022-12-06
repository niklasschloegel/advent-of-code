from argparse import ArgumentParser

debug_enabled = False


def debug(out: str):
    if debug_enabled:
        print(out)


# ----------------------------- SOLUTION CODE -----------------------------


def solve(data: str) -> str:
    count = 0
    for i, char in enumerate(data):
        char_set = {c for c in data[i : i + 14]}
        if len(char_set) == 14:
            return f"{count+14}"
        count += 1


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
            solution = solve(data.read())
            print(solution)


if __name__ == "__main__":
    main()
