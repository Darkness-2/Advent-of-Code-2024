from collections import deque
from typing import Deque


type Coordinate = tuple[int, int]
type Grid = list[list[int]]


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
    Performs DFS from the start coordinate. Only considers neighbors if they are of +1 height from the node.

    O(m*n) as # of edges are known in a grid graph (2mn-m-n)

    https://www.geeksforgeeks.org/iterative-depth-first-traversal/
    """
    visited: set[Coordinate] = set()
    nines: set[Coordinate] = set()
    stack: Deque[Coordinate] = deque()

    # Push start onto stack
    stack.append(start)

    while len(stack):
        v = stack.pop()
        row, col = v
        height = grid[row][col]

        visited.add(v)

        # Add to nines if height is 9
        if height == 9:
            nines.add(v)

        neighbors = generate_neighbors(v)

        # Check if each neighbor is reachable
        for neighbor in neighbors:
            neighbor_row, neighbor_col = neighbor

            # Skip if out of bounds
            if not check_in_bounds(grid, neighbor):
                continue

            # Skip if already visited
            if neighbor in visited:
                continue

            # Skip if not +1 in height
            neighbor_height = grid[neighbor_row][neighbor_col]
            if neighbor_height != height + 1:
                continue

            # Otherwise, visit it
            stack.append(neighbor)

    return visited, nines


def modified_bfs(grid: Grid, start: Coordinate):
    """
    Performs a modified BFS that doesn't keep track of a visited set, so as to find all possible paths between the start and a '9'.

    Note that each vertex can be added to the queue up to 4 times each (once by each of its neighbors) so:
    O(4m*n) = O(m*n)

    https://stackoverflow.com/questions/9535819/find-all-paths-between-two-graph-nodes
    https://en.wikipedia.org/wiki/Breadth-first_search
    """
    queue: Deque[Coordinate] = deque()
    paths = 0

    # Push start into the queue
    queue.append(start)

    while len(queue):
        v = queue.popleft()
        row, col = v
        height = grid[row][col]

        # If height is 9, we found another path
        if height == 9:
            paths += 1
            continue

        neighbors = generate_neighbors(v)

        # Check if each neighbor is reachable
        for neighbor in neighbors:
            neighbor_row, neighbor_col = neighbor

            # Skip if out of bounds
            if not check_in_bounds(grid, neighbor):
                continue

            # Skip if not +1 in height
            neighbor_height = grid[neighbor_row][neighbor_col]
            if neighbor_height != height + 1:
                continue

            # Otherwise, add it to the queue
            queue.append(neighbor)

    return paths
