increase_count = 0

with open("input.txt") as input_file:
    lines = input_file.read().splitlines()
    for i, l in enumerate(lines):
        if i == 0:
            continue
        if int(l) > int(lines[i-1]):
            increase_count += 1


print("{} measurements are larger than the previous one".format(increase_count))
