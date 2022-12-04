from argparse import ArgumentParser

debug_enabled = False


def debug(*out: str):
    if debug_enabled:
        print(*out)


# ----------------------------- SOLUTION CODE -----------------------------


def solve(data: str) -> str:
    count = 0
    for l in data.splitlines():
        left, right = l.split(",")
        llb, lrb = [int(n) for n in left.split("-")]
        lrange = [*range(llb, lrb + 1)]
        rlb, rrb = [int(n) for n in right.split("-")]
        rrange = [*range(rlb, rrb + 1)]

        for ln in lrange:
            if ln in rrange:
                count += 1
                break

    return f"{count}"


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
