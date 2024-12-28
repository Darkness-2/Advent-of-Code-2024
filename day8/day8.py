from itertools import combinations
from time import perf_counter


type Coordinate = tuple[int, int]
type AntennaDict = dict[str, set[Coordinate]]


def read_input(filename: str):
    antennas: AntennaDict = dict()
    with open(filename, 'r') as f:
        row = -1
        while line := f.readline():
            row += 1
            line = line.strip()
            cols = len(line)

            for col, char in enumerate(line):
                if char.isdigit() or char.islower() or char.isupper():
                    antenna_set = antennas.setdefault(char, set())
                    antenna_set.add((row, col))

    rows = row + 1

    return antennas, rows, cols


def part1(antennas: AntennaDict, rows: int, cols: int):
    antinodes: set[Coordinate] = set()

    # Create all pairs of antennas of same type and check their antinode positions
    for antenna_type in antennas.keys():
        for a, b in combinations(antennas[antenna_type], 2):
            x_1, y_1 = a
            x_2, y_2 = b

            x_delta = x_2 - x_1
            y_delta = y_2 - y_1

            # Create the two antinodes
            x_3, y_3 = x_2 + x_delta, y_2 + y_delta
            x_4, y_4 = x_1 - x_delta, y_1 - y_delta

            # Check they are in bounds and add
            if 0 <= x_3 < rows and 0 <= y_3 < cols:
                antinodes.add((x_3, y_3))

            if 0 <= x_4 < rows and 0 <= y_4 < cols:
                antinodes.add((x_4, y_4))

    print("part 1:", len(antinodes))


def part2():
    print("part 2:", 0)


def main():
    filename = "day8/input.txt"

    start = perf_counter()
    antennas, rows, cols = read_input(filename)
    end = perf_counter()
    print(f"read input: {round((end-start) * 1000)}ms")

    start = perf_counter()
    part1(antennas, rows, cols)
    end = perf_counter()
    print(f"part 1: {round((end-start) * 1000)}ms")

    start = perf_counter()
    part2()
    end = perf_counter()
    print(f"part 2: {round((end-start) * 1000)}ms")


if __name__ == "__main__":
    main()
