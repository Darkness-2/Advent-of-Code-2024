from typing import Literal, TYPE_CHECKING

if TYPE_CHECKING:
    from grid import Grid


type Facing = Literal["up", "down", "left", "right"]


class Guard:
    # Record starting positions so can be reset later
    starting_row = -1
    starting_col = -1
    starting_facing: Facing = "up"
    starting_on_map = False

    row = -1
    col = -1
    facing: Facing = "up"
    on_map = False

    def __init__(self, row: int, col: int, facing: Facing):
        self.row = row
        self.col = col
        self.facing = facing
        self.on_map = True

        self.starting_row = row
        self.starting_col = col
        self.starting_facing = facing
        self.starting_on_map = True

    def __str__(self) -> str:
        return f"{self.row}, {self.col}, {self.facing}"

    def __repr__(self) -> str:
        return self.__str__()

    def reset_guard(self):
        self.row = self.starting_row
        self.col = self.starting_col
        self.facing = self.starting_facing
        self.on_map = self.starting_on_map

    def move_guard(self, grid: 'Grid'):
        """
        Moves the guard one move.

        Returns True if cycle found, None otherwise.
        """

        if not self.on_map:
            return

        # Calculate bounds
        total_rows = len(grid.grid)
        total_cols = len(grid.grid[0])

        # Determine spot moving to
        new_row, new_col = -1, -1

        match self.facing:
            case "up":
                new_row = self.row - 1
                new_col = self.col
            case "down":
                new_row = self.row + 1
                new_col = self.col
            case "left":
                new_row = self.row
                new_col = self.col - 1
            case "right":
                new_row = self.row
                new_col = self.col + 1

        # If new position is out of bounds, set it and set off map
        if new_row < 0 or new_col < 0 or new_row >= total_rows or new_col >= total_cols:
            self.row = new_row
            self.col = new_col
            self.on_map = False
            return

        # If new position is obstacle, rotate guard
        if grid.grid[new_row][new_col] == "#":
            match self.facing:
                case "up":
                    self.facing = "right"
                case "down":
                    self.facing = "left"
                case "left":
                    self.facing = "up"
                case "right":
                    self.facing = "down"

            # Add new facing to the visited facing set
            visited_set = grid.visited_facing.setdefault(
                (self.row, self.col), set())
            visited_set.add(self.facing)
            return

        # Otherwise, move guard to new position
        self.row = new_row
        self.col = new_col
        grid.visited.add((new_row, new_col))

        # If guard moves here and has visited in same facing before, then we are in a cycle
        visited_set = grid.visited_facing.setdefault(
            (new_row, new_col), set())

        if self.facing in visited_set:
            return True

        # Otherwise, add it
        visited_set.add(self.facing)
