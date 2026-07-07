def is_safe(levels):
    increasing = all(1 <= levels[i + 1] - levels[i] <= 3 for i in range(len(levels) - 1))
    decreasing = all(1 <= levels[i] - levels[i + 1] <= 3 for i in range(len(levels) - 1))
    return increasing or decreasing


def count_safe_reports(filename):
    safe_count = 0

    with open(filename, "r") as file:
        for line in file:
            levels = list(map(int, line.split()))
            if is_safe(levels):
                safe_count += 1

    return safe_count


if __name__ == "__main__":
    print(count_safe_reports("input.txt"))
