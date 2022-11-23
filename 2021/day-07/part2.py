from functools import reduce

with open("input.txt") as input_file:
    nums = [int(n) for n in input_file.read().split(",")]
    fuel_vals = []
    for i in range(min(nums), max(nums) + 1):
        fuel = 0
        for n in nums:
            dist = abs(i - n)
            step = sum(range(dist))
            fuel += dist + step
        fuel_vals.append(fuel)
    print(min(fuel_vals))
