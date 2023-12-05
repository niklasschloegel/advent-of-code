import { parse } from "https://deno.land/std@0.119.0/flags/mod.ts";

let debugEnabled = false;

function debug(...data: any[]) {
  if (debugEnabled) {
    console.log(...data);
  }
}

// ----------------------------- SOLUTION CODE -----------------------------
const colors = ["red", "green", "blue"] as const;

interface RevealedCubes {
  red: number;
  green: number;
  blue: number;
}

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

function solve(data: string): string {
  const games = data.split("\n").map(parseGame);
  const maxRed = 12;
  const maxGreen = 13;
  const maxBlue = 14;
  return games.filter((game) =>
    game.revealedCubes.every(({ red, green, blue }) =>
      red <= maxRed && green <= maxGreen && blue <= maxBlue
    )
  ).map((game) => game.id)
    .reduce((sum, id) => sum + id, 0);
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
