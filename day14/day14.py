import re
from time import perf_counter

from helpers import Robot, calculate_safety_factor, generate_positions_dict, print_robot_grid


def read_input(filename: str):
    regex = r'p=(\d+),(\d+) v=(-?\d+),(-?\d+)'

    robots: list[Robot] = []

    with open(filename, 'r') as f:
        while line := f.readline().strip():
            re_match = re.match(regex, line)

            if re_match is None:
                raise TypeError("Could not match regex.")

            p_x, p_y = re_match.group(1, 2)
            v_x, v_y = re_match.group(3, 4)

            p_x, p_y = int(p_x), int(p_y)
            v_x, v_y = int(v_x), int(v_y)

            robots.append(Robot((p_x, p_y), (v_x, v_y)))

    return robots


def part1(robots: list[Robot], bounds: tuple[int, int], moves: int):
    # top-left, top-right, bottom-left, bottom-right, middle
    quadrants = [0, 0, 0, 0, 0]

    for robot in robots:
        robot.move_robot(moves, bounds)
        quadrant = robot.determine_quadrant(bounds)
        quadrants[quadrant] += 1

    print("part 1:", calculate_safety_factor(quadrants))


def part2(robots: list[Robot], bounds: tuple[int, int], moves: int):
    for i in range(moves):
        for robot in robots:
            robot.move_robot(1, bounds)

        positions = generate_positions_dict(robots)

        # Skip if all robots are not in unique positions
        if len(positions) != len(robots):
            continue

        print_robot_grid(positions, bounds)
        print(f"move {i + 1} ^")

    print("part 2:", moves)


def main():
    filename = "day14/input.txt"
    bounds = (101, 103)  # (x, y)

    start = perf_counter()
    robots = read_input(filename)
    end = perf_counter()
    print(f"read input: {round((end-start) * 1000)}ms")

    start = perf_counter()
    part1(robots, bounds, 100)
    end = perf_counter()
    print(f"part 1: {round((end-start) * 1000)}ms")

    robots = read_input(filename)

    start = perf_counter()
    part2(robots, bounds, 10000)
    end = perf_counter()
    print(f"part 2: {round((end-start) * 1000)}ms")


if __name__ == "__main__":
    main()
