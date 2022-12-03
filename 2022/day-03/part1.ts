import { parse } from "https://deno.land/std@0.119.0/flags/mod.ts";

let debugEnabled = false;

function debug(...data: any[]) {
  if (debugEnabled) {
    console.log(...data);
  }
}

// ----------------------------- SOLUTION CODE -----------------------------
const letters: { [letter: string]: number } = [
  ...Array.from(
    { length: 26 },
    (_, i) => String.fromCharCode("a".charCodeAt(0) + i),
  ),
  ...Array.from(
    { length: 26 },
    (_, i) => String.fromCharCode("A".charCodeAt(0) + i),
  ),
].reduce((obj, letter, index) => ({ ...obj, [letter]: index + 1 }), {});

function solve(data: string): string {
  return data.split("\n").reduce((sum, rucksack) => {
    const items = rucksack.split("");
    const a = items.slice(0, items.length / 2);
    const b = items.slice(items.length / 2);

    const duplicates = a.reduce((all, item) => {
      if (b.includes(item) && !all.includes(item)) {
        return [...all, item];
      }
      return all;
    }, [] as string[]);

    return sum + duplicates.reduce(
      (pSum, letter) => letters[letter] + pSum,
      0,
    );
  }, 0).toString();
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
