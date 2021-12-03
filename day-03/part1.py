# most common bits
gamma = ""

# least common bits
epsilon = ""

with open("input.txt") as input_file:
    lines = input_file.read().splitlines()
    for row in zip(*lines):
        max_val = max("01", key=row.count)
        gamma += max_val
        epsilon += "0" if max_val == "1" else "1"
    gamma_rate = int(gamma, 2)
    epsilon_rate = int(epsilon, 2)

    power_consumption = gamma_rate * epsilon_rate
    print(power_consumption)
