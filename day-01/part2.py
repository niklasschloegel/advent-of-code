with open("input.txt") as input_file:
    lines = input_file.read().splitlines()
    sums = [sum(list(map(lambda x: int(x), lines[i:i+3])))
            for i in range(len(lines)-2)]

    increase_count = 0
    for i, l in enumerate(sums):
        if i == 0:
            continue
        if int(l) > int(sums[i-1]):
            increase_count += 1

    print("{} sums are larger than the previous ones".format(increase_count))
