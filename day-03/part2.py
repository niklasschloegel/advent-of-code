from functools import reduce

MODE_OXYGEN = "OXYGEN"
MODE_CO2 = "C02"


def find_rating(lst, mode):
    offset = 0
    while len(lst) != 1:
        curr_bits = list(map(lambda l: l[offset:offset+1], lst))

        one_cnt = reduce(lambda acc, curr: acc +
                         (curr == "1"), list(curr_bits), 0)
        zero_cnt = len(curr_bits) - one_cnt

        if (mode == MODE_OXYGEN and one_cnt >= zero_cnt) or (mode == MODE_CO2 and one_cnt < zero_cnt):
            # keep numbers with ones in current position
            lst = [l for l in lst if l[offset:].startswith("1")]
        else:
            # keep zeros
            lst = [l for l in lst if l[offset:].startswith("0")]

        offset += 1

    return int(lst[0], 2)


with open("input.txt") as input_file:
    numbers = input_file.read().splitlines()

    possible_oxygen_ratings = numbers.copy()
    possible_co2_ratings = numbers.copy()

    ox_rating = find_rating(possible_oxygen_ratings, MODE_OXYGEN)
    o2_rating = find_rating(possible_co2_ratings, MODE_CO2)
    life_support_rating = ox_rating * o2_rating

    print(ox_rating, o2_rating)
    print(life_support_rating)
