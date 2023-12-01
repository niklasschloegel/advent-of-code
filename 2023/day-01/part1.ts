import { parse } from "https://deno.land/std@0.119.0/flags/mod.ts";

let debugEnabled = false;

function debug(...data: any[]) {
  if (debugEnabled) {
    console.log(...data);
  }
}

// ----------------------------- SOLUTION CODE -----------------------------
function solve(data: string): string {
  return data.split("\n").map((line) => line.split("")).map((charArray) => {
    const firstDigit = charArray.find((char) => !!parseInt(char));
    const lastDigit = charArray.findLast((char) => !!parseInt(char));
    if (!firstDigit || !lastDigit) {
      throw new Error("Line does not have two digits");
    }
    return parseInt(`${firstDigit}${lastDigit}`);
  }).reduce((sum, num) => num + sum, 0).toString();
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
