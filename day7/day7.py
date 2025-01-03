from time import perf_counter
from equation import Equation, Operator


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


def part1(equations: list[Equation]):
    total = 0

    operators: set[Operator] = {'+', '*'}

    for equation in equations:
        if equation.test_equation(operators):
            total += equation.target

    print("part 1:", total)


def part2(equations: list[Equation]):
    total = 0

    operators: set[Operator] = {'+', '*', '||'}

    for equation in equations:
        if equation.test_equation(operators):
            total += equation.target

    print("part 2:", total)


def main():
    filename = "day7/input.txt"

    start = perf_counter()
    equations = read_input(filename)
    end = perf_counter()
    print(f"read input: {round((end-start) * 1000)}ms")

    start = perf_counter()
    part1(equations)
    end = perf_counter()
    print(f"part 1: {round((end-start) * 1000)}ms")

    start = perf_counter()
    part2(equations)
    end = perf_counter()
    print(f"part 2: {round((end-start) * 1000)}ms")


if __name__ == "__main__":
    main()
