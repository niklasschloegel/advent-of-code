with open("input.txt") as input_file:
    fish = [int(n) for n in input_file.read().split(",")]
    max_days = 80
    day = 0
    while day < max_days:
        new_fish_indices = []
        for i, f in enumerate(fish):
            fish[i] -= 1
            if f <= 0:
                fish[i] = 6
                new_fish_indices.append(i + 1)

        for ni in new_fish_indices:
            fish.insert(ni, 8)

        day += 1
    print(len(fish))
