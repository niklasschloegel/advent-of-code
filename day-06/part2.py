with open("input.txt") as input_file:
    fish = {i: 0 for i in range(9)}
    for n in input_file.read().split(","):
        fish[int(n)] += 1

    for i in range(256):
        tmp = {i: 0 for i in range(9)}
        for f, cnt in fish.items():
            if f == 0:
                tmp[6] += cnt
                tmp[8] += cnt
            else:
                tmp[f - 1] += cnt
        fish = tmp

    print(sum(fish.values()))
