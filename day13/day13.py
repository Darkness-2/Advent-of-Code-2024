import re
from time import perf_counter
from typing import Final

from helpers import Game


A_BUTTON_COST: Final[int] = 3
B_BUTTON_COST: Final[int] = 1


def read_input(filename: str):
    button_regex = r'X\+(\d+), Y\+(\d+)'
    prize_regex = r'X=(\d+), Y=(\d+)'

    games: list[Game] = []

    with open(filename, 'r') as f:
        while True:
            lines = [f.readline().strip() for _ in range(4)]

            # Exit once done
            if len(lines[0]) == 0:
                break

            button_a_re = re.search(button_regex, lines[0])
            button_b_re = re.search(button_regex, lines[1])
            prize_re = re.search(prize_regex, lines[2])

            if button_a_re is None or button_b_re is None or prize_re is None:
                raise TypeError("Regex reading of game failed.")

            a_x, a_y = button_a_re.group(1, 2)
            b_x, b_y = button_b_re.group(1, 2)
            prize_x, prize_y = prize_re.group(1, 2)

            a_x, a_y = int(a_x), int(a_y)
            b_x, b_y = int(b_x), int(b_y)
            prize_x, prize_y = int(prize_x), int(prize_y)

            games.append(Game((a_x, a_y), (b_x, b_y), (prize_x, prize_y)))

    return games


def part1(games: list[Game]):
    cost = 0

    for game in games:
        (a, b), (r_a, r_b) = game.apply_cramers_rule()

        # Can't have non-integer solutons
        if r_a or r_b:
            continue

        cost += int(a) * A_BUTTON_COST + int(b) * B_BUTTON_COST

    print("part 1:", cost)


def part2(games: list[Game]):
    ADDITION_FACTOR: Final[int] = 10000000000000

    cost = 0

    for game in games:
        # Adjust prize
        game.prize_x = game.prize_x + ADDITION_FACTOR
        game.prize_y = game.prize_y + ADDITION_FACTOR

        (a, b), (r_a, r_b) = game.apply_cramers_rule()

        # Can't have non-integer solutons
        if r_a or r_b:
            continue

        cost += int(a) * A_BUTTON_COST + int(b) * B_BUTTON_COST

    print("part 2:", cost)


def main():
    filename = "day13/input.txt"

    start = perf_counter()
    games = read_input(filename)
    end = perf_counter()
    print(f"read input: {round((end-start) * 1000)}ms")

    start = perf_counter()
    part1(games)
    end = perf_counter()
    print(f"part 1: {round((end-start) * 1000)}ms")

    start = perf_counter()
    part2(games)
    end = perf_counter()
    print(f"part 2: {round((end-start) * 1000)}ms")


if __name__ == "__main__":
    main()
