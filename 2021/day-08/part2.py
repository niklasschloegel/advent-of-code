SIGNALS = {
    "a": "",
    "b": "",
    "c": "",
    "d": "",
    "e": "",
    "f": "",
    "g": "",
}

#  aaaa
# b    c
# b    c
#  dddd
# e    f
# e    f
#  gggg


def filter_string(string, todelete):
    return string.translate(string.maketrans({c: None for c in todelete}))


def build_pattern(letters):
    return "".join(sorted([SIGNALS[l] for l in letters]))


def determine_signal_patterns(signal_values):
    signal_patterns = {i: "" for i in range(10)}

    for s in sorted(signal_values, key=len):
        sorted_s = "".join(sorted(s))
        if len(s) == 2:
            # pattern for 1
            signal_patterns[1] = sorted_s
        elif len(s) == 3:
            # pattern for 7
            signal_patterns[7] = sorted_s
        elif len(s) == 4:
            # pattern for 4
            signal_patterns[4] = sorted_s
        elif len(s) == 5:
            # 2, 3 or 5
            SIGNALS["a"] = filter_string(signal_patterns[7], signal_patterns[1])
            c_and_f = signal_patterns[1]
            b_and_d = filter_string(signal_patterns[4], signal_patterns[7])

            if SIGNALS["a"] in s and b_and_d[0] in s and b_and_d[1] in s:
                abcdf = signal_patterns[4] + signal_patterns[7]
                SIGNALS["g"] = filter_string(s, abcdf)
                abcdfg = abcdf + SIGNALS["g"]
                SIGNALS["e"] = filter_string("abcdefg", abcdfg)
                signal_patterns[5] = sorted_s
            elif (
                SIGNALS["a"] in s
                and ((c_and_f[0] in s) ^ (c_and_f[1] in s))
                and (b_and_d[0] in s or b_and_d[1] in s)
            ):
                if c_and_f[0] in s:
                    SIGNALS["c"] = c_and_f[0]
                    SIGNALS["f"] = c_and_f[1]
                else:
                    SIGNALS["c"] = c_and_f[1]
                    SIGNALS["f"] = c_and_f[0]

                if b_and_d[0] in s:
                    SIGNALS["d"] = b_and_d[0]
                    SIGNALS["b"] = b_and_d[1]
                else:
                    SIGNALS["d"] = b_and_d[1]
                    SIGNALS["b"] = b_and_d[0]

                signal_patterns[2] = sorted_s

        elif len(s) == 7:
            # pattern for 8
            signal_patterns[8] = sorted_s

    # at this point all signals are identified and
    # the missing signal patterns for 0, 2, 6 and 9 can be built
    # through the signal values

    signal_patterns[0] = build_pattern("abcefg")
    signal_patterns[3] = build_pattern("acdfg")
    signal_patterns[6] = build_pattern("abdefg")
    signal_patterns[9] = build_pattern("abcdfg")
    return signal_patterns


def main():
    with open("input.txt") as input_file:
        lines = input_file.read().splitlines()

        allcount = 0
        for l in lines:
            sv, ov = l.split("|")
            signal_values = sv.split()
            output_values = ov.split()

            signal_patterns = determine_signal_patterns(signal_values)
            cnt = ""
            for o in output_values:
                for num, pattern in signal_patterns.items():
                    if "".join(sorted(o)) == pattern:
                        cnt += str(num)
            if len(cnt) < 4:
                print(signal_patterns)
                print(["".join(sorted(o)) for o in output_values])
                print(l)
                print(cnt)
                print("----------------------------------------")
            allcount += int(cnt)
        print("res:", allcount)


main()
