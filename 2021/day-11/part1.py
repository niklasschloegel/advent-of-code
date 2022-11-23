class Octo:
    def __init__(self, filename):
        with open(filename) as file_input:
            self.grid = [
                [int(s) for s in list(l)] for l in file_input.read().splitlines()
            ]
        self.flashes = 0
        self.size = len(self.grid)

    def __repr__(self):
        repr_str = ""
        for y in self.grid:
            repr_str += " ".join([str(l) for l in y])
            repr_str += "\n"
        return repr_str

    def get_neighbors(self, x, y):
        neighbours = {}
        if y > 0:  # t
            neighbours[(x, y - 1)] = self.grid[y - 1][x]
            if x > 0:  # tl
                neighbours[(x - 1, y - 1)] = self.grid[y - 1][x - 1]
        if y < self.size - 1:  # b
            neighbours[(x, y + 1)] = self.grid[y + 1][x]
            if x < self.size - 1:  # br
                neighbours[(x + 1, y + 1)] = self.grid[y + 1][x + 1]
        if x > 0:  # l
            neighbours[(x - 1, y)] = self.grid[y][x - 1]
            if y < self.size - 1:  # bl
                neighbours[(x - 1, y + 1)] = self.grid[y + 1][x - 1]
        if x < self.size - 1:  # r
            neighbours[(x + 1, y)] = self.grid[y][x + 1]
            if y > 0:  # tr
                neighbours[(x + 1, y - 1)] = self.grid[y - 1][x + 1]
        return neighbours

    def flash(self, x, y, curr_flashes=[]):
        if (x, y) in curr_flashes:
            return curr_flashes
        self.flashes += 1
        curr_flashes.append((x, y))
        vals = self.get_neighbors(x, y)
        for (vx, vy), v in vals.items():
            self.grid[vy][vx] += 1
            if v >= 9:
                return self.flash(vx, vy, curr_flashes)

    def step(self):
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                self.grid[y][x] += 1
                if self.grid[y][x] > 9:
                    flashes = self.flash(x, y, [])
                    if flashes:
                        for (fx, fy) in flashes:
                            self.grid[fy][fx] = 0

    def simulate(self, n):
        for _ in range(n):
            self.step()


def main():
    o = Octo("simple.txt")
    o.simulate(100)
    print(o.flashes)
    print(o)


main()
