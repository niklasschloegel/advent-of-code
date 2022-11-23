def dict_find_index_by_value(dictionary, val):
    return list(dictionary.keys())[list(dictionary.values()).index(val)]


class HeightMap:
    def __init__(self, file_path):
        self.lows = {}
        with open(file_path) as input_file:
            self.width = None
            self.heightmap = []
            for i in input_file.read().splitlines():
                line = [int(j) for j in list(i)]
                self.heightmap.append(line)
                if not self.width:
                    self.width = len(line)
            self.height = len(self.heightmap)

    def __repr__(self):
        repr_str = ""
        for h in self.heightmap:
            repr_str += " ".join(str(i) for i in h)
            repr_str += "\n"
        return repr_str

    def find_neighbours(self, x, y):
        neighbours = {}
        if y > 0:
            neighbours[(x, y - 1)] = self.heightmap[y - 1][x]
        if y < self.height - 1:
            neighbours[(x, y + 1)] = self.heightmap[y + 1][x]
        if x > 0:
            neighbours[(x - 1, y)] = self.heightmap[y][x - 1]
        if x < self.width - 1:
            neighbours[(x + 1, y)] = self.heightmap[y][x + 1]
        return neighbours

    def find_low(self, startx=0, starty=0):
        for y in range(starty, self.height):
            for x in range(startx, self.width):
                neighbours = self.find_neighbours(x, y)
                min_neighbour = min(neighbours.values())
                curr = self.heightmap[y][x]
                if min_neighbour <= curr:
                    new_x, new_y = dict_find_index_by_value(neighbours, min_neighbour)
                    return self.find_low(startx=new_x, starty=new_y)
                else:
                    return x, y, curr

    def gen_lows(self):
        for y in range(self.height):
            for x in range(self.width):
                xpos, ypos, low = self.find_low(startx=x, starty=y)
                self.lows[(xpos, ypos)] = low
        return list(self.lows.values())

    def gen_risk_level_sum(self):
        lows = self.gen_lows()
        return sum([l + 1 for l in lows])


def main():
    height_map = HeightMap("input.txt")
    print(height_map.gen_risk_level_sum())


if __name__ == "__main__":
    main()
