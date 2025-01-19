from turtle import position


class Robot:
    p_x = -1
    p_y = -1
    v_x = -1
    v_y = -1

    def __init__(self, pos: tuple[int, int], velo: tuple[int, int]):
        self.p_x = pos[0]
        self.p_y = pos[1]
        self.v_x = velo[0]
        self.v_y = velo[1]

    def __repr__(self) -> str:
        return f"p={self.p_x},{self.p_y} v={self.v_x},{self.v_y}"

    def move_robot(self, moves: int, bounds: tuple[int, int]):
        x_movement = self.v_x * moves
        y_movement = self.v_y * moves

        self.p_x += x_movement
        self.p_y += y_movement

        # Ensure placed within bounds
        self.adjust_placement_in_bounds(bounds)

    def adjust_placement_in_bounds(self, bounds: tuple[int, int]):
        r_x = self.p_x % bounds[0]
        r_y = self.p_y % bounds[1]

        self.p_x = r_x
        self.p_y = r_y

    def determine_quadrant(self, bounds: tuple[int, int]):
        """
        Returns 0 for top-left, 1 for top-right, 2 for bottom-left, 3 for bottom-right, 4 for in the middle.
        """
        mid_x = bounds[0] / 2
        mid_y = bounds[1] / 2

        left_half = self.p_x < mid_x - 1
        right_half = self.p_x > mid_x

        top_half = self.p_y < mid_y - 1
        bottom_half = self.p_y > mid_y

        if left_half and top_half:
            return 0

        if right_half and top_half:
            return 1

        if left_half and bottom_half:
            return 2

        if right_half and bottom_half:
            return 3

        return 4


def calculate_safety_factor(quadrants: list[int]):
    return quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]


def generate_positions_dict(robots: list[Robot]):
    positions: dict[tuple[int, int], int] = {}

    # Sum robots at each spot
    for robot in robots:
        positions.setdefault((robot.p_x, robot.p_y), 0)
        positions[(robot.p_x, robot.p_y)] += 1

    return positions


def print_robot_grid(positions: dict[tuple[int, int], int], bounds: tuple[int, int]):
    # Print grid
    for y in range(bounds[1]):
        for x in range(bounds[0]):
            if (x, y) not in positions:
                print(" ", end="")
            else:
                print(positions[(x, y)], end="")

        print("")
