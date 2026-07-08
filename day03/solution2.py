import re


def calculate_total(filename):
    total = 0

    with open(filename, "r") as file:
        memory = file.read()

    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

    matches = re.findall(pattern, memory)

    for x, y in matches:
        total += int(x) * int(y)

    return total


if __name__ == "__main__":
    print(calculate_total("input_day3.txt"))

import re

def calculate_total(filename):
    with open(filename, "r") as file:
        memory = file.read()

    pattern = r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)"

    enabled = True
    total = 0

    for match in re.finditer(pattern, memory):
        instruction = match.group()

        if instruction == "do()":
            enabled = True

        elif instruction == "don't()":
            enabled = False

        elif enabled:
            x = int(match.group(1))
            y = int(match.group(2))
            total += x * y

    return total


if __name__ == "__main__":
    print(calculate_total("input_day3.txt"))
