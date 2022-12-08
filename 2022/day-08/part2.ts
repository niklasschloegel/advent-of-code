import { parse } from "https://deno.land/std@0.119.0/flags/mod.ts";

let debugEnabled = false;

function debug(...data: any[]) {
  if (debugEnabled) {
    console.log(...data);
  }
}

// ----------------------------- SOLUTION CODE -----------------------------
class Grid2D {
  values: number[][];

  constructor(str: string) {
    this.values = str.split("\n").reduce(
      (arr, currentDigit) => [
        ...arr,
        currentDigit.split("").map((d) => parseInt(d)),
      ],
      [] as number[][],
    );
  }

  get numbersAround(): number {
    const n = this.values.length;
    return n + 2 * (n - 1) + (n - 2);
  }

  getNeighboursTRBL(x: number, y: number): (number | undefined)[] {
    return [
      this.getTop(x, y),
      this.getRight(x, y),
      this.getBottom(x, y),
      this.getLeft(x, y),
    ];
  }

  getTop(x: number, y: number): number | undefined {
    if (y > 0) {
      return this.values[y - 1][x];
    }
  }

  getTopRow(x: number, y: number): number[] {
    const numbers: number[] = [];
    let n = y - 1;
    while (n >= 0) {
      numbers.push(this.values[n][x]);
      n--;
    }
    return numbers;
  }

  getRight(x: number, y: number): number | undefined {
    if (x < this.values.length - 1) {
      return this.values[y][x + 1];
    }
  }

  getRightRow(x: number, y: number): number[] {
    const numbers: number[] = [];
    let n = x + 1;
    while (n <= this.values.length - 1) {
      numbers.push(this.values[y][n]);
      n++;
    }
    return numbers;
  }

  getBottom(x: number, y: number): number | undefined {
    if (y < this.values.length - 1) {
      return this.values[y + 1][x];
    }
  }

  getBottomRow(x: number, y: number): number[] {
    const numbers: number[] = [];
    let n = y + 1;
    while (n <= this.values.length - 1) {
      numbers.push(this.values[n][x]);
      n++;
    }
    return numbers;
  }

  getLeft(x: number, y: number): number | undefined {
    if (x >= 0) {
      return this.values[y][x - 1];
    }
  }

  getLeftRow(x: number, y: number): number[] {
    const numbers: number[] = [];
    let n = x - 1;
    while (n >= 0) {
      numbers.push(this.values[y][n]);
      n--;
    }
    return numbers;
  }

  getNeighbourRowsTRBL(x: number, y: number): number[][] {
    return [
      this.getTopRow(x, y),
      this.getRightRow(x, y),
      this.getBottomRow(x, y),
      this.getLeftRow(x, y),
    ];
  }

  toString(): string {
    return this.values.map((v) => v.join(" ")).join("\n\n");
  }
}
function solve(data: string): string {
  const grid = new Grid2D(data);

  const scenicScores = [];
  for (const [y, row] of grid.values.slice(1, -1).entries()) {
    for (const [x, col] of row.slice(1, -1).entries()) {
      const _x = x + 1;
      const _y = y + 1;
      const neighbourRows = grid.getNeighbourRowsTRBL(_x, _y);

      const score = neighbourRows.map((r) =>
        Math.max(
          0,
          r.findIndex((n, i, arr) => n >= col || i === arr.length - 1) + 1,
        )
      ).reduce<
        number
      >(
        (s, current) => s * (current ?? 1),
        1,
      );
      scenicScores.push(score);
    }
  }

  return `${Math.max(...scenicScores)}`;
}
// --------------------------- END SOLUTION CODE ---------------------------

async function main() {
  const flags = parse(Deno.args, {
    boolean: ["d"],
    string: ["f"],
    default: {
      debug: false,
    },
    alias: {
      d: "debug",
      f: "filename",
    },
  });

  const { debug, filename } = flags;
  debugEnabled = debug;
  const data = await Deno.readTextFile(filename);

  const solution = solve(data);
  console.log(solution);
}

await main();
