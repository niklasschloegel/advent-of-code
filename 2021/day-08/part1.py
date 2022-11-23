OUTPUT_PATTERNS = {
    0: "abcefg",
    1: "cf",
    2: "acdeg",
    3: "acdfg",
    4: "bcdf",
    5: "abdfg",
    6: "abdefg",
    7: "acf",
    8: "abcdefg",
    9: "abcdfg",
}

with open("input.txt") as input_file:
    lines = input_file.read().splitlines()

    signal_patterns = []
    ouput_values = []
    for l in lines:
        sp, ov = l.split("|")
        signal_patterns.extend(sp.split())
        ouput_values.extend(ov.split())

    count = {i: 0 for i in OUTPUT_PATTERNS.keys()}
    for o in ouput_values:
        for k, v in OUTPUT_PATTERNS.items():
            if len(v) == len(o):
                count[k] += 1
    print(count)
    print(count[1] + count[4] + count[7] + count[8])
