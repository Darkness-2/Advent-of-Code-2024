from collections import deque


type Coordinate = tuple[int, int]
type Grid = list[str]


def generate_neighbors(start: Coordinate) -> list[Coordinate]:
    row, col = start

    return [(row, col - 1),
            (row, col + 1),
            (row - 1, col),
            (row + 1, col)]


def check_in_bounds(grid: Grid, v: Coordinate) -> bool:
    row, col = v

    if row < 0 or col < 0:
        return False

    if row >= len(grid) or col >= len(grid[0]):
        return False

    return True


def dfs(grid: Grid, start: Coordinate):
    """
    Performs DFS from the start coordinate. Only considers neighbors of the same type.

    Returns a visited set, area and a perimeter value for the region.

    https://www.geeksforgeeks.org/iterative-depth-first-traversal/
    """
    visited: set[Coordinate] = set()
    stack: deque[Coordinate] = deque()
    perimeter = 0

    # Push start onto stack
    stack.append(start)

    while len(stack):
        v = stack.pop()

        # Skip if already visited
        if v in visited:
            continue

        visited.add(v)
        row, col = v
        plot_type = grid[row][col]
        local_perimeter = 4

        neighbors = generate_neighbors(v)

        # Check if neighbors are the same type
        for neighbor in neighbors:
            # Skip if out of bounds
            if not check_in_bounds(grid, neighbor):
                continue

            # Skip if plot type is different
            neighbor_row, neighbor_col = neighbor
            neighbor_plot_type = grid[neighbor_row][neighbor_col]
            if neighbor_plot_type != plot_type:
                continue

            # Neighbor is of same type, reduce perimeter
            local_perimeter -= 1

            # Visit neighbor if not already visited
            if not neighbor in visited:
                stack.append(neighbor)

        # Add this spot's perimeter to total
        perimeter += local_perimeter

    return visited, len(visited), perimeter


def is_a_corner(neighbor1: bool, neighbor2: bool, diagonal: bool) -> bool:
    """
    For top-left as example, corner exists if both top and left are not neighbors 
    OR if top and left are neighbors AND top-left is not.
    """
    return (not neighbor1 and not neighbor2) or (neighbor1 and neighbor2 and not diagonal)


def count_corners(region: set[Coordinate]):
    """
    Counts the number of corners in a region.
    """
    corners = 0

    for plot in region:
        row, col = plot

        has_top_neighbor = (row - 1, col) in region
        has_bottom_neighbor = (row + 1, col) in region
        has_left_neighbor = (row, col - 1) in region
        has_right_neighbor = (row, col + 1) in region

        has_top_left_neighbor = (row - 1, col - 1) in region
        has_top_right_neighbor = (row - 1, col + 1) in region
        has_bottom_left_neighbor = (row + 1, col - 1) in region
        has_bottom_right_neighbor = (row + 1, col + 1) in region

        corner_bools = [is_a_corner(has_top_neighbor, has_left_neighbor, has_top_left_neighbor),
                        is_a_corner(has_top_neighbor,
                                    has_right_neighbor, has_top_right_neighbor),
                        is_a_corner(has_bottom_neighbor,
                                    has_left_neighbor, has_bottom_left_neighbor),
                        is_a_corner(has_bottom_neighbor, has_right_neighbor, has_bottom_right_neighbor)]

        corners += corner_bools.count(True)

    return corners
