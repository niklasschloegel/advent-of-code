def calc_total_length(array_2d):
    length = 0
    for i, _ in enumerate(array_2d):
        length += len(array_2d[i])
    return length


class Octo:
    def __init__(self, filename):
        with open(filename) as file_input:
            self.grid = [
                [int(s) for s in list(l)] for l in file_input.read().splitlines()
            ]
        self.flashes = 0
        self.size = len(self.grid)
        self.current_flashes = []

    def __repr__(self):
        repr_str = ""
        for y in self.grid:
            repr_str += " ".join([str(l) for l in y])
            repr_str += "\n"
        return repr_str

    def _get_value(self, x, y):
        return self.grid[y][x]

    def _set_value(self, x, y, value):
        self.grid[y][x] = value

    def get_neighbours(self, x, y):
        neighbours = []

        if y > 0 and x > 0:  # top-left
            neighbours.append((x - 1, y - 1))
        if y > 0:  # top
            neighbours.append((x, y - 1))
        if x < self.size - 1 and y > 0:  # top-right
            neighbours.append((x + 1, y - 1))
        if x > 0:  # left
            neighbours.append((x - 1, y))
        if x < self.size - 1:  # right
            neighbours.append((x + 1, y))
        if x > 0 and y < self.size - 1:  # bottom-left
            neighbours.append((x - 1, y + 1))
        if y < self.size - 1:  # bottom
            neighbours.append((x, y + 1))
        if y < self.size - 1 and x < self.size - 1:  # bottom-right
            neighbours.append((x + 1, y + 1))
        return neighbours

    def _flash(self, x, y):
        if (x, y) in self.current_flashes:
            return

        self.flashes += 1
        self.current_flashes.append((x, y))
        self._set_value(x, y, 0)

        for (nx, ny) in self.get_neighbours(x, y):
            if (nx, ny) not in self.current_flashes:
                self.step(nx, ny, True)

    def step(self, x, y, flash=False):
        previous_value = self._get_value(x, y)
        if flash and previous_value >= 9:
            self._flash(x, y)
        else:
            self._set_value(x, y, previous_value + 1)

    def check_flash(self, x, y):
        if self._get_value(x, y) > 9:
            self._flash(x, y)

    def run(self, func):
        for y in range(self.size):
            for x in range(self.size):
                func(x, y)

    def simulate(self):
        t = 0
        while True:
            t += 1
            self.run(self.step)
            self.run(self.check_flash)
            if len(self.current_flashes) == self.size**2:
                print("Simultaneous flash at", t)
                return
            self.current_flashes = []


def main():
    o = Octo("input.txt")
    print(o)
    o.simulate()
    print("times flashed:", o.flashes)
    print(o)


main()
