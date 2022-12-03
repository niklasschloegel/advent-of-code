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
  return data.split("\n")
    .reduce<string[][]>(
      (group, _, index, all) => {
        if (index % 3 === 0) {
          return [...group, all.slice(index, index + 3)];
        }
        return group;
      },
      [],
    )
    .reduce((sum, group) => {
      const commonLetter = group[0].split("").reduce(
        (common, currentLetter) => {
          if (
            group[1].includes(currentLetter) && group[2].includes(currentLetter)
          ) {
            return currentLetter;
          }
          return common;
        },
        "",
      );
      return sum + letters[commonLetter];
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
