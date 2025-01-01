from time import perf_counter

from helpers import Coordinate, Grid, count_corners, dfs


def read_input(filename: str):
    grid: Grid = []

    with open(filename, 'r') as f:
        while line := f.readline().strip():
            grid.append(line)

    return grid


def part1(grid: Grid):
    total_price = 0
    visited: set[Coordinate] = set()

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # Skip if already visited
            if (i, j) in visited:
                continue

            # Otherwise perform DFS to find the region
            local_visited, area, perimeter = dfs(grid, (i, j))

            # Don't visit these again as they're accounted for
            visited.update(local_visited)

            total_price += area * perimeter

    print("part 1:", total_price)


def part2(grid: Grid):
    total_price = 0
    visited: set[Coordinate] = set()

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # Skip if already visited
            if (i, j) in visited:
                continue

            # Otherwise perform DFS to find the region
            local_visited, area, _ = dfs(grid, (i, j))

            # Don't visit these again as they're accounted for
            visited.update(local_visited)

            # Calculate number of corners
            corners = count_corners(local_visited)

            total_price += area * corners

    print("part 2:", total_price)


def main():
    filename = "day12/input.txt"

    start = perf_counter()
    grid = read_input(filename)
    end = perf_counter()
    print(f"read input: {round((end-start) * 1000)}ms")

    start = perf_counter()
    part1(grid)
    end = perf_counter()
    print(f"part 1: {round((end-start) * 1000)}ms")

    start = perf_counter()
    part2(grid)
    end = perf_counter()
    print(f"part 2: {round((end-start) * 1000)}ms")


if __name__ == "__main__":
    main()
