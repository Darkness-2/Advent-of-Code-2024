from time import perf_counter
from grid import Grid, TileType
from guard import Guard


def read_input(filename: str):
    grid = Grid()
    guard: Guard | None = None

    with open(filename, 'r') as f:
        line = f.readline()

        while len(line):
            line = line.strip()

            row: list[TileType] = []

            for c in line:
                if c == '.':
                    row.append('.')
                elif c == "#":
                    row.append('#')
                elif c == "^":
                    # Create a guard
                    x, y = len(grid.grid), len(row)
                    guard = Guard(x, y, "up")

                    # Mark spot as visited
                    grid.reset_grid(guard)

                    row.append('.')
                else:
                    raise ValueError("Tried to parse non ., #, ^ character.")

            grid.grid.append(row)

            line = f.readline()

    if guard is None:
        raise TypeError("Guard was not present in input.")

    return grid, guard


def part1(grid: Grid, guard: Guard):
    # Move guard while possible
    while guard.on_map:
        guard.move_guard(grid)

    # Calculate tiles visited
    tiles_visited = 0

    for i, row in enumerate(grid.grid):
        for j, tile in enumerate(row):
            if (i, j) in grid.visited:
                tiles_visited += 1

    print("part 1:", tiles_visited)


def part2(grid: Grid, guard: Guard):
    # Only try positions on original visited spots
    valid_positions = 0
    positions_to_try = grid.visited

    for (row, col) in positions_to_try:
        # Reset the grid and guard
        guard.reset_guard()
        grid.reset_grid(guard)

        # Ignore if starting guard spot
        if row == guard.row and col == guard.col:
            continue

        # Test the position and see if it contains a cycle
        grid.grid[row][col] = '#'

        while guard.on_map:
            cycle_found = guard.move_guard(grid)

            if cycle_found:
                valid_positions += 1
                break

        # Reset grid
        grid.grid[row][col] = '.'

    print("part 2:", valid_positions)


def main():
    filename = "day6/input.txt"

    start = perf_counter()
    grid, guard = read_input(filename)
    end = perf_counter()
    print(f"read input: {round((end-start) * 1000)}ms")

    start = perf_counter()
    part1(grid, guard)
    end = perf_counter()
    print(f"part 1: {round((end-start) * 1000)}ms")

    start = perf_counter()
    part2(grid, guard)
    end = perf_counter()
    print(f"part 2: {round((end-start) * 1000)}ms")


if __name__ == "__main__":
    main()
