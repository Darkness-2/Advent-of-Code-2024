from time import perf_counter

from helpers import Coordinate, Grid, dfs, modified_bfs


def read_input(filename: str):
    """
    Input is m row x n col grid.
    O(m*n)
    """

    grid: Grid = []
    trailheads: set[Coordinate] = set()

    with open(filename, 'r') as f:
        # Each line is a row in the grid
        while line := f.readline():
            line = line.strip()

            row: list[int] = []

            # Each char in the line is a position
            for pos in line:
                pos = int(pos)
                row.append(pos)

                # Keep track of trailheads
                if pos == 0:
                    trailheads.add((len(grid), len(row) - 1))

            grid.append(row)

    return grid, trailheads


def part1(grid: Grid, trailheads: set[Coordinate]):
    """
    O(m*n*trailheads) = at worst O(m*n*m*n) = O(m^2n^2)
    """
    total = 0

    # For each trailhead, perform dfs and count nines
    for trailhead in trailheads:
        _, nines = dfs(grid, trailhead)
        total += len(nines)

    print("part 1:", total)


def part2(grid: Grid, trailheads: set[Coordinate]):
    """
    O(m*n*trailheads) = at worst O(m*n*m*n) = O(m^2n^2)

    Could instead consider finding all paths from each source (0) to each destination (9) via a DAG path counter.
    Probably also possible to do this for part 1.
    Would result in O(m*n) for topo sort + O(m*n) for each pair of source and destination.
    However, there are m*n possible sources/destinations, so likely ends up the same?
    https://www.geeksforgeeks.org/number-of-paths-from-source-to-destination-in-a-directed-acyclic-graph/
    """
    total = 0

    # For each trailhead, perform a modified bfs and count total paths
    for trailhead in trailheads:
        paths = modified_bfs(grid, trailhead)
        total += paths

    print("part 2:", total)


def main():
    filename = "day10/input.txt"

    start = perf_counter()
    grid, trailheads = read_input(filename)
    end = perf_counter()
    print(f"read input: {round((end-start) * 1000)}ms")

    start = perf_counter()
    part1(grid, trailheads)
    end = perf_counter()
    print(f"part 1: {round((end-start) * 1000)}ms")

    start = perf_counter()
    part2(grid, trailheads)
    end = perf_counter()
    print(f"part 2: {round((end-start) * 1000)}ms")


if __name__ == "__main__":
    main()
