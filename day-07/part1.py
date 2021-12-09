from functools import reduce

with open("input.txt") as input_file:
    nums = [int(n) for n in input_file.read().split(",")]
    fuel_vals = [
        reduce(lambda acc, curr: acc + abs(i - curr), nums, 0)
        for i in range(min(nums), max(nums) + 1)
    ]
    print(min(fuel_vals))
