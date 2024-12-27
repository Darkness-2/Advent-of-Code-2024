from collections import deque
from math import floor
import re

type Rule = tuple[int, int]
type Update = list[int]
type DiGraph = dict[int, set[int]]


def read_input(filename: str):
    rule_regex = r'(\d+)\|(\d+)'
    update_regex = r'(?:\d+,)+(?:\d+)'

    rules: list[Rule] = []
    updates: list[Update] = []

    with open(filename, 'r') as f:
        line = f.readline()

        while len(line):
            line = line.strip()

            m = re.match(rule_regex, line)
            if m:
                rules.append((int(m.group(1)), int(m.group(2))))

            m = re.match(update_regex, line)
            if m:
                update = line.split(',')
                update = list(map(int, update))
                updates.append(update)

            line = f.readline()

    return rules, updates


def check_topo_sort(rules: list[Rule], update: Update):
    """
    O(rules * size of update)
    https://stackoverflow.com/questions/54174116/checking-validity-of-topological-sort
    """
    # Iterate over rules (edges) and check if any is violated
    for rule in rules:
        # Find index of each vertex in a rule
        try:
            i = update.index(rule[0])
            j = update.index(rule[1])
        except ValueError:
            # One or more is not present, can skip
            continue

        # If first vertex appears later, rule is violated
        if j < i:
            return False

    # If all rules pass, it's a valid topo sort
    return True


def part1(rules: list[Rule], updates: list[Update]):
    """
    O(rules * size of update * updates)
    """
    total = 0

    # Check if all updates are a valid topo sort
    for update in updates:
        if check_topo_sort(rules, update):
            # Grab middle value and add to total
            total += update[floor(len(update) / 2)]

    print("part 1:", total)


def make_digraph(rules: list[Rule], update: Update):
    """
    O(rules * size of update)
    """
    # Make adjacency list graph
    graph: DiGraph = dict()

    # Add vertices
    for v in update:
        graph[v] = set()

    for rule in rules:
        # Ignore irrelevant rules
        if not (rule[0] in update and rule[1] in update):
            continue

        # Add edge
        edges = graph.get(rule[0])
        if edges is None:
            raise RuntimeError("Could not find node.")

        edges.add(rule[1])

    return graph


def make_topo_sort(graph: DiGraph):
    """
    https://www.geeksforgeeks.org/topological-sorting/
    O(rules + size of update)
    """
    visited: set[int] = set()
    stack: deque[int] = deque()
    topo_sort: list[int] = []

    def dfs(vertex: int):
        visited.add(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                dfs(neighbor)

        stack.append(vertex)

    for vertex in graph.keys():
        if vertex not in visited:
            dfs(vertex)

    while stack:
        topo_sort.append(stack.pop())

    return topo_sort


def make_valid_ordering(rules: list[Rule], update: Update):
    """
    O(rules * size of update)
    """
    # Generate a topo_sort from the rules
    graph = make_digraph(rules, update)
    topo_sort = make_topo_sort(graph)

    return topo_sort


def part2(rules: list[Rule], updates: list[Update]):
    """
    O(rules * size of update * updates)
    """
    total = 0

    # Check for invalid topo sorts
    for update in updates:
        if not check_topo_sort(rules, update):
            # Generate a valid ordering
            ordering = make_valid_ordering(rules, update)

            # Grab middle value and add to total
            total += ordering[floor(len(update) / 2)]

    print("part 2:", total)


def main():
    filename = "day5/input.txt"

    rules, updates = read_input(filename)
    part1(rules, updates)
    part2(rules, updates)


if __name__ == "__main__":
    main()
