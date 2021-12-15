with open("input.txt") as input_file:
    err_score = 0
    for l in input_file.read().splitlines():
        stack = []
        for s in list(l):
            if s in ["(", "[", "{", "<"]:
                stack.append(s)
            else:
                pop = stack.pop()
                if s == ")" and pop != "(":
                    err_score += 3
                    break
                elif s == "]" and pop != "[":
                    err_score += 57
                    break
                elif s == "}" and pop != "{":
                    err_score += 1197
                    break
                elif s == ">" and pop != "<":
                    err_score += 25137
                    break
    print(err_score)
