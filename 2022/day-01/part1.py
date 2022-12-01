with open("input.txt") as input_file:
    lines = input_file.read().splitlines()

    elves = []
    while "" in lines:
        seperator_idx = lines.index("")
        elve = sum([int(e) for e in lines[:seperator_idx]])
        elves.append(elve)
        lines = lines[seperator_idx+1:]
    
    if len(lines):
        elve = sum([int(e) for e in lines])
        elves.append(elve)
    
    print(max(elves))
