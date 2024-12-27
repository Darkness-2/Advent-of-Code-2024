from typing import Literal
from guard import Facing, Guard


type TileType = Literal[".", "#"]


class Grid:
    grid: list[list[TileType]] = list()
    visited: set[tuple[int, int]] = set()
    visited_facing: dict[tuple[int, int], set[Facing]] = dict()

    def __init__(self):
        self.grid = list()
        self.visited = set()
        self.visited_facing = dict()

    def reset_grid(self, guard: Guard):
        self.visited = set()
        self.visited_facing = dict()

        # Set guard as visited
        self.visited.add((guard.row, guard.col))
        visited_set = self.visited_facing.setdefault(
            (guard.row, guard.col), set())
        visited_set.add(guard.facing)
