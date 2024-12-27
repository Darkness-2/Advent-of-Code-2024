type Reports = list[list[int]]


def read_input(filename: str):
    reports: Reports = []

    with open(filename, 'r') as f:
        lines = f.readlines()

        for line in lines:
            line = line.strip()
            items = line.split()
            items = [int(i) for i in items]
            reports.append(items)

    return reports


def part1(reports: Reports):
    count = 0

    for report in reports:
        if validate_report(report):
            count += 1

    print("part 1:", count)


def validate_report(report: list[int]) -> bool:
    # Report of length 1 is safe
    if len(report) == 1:
        return True

    # Create list of increasing, decreasing, and size steps
    decreasing = all([True if report[i + 1] < report[i] else False
                      for i in range(len(report) - 1)])

    increasing = all([True if report[i + 1] > report[i] else False
                      for i in range(len(report) - 1)])

    all_small = all([False if abs(report[i] - report[i+1]) > 3
                     else True
                     for i in range(len(report) - 1)])

    return all_small and (decreasing or increasing)


def part2(reports: Reports):
    count = 0

    for report in reports:
        if validate_report(report):
            count += 1
            continue

        # If wasn't valid, brute force remove elements
        for i in range(len(report)):
            new_report = report.copy()
            del new_report[i]

            if validate_report(new_report):
                count += 1
                break

    print("part 2:", count)


def main():
    reports = read_input("day2/input.txt")
    part1(reports)
    part2(reports)


if __name__ == "__main__":
    main()
