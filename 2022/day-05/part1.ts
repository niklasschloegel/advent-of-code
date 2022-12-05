import { parse } from "https://deno.land/std@0.119.0/flags/mod.ts";

let debugEnabled = false;

function debug(...data: any[]) {
  if (debugEnabled) {
    console.log(...data);
  }
}

// ----------------------------- SOLUTION CODE -----------------------------
type Stacks = Record<number, string[]>;
class Cargo {
  stacks: Stacks = {};

  createStacks(lines: string[]) {
    lines.forEach((line) => {
      line.split("").forEach((_, index, line) => {
        if (index % 4 === 0) {
          const value = line[index + 1];
          if (value !== " ") {
            this._addToStack(value, (index / 4) + 1);
          }
        }
      });
    });
  }

  move(from: number, to: number, amount: number) {
    const deletedFrom = this.stacks[from].splice(
      this.stacks[from].length - amount,
      amount,
    );
    this.stacks[to].push(...deletedFrom.reverse());
  }

  getTops(): string {
    debug(Object.values(this.stacks));
    return Object.values(this.stacks).reduce((totalString, currentStack) => {
      if (currentStack.length) {
        return totalString + currentStack[currentStack.length - 1];
      }
      return totalString;
    }, "");
  }

  private _addToStack(value: string, index: number) {
    if (this.stacks[index]) {
      this.stacks[index] = [value, ...this.stacks[index]];
    } else {
      this.stacks[index] = [value];
    }
  }
}

function solve(data: string): string {
  const cargo = new Cargo();
  data.split("\n").forEach((line, index, lines) => {
    if (line.length === 0) {
      cargo.createStacks(lines.slice(0, index - 1));
    } else if (line.startsWith("move")) {
      const amount = parseInt(line.split("move ")[1].split(" ")[0]);
      const from = parseInt(line.split("from ")[1].split(" ")[0]);
      const to = parseInt(line.split("to ")[1].split(" ")[0]);
      debug(`move ${amount} from ${from} to ${to}`);
      cargo.move(from, to, amount);
      debug(cargo.stacks);
    }
  });
  debug(cargo.stacks);
  return cargo.getTops();
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
