def read_input():
    list1: list[int] = []
    list2: list[int] = []

    # Read input
    with open('day1/input.txt', 'r') as f:
        lines = f.readlines()

        for line in lines:
            line = line.strip()
            items = line.split()
            list1.append(int(items[0]))
            list2.append(int(items[1]))

    return (list1, list2)


def part1(list1: list[int], list2: list[int]):
    # Sort lists
    list1.sort()
    list2.sort()

    # Calculate total distance
    distance = 0
    for i in range(len(list1)):
        distance += abs(list1[i] - list2[i])

    print("part 1:", distance)


def part2(list1: list[int], list2: list[int]):
    # Calculate how many times each number in 2nd list occurs
    counter: dict[int, int] = dict()

    for i in list2:
        count = counter.get(i)
        counter[i] = 1 if count == None else count + 1

    # Calculate similarity score by iterating 1st list
    similarity_score = 0

    for i in list1:
        count = counter.get(i)
        similarity_score += 0 if count is None else i * count

    print("part 2:", similarity_score)


def main():
    list1, list2 = read_input()
    part1(list1, list2)
    part2(list1, list2)


if __name__ == "__main__":
    main()
