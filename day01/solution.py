from collections import Counter


def calculate_total_distance(filename):
    left = []
    right = []

    with open(filename, "r") as file:
        for line in file:
            a, b = map(int, line.split())
            left.append(a)
            right.append(b)

    left.sort()
    right.sort()

    return sum(abs(a - b) for a, b in zip(left, right))


def calculate_similarity_score(filename):
    left = []
    right = []

    with open(filename, "r") as file:
        for line in file:
            a, b = map(int, line.split())
            left.append(a)
            right.append(b)

    right_counts = Counter(right)

    similarity_score = 0

    for value in left:
        similarity_score += value * right_counts[value]

    return similarity_score


if __name__ == "__main__":
    filename = "input_day1.txt"

    print(f"Part 1: {calculate_total_distance(filename)}")
    print(f"Part 2: {calculate_similarity_score(filename)}")
