from math import floor, log


def stone_rule(x: int):
    # https://math.stackexchange.com/questions/469606/how-to-get-count-of-digits-of-a-number
    num_digits = 1 if x == 0 else floor(log(x, 10)) + 1

    res: list[int] = []
    if x == 0:
        res.append(1)
    elif num_digits % 2 == 0:
        y = 10 ** int(num_digits / 2)

        lower_half = x % y
        upper_half = floor(x / y)

        res.append(upper_half)
        res.append(lower_half)
    else:
        res.append(x * 2024)

    return res


# stone_results_after_x_moves[(x, y)] = [a, b]
# number x after y moves results in stones a and b
stone_results_after_x_moves: dict[tuple[int, int], list[int]] = {}


def stones_after_x_moves(stone: int, moves: int) -> list[int]:
    # Check cache
    if (stone, moves) in stone_results_after_x_moves:
        return stone_results_after_x_moves[(stone, moves)]

    stones = []

    # Base case: if just one move, calculate
    if moves == 1:
        stones.extend(stone_rule(stone))
    else:
        # Otherwise, get stones from previous move and run stone rule on each
        for parent_stone in stones_after_x_moves(stone, moves - 1):
            stones.extend(stones_after_x_moves(parent_stone, 1))

    # Store in cache
    stone_results_after_x_moves[(stone, moves)] = stones
    return stones


def calculate_stones_after_x_moves(stones: list[int], moves: int):
    total = 0

    for stone in stones:
        total += len(stones_after_x_moves(stone, moves))

    return total
