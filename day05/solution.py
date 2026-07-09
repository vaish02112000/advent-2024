from collections import defaultdict, deque


def parse_input(filename):
    with open(filename, "r") as file:
        rules_text, updates_text = file.read().strip().split("\n\n")

    rules = []
    for line in rules_text.splitlines():
        before, after = map(int, line.split("|"))
        rules.append((before, after))

    updates = []
    for line in updates_text.splitlines():
        updates.append(list(map(int, line.split(","))))

    return rules, updates


def is_valid(update, rules):
    position = {page: i for i, page in enumerate(update)}

    for before, after in rules:
        if before in position and after in position:
            if position[before] > position[after]:
                return False

    return True


def middle_page(update):
    return update[len(update) // 2]


def topological_sort(update, rules):
    pages = set(update)

    graph = defaultdict(list)
    indegree = defaultdict(int)

    # Initialize indegrees
    for page in pages:
        indegree[page] = 0

    # Build graph using only relevant rules
    for before, after in rules:
        if before in pages and after in pages:
            graph[before].append(after)
            indegree[after] += 1

    # Queue pages with indegree 0
    queue = deque(sorted([page for page in pages if indegree[page] == 0]))

    ordered = []

    while queue:
        current = queue.popleft()
        ordered.append(current)

        for neighbor in graph[current]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return ordered


def part1(rules, updates):
    total = 0

    for update in updates:
        if is_valid(update, rules):
            total += middle_page(update)

    return total


def part2(rules, updates):
    total = 0

    for update in updates:
        if not is_valid(update, rules):
            corrected = topological_sort(update, rules)
            total += middle_page(corrected)

    return total


def main():
    rules, updates = parse_input("input_day5.txt")

    print(f"Part 1: {part1(rules, updates)}")
    print(f"Part 2: {part2(rules, updates)}")


if __name__ == "__main__":
    main()
