import re

full_regex = r'do\(\)|don\'t\(\)|mul\(\d+,\d+\)'
mul_regex = r'mul\((\d+),(\d+)\)'


def read_input(filename: str):
    instances: list[str] = []

    with open(filename, 'r') as f:
        line = f.readline()

        while len(line):
            # Find all instances in line and add
            results: list[str] = re.findall(full_regex, line)
            instances.extend(results)
            line = f.readline()

    return instances


def part1(instances: list[str]):
    total = 0

    for instance in instances:
        match instance[:3]:
            case "mul":
                match = re.match(mul_regex, instance)
                if match is None:
                    raise ValueError("Could not get match from mul statement.")

                val1 = int(match.group(1))
                val2 = int(match.group(2))

                total += val1 * val2

    print("part 1:", total)


def part2(instances: list[str]):
    enabled = True
    total = 0

    for instance in instances:
        match instance[:3]:
            case "mul":
                # Skip if not enabled
                if not enabled:
                    continue

                match = re.match(mul_regex, instance)
                if match is None:
                    raise ValueError("Could not get match from mul statement.")

                val1 = int(match.group(1))
                val2 = int(match.group(2))

                total += val1 * val2

            case "do(":
                enabled = True

            case "don":
                enabled = False

    print("part 2:", total)


def main():
    filename = "day3/input.txt"

    instances = read_input(filename)
    part1(instances)
    part2(instances)


if __name__ == "__main__":
    main()
