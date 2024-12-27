from time import perf_counter
from equation import Equation


def read_input(filename: str):
    equations: list[Equation] = []

    with open(filename, 'r') as f:
        while line := f.readline():
            line = line.strip()

            parts = line.split(":")
            operands = [int(x) for x in parts[1].split()]
            equation = Equation(int(parts[0]), operands)
            equations.append(equation)

    return equations


def part1():
    print("part 1:", 0)


def part2():
    print("part 2:", 0)


def main():
    filename = "day7/sample_input.txt"

    start = perf_counter()
    x = read_input(filename)
    end = perf_counter()
    print(f"read input: {round((end-start) * 1000)}ms")

    start = perf_counter()
    part1()
    end = perf_counter()
    print(f"part 1: {round((end-start) * 1000)}ms")

    start = perf_counter()
    part2()
    end = perf_counter()
    print(f"part 2: {round((end-start) * 1000)}ms")


if __name__ == "__main__":
    main()
