with open("input.txt") as input_file:
    scores = []
    for l in input_file.read().splitlines():
        stack = []
        corrupted = False
        for s in list(l):
            if s in ["(", "[", "{", "<"]:
                stack.append(s)
            else:
                pop = stack.pop()
                if (
                    s == ")"
                    and pop != "("
                    or s == "]"
                    and pop != "["
                    or s == "}"
                    and pop != "{"
                    or s == ">"
                    and pop != "<"
                ):
                    corrupted = True
                    break

        if not corrupted:
            score = 0
            for s in stack[::-1]:
                if s == "(":
                    points = 1
                elif s == "[":
                    points = 2
                elif s == "{":
                    points = 3
                else:
                    points = 4
                score = (score * 5) + points
            scores.append(score)
    sorted_scores = sorted(scores)
    print(sorted_scores[len(sorted_scores) // 2])
