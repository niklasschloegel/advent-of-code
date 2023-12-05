import { parse } from "https://deno.land/std@0.119.0/flags/mod.ts";

let debugEnabled = false;

function debug(...data: any[]) {
  if (debugEnabled) {
    console.log(...data);
  }
}

// ----------------------------- SOLUTION CODE -----------------------------
interface RevealedCubes {
  red: number;
  green: number;
  blue: number;
}
const colors: (keyof RevealedCubes)[] = ["red", "green", "blue"];

interface Game {
  id: number;
  revealedCubes: RevealedCubes[];
}

function parseGame(line: string): Game {
  const gamePrefix = "Game ";
  const idSeparator = ":";
  const separatorIndex = line.indexOf(idSeparator);
  const id = parseInt(line.substring(gamePrefix.length, separatorIndex));

  const gameContent = line.substring(separatorIndex + 1);
  const draws = gameContent.trim().split(";");
  const revealedCubes = draws.map((draw) =>
    draw.trim().split(",").reduce<RevealedCubes>(
      (revealedCubes, revelation) => {
        const [amount, color] = revelation.trim().split(" ");
        return { ...revealedCubes, [color]: parseInt(amount) };
      },
      { red: 0, green: 0, blue: 0 },
    )
  );
  return { id, revealedCubes };
}

function findMax(
  color: keyof RevealedCubes,
  revealedCubes: RevealedCubes[],
): number {
  let max = 0;
  for (const cubes of revealedCubes) {
    const amount = cubes[color];
    if (amount > max) {
      max = amount;
    }
  }
  return max;
}

function solve(data: string): string {
  const games = data.split("\n").map(parseGame);
  return games.map((game) =>
    colors.map((color) => findMax(color, game.revealedCubes)).reduce(
      (pow, max) => pow * max,
      1,
    )
  ).reduce((powSum, pow) => pow + powSum, 0).toString();
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
