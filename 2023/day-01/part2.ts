import { parse } from "https://deno.land/std@0.119.0/flags/mod.ts";

let debugEnabled = false;

function debug(...data: any[]) {
  if (debugEnabled) {
    console.log(...data);
  }
}

// ----------------------------- SOLUTION CODE -----------------------------
const wordNumLUT = {
  one: "1",
  two: "2",
  three: "3",
  four: "4",
  five: "5",
  six: "6",
  seven: "7",
  eight: "8",
  nine: "9",
};

function solve(data: string): string {
  return data.split("\n")
    .map((line) => {
      let minIndex = line.length - 1;
      let maxIndex = 0;
      let firstDigit!: string;
      let lastDigit!: string;
      for (const [word, digit] of Object.entries(wordNumLUT)) {
        const wordMatchFirstIndex = line.indexOf(word);
        const digitMatchFirstIndex = line.indexOf(digit);
        if (wordMatchFirstIndex >= 0 || digitMatchFirstIndex >= 0) {
          const localMinIndex =
            wordMatchFirstIndex >= 0 && digitMatchFirstIndex >= 0
              ? Math.min(wordMatchFirstIndex, digitMatchFirstIndex)
              : (
                wordMatchFirstIndex >= 0
                  ? wordMatchFirstIndex
                  : digitMatchFirstIndex
              );

          if (localMinIndex < minIndex) {
            firstDigit = digit;
            minIndex = localMinIndex;
          }
        }

        const wordMatchLastIndex = line.lastIndexOf(word);
        const digitMatchLastIndex = line.lastIndexOf(digit);
        if (wordMatchLastIndex < 0 && digitMatchLastIndex < 0) {
          continue;
        }

        const localMaxIndex =
          wordMatchLastIndex >= 0 && digitMatchLastIndex >= 0
            ? Math.max(wordMatchLastIndex, digitMatchLastIndex)
            : (
              wordMatchLastIndex >= 0 ? wordMatchLastIndex : digitMatchLastIndex
            );
        if (localMaxIndex > maxIndex) {
          lastDigit = digit;
          maxIndex = localMaxIndex;
        }
        debug(line);
        debug(firstDigit, lastDigit);
      }
      if (!firstDigit) return parseInt(`${lastDigit}${lastDigit}`);
      if (!lastDigit) return parseInt(`${firstDigit}${firstDigit}`);
      return parseInt(`${firstDigit}${lastDigit}`);
    })
    .reduce((sum, num) => num + sum, 0).toString();
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
