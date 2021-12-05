
from typing import List, Tuple
import numpy as np
from functools import reduce


class Line:

    def __init__(self, start: Tuple[int, int], end: Tuple[int, int]):
        self.x1, self.y1 = start
        self.x2, self.y2 = end

        if self.x1 == self.x2:
            self.m = None
            self.n = None
            if self.y2 < self.y1:
                self.x1, self.x2 = self.x2, self.x1
                self.y1, self.y2 = self.y2, self.y1
            self.points = [(self.x1, y) for y in range(self.y1, self.y2+1)]
        else:
            if self.x2 < self.x1:
                self.x1, self.x2 = self.x2, self.x1
                self.y1, self.y2 = self.y2, self.y1
            self.m = (self.y2 - self.y1) / (self.x2 - self.x1)
            self.n = self.y1 - (self.m * self.x1)

            x = self.x1
            y = self.y1
            self.points = []
            while (self.x1 <= x <= self.x2):
                self.points.append((x, y))
                x += 1
                y = (self.m * x) + self.n

    def __repr__(self) -> str:
        return f'Line ({self.x1}, {self.y1}), ({self.x2}, {self.y2})'


class Diagram:

    def __init__(self, lines: List[Line]):
        self.points = [p for sub in list(
            map(lambda l: l.points, lines)) for p in sub]
        self.minx = min(self.points, key=lambda p: p[0])[0]
        self.maxx = max(self.points, key=lambda p: p[0])[0]
        self.miny = min(self.points, key=lambda p: p[1])[1]
        self.maxy = max(self.points, key=lambda p: p[1])[1]
        self.dia = [list(l) for l in list(
            np.full((int(self.minx+self.maxx+1), int(self.miny+self.maxy+1)), 0, dtype=int))]

        for y, x in self.points:
            self.dia[int(x)][int(y)] += 1

    def __repr__(self) -> str:
        repr_str = ""
        for row in self.dia:
            repr_str += " ".join([repr(f) for f in row]) + "\n"
        return repr_str

    def overlap_sum(self):
        return reduce(lambda acc, curr: acc + (curr > 1), [p for sub in self.dia for p in sub])


with open("input.txt") as input_file:
    lines = []
    for l in input_file.read().splitlines():
        p1, p2 = l.split("->")
        x1, y1 = [int(p) for p in p1.strip().split(",")]
        x2, y2 = [int(p) for p in p2.strip().split(",")]
        line = Line((x1, y1), (x2, y2))
        if x1 == x2 or line.m in [-1, 0, 1]:
            #print(line, line.points)
            lines.append(line)
    diagram = Diagram(lines)
    #print(diagram)
    print(diagram.overlap_sum())

