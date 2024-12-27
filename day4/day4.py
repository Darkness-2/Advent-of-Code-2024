WORD_LENGTH = 4


def read_input(filename: str):
    with open(filename, 'r') as f:
        lines = f.readlines()

    grid = list(map(lambda x: x.strip(), lines))

    return grid


def check_word(word: str):
    if word == "XMAS":
        return True
    elif word == "SAMX":
        return True
    else:
        return False


def check_horizontal(grid: list[str], row: int, col: int):
    # Prevent out of index errors
    if row >= len(grid):
        return False

    if col > len(grid[0]) - WORD_LENGTH:
        return False

    word = grid[row][col:col + WORD_LENGTH]

    return check_word(word)


def check_vertical(grid: list[str], row: int, col: int):
    # Prevent out of index errors
    if row > len(grid) - WORD_LENGTH:
        return False

    if col >= len(grid[0]):
        return False

    word = ""

    for i in range(WORD_LENGTH):
        word += grid[row + i][col]

    return check_word(word)


def check_right_diagonal(grid: list[str], row: int, col: int):
    # Prevent out of index errors
    if row > len(grid) - WORD_LENGTH:
        return False

    if col > len(grid[0]) - WORD_LENGTH:
        return False

    word = ""

    for i in range(WORD_LENGTH):
        word += grid[row + i][col + i]

    return check_word(word)


def check_left_diagonal(grid: list[str], row: int, col: int):
    # Prevent out of index errors
    if row > len(grid) - WORD_LENGTH:
        return False

    if col < WORD_LENGTH - 1:
        return False

    word = ""

    for i in range(WORD_LENGTH):
        word += grid[row + i][col - i]

    return check_word(word)


def part1(grid: list[str]):
    occurences = 0

    # Check all starting spots
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if check_horizontal(grid, row, col):
                occurences += 1

            if check_vertical(grid, row, col):
                occurences += 1

            if check_right_diagonal(grid, row, col):
                occurences += 1

            if check_left_diagonal(grid, row, col):
                occurences += 1

    print("part 1:", occurences)


def check_x_mas(grid: list[str], row: int, col: int):
    left_diag_word = grid[row][col]
    left_diag_word += grid[row + 1][col + 1]
    left_diag_word += grid[row + 2][col + 2]

    right_diag_word = grid[row][col + 2]
    right_diag_word += grid[row + 1][col + 1]
    right_diag_word += grid[row + 2][col]

    if left_diag_word == "MAS" or left_diag_word == "SAM":
        if right_diag_word == "MAS" or right_diag_word == "SAM":
            return True

    return False


def part2(grid: list[str]):
    occurences = 0

    # Check all 3x3 starting spots
    for row in range(len(grid) - 2):
        for col in range(len(grid[0]) - 2):
            if check_x_mas(grid, row, col):
                occurences += 1

    print("part 2:", occurences)


def main():
    filename = "day4/input.txt"

    grid = read_input(filename)
    part1(grid)
    part2(grid)


if __name__ == "__main__":
    main()
