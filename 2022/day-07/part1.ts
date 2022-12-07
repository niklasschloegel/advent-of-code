import { parse } from "https://deno.land/std@0.119.0/flags/mod.ts";

let debugEnabled = false;

function debug(...data: any[]) {
  if (debugEnabled) {
    console.log(...data);
  }
}

// ----------------------------- SOLUTION CODE -----------------------------

const threshold = 100_000;

function solve(data: string): string {
  const pwd: string[] = [];
  const dirSizes: { [dir: string]: number } = {};

  function increaseSize(dir: string, size: number) {
    if (dirSizes[dir]) {
      dirSizes[dir] += size;
    } else {
      dirSizes[dir] = size;
    }
  }

  data.split("\n").forEach((line) => {
    const currentDir = pwd.join("/");

    if (line.startsWith("$")) {
      const command = line.split(" ");
      if (command[1] === "cd") {
        const goalDir = command[2];
        if (goalDir === "..") {
          pwd.pop();
        } else {
          pwd.push(goalDir);
        }
      }
    } else if (!line.startsWith("dir")) {
      const size = parseInt(line.split(" ")[0]);
      increaseSize(currentDir, size);

      const parentDirs = [...pwd];
      while (parentDirs.length) {
        const dir = parentDirs.join("/");
        if (dir !== currentDir) {
          increaseSize(dir, size);
        }
        parentDirs.pop();
      }
    }
    debug(pwd);
  });

  debug(dirSizes);
  return Object.values(dirSizes).reduce((sum, currentSize) => {
    if (currentSize <= threshold) {
      return sum + currentSize;
    }
    return sum;
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
