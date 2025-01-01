from time import perf_counter

from helpers import calculate_stones_after_x_moves


def read_input(filename: str):
    with open(filename, 'r') as f:
        stones = [int(x) for x in f.readline().split()]

    return stones


def part1(stones: list[int]):
    count = calculate_stones_after_x_moves(stones, 25)
    print("part 1:", count)


def part2(stones: list[int]):
    count = calculate_stones_after_x_moves(stones, 75)
    print("part 2:", count)


def main():
    filename = "day11/input.txt"

    start = perf_counter()
    stones = read_input(filename)
    end = perf_counter()
    print(f"read input: {round((end-start) * 1000)}ms")

    start = perf_counter()
    part1(stones)
    end = perf_counter()
    print(f"part 1: {round((end-start) * 1000)}ms")

    start = perf_counter()
    part2(stones)
    end = perf_counter()
    print(f"part 2: {round((end-start) * 1000)}ms")


if __name__ == "__main__":
    main()
