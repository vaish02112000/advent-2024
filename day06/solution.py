def read_input(filename):
    with open(filename, "r") as file:
        return [list(line.strip()) for line in file]

def find_guard(grid):
    directions = {
        "^": 0,
        ">": 1,
        "v": 2,
        "<": 3
    }
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] in directions:
                return r, c, directions[grid[r][c]]

def simulate(grid, extra_obstacle=None):
    rows = len(grid)
    cols = len(grid[0])
    r, c, direction = find_guard(grid)
    # Up, Right, Down, Left
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visited_positions = set()
    visited_states = set()
    while True:
        visited_positions.add((r, c))

        state = (r, c, direction)
        if state in visited_states:
            return True, visited_positions

        visited_states.add(state)

        dr, dc = moves[direction]
        nr = r + dr
        nc = c + dc

        if not (0 <= nr < rows and 0 <= nc < cols):
            return False, visited_positions

        if grid[nr][nc] == "#" or (extra_obstacle == (nr, nc)):
            direction = (direction + 1) % 4
        else:
            r, c = nr, nc

def part1(grid):
    _, visited = simulate(grid)
    return len(visited), visited

def part2(grid, visited):
    start_r, start_c, _ = find_guard(grid)

    count = 0

    for position in visited:
        if position == (start_r, start_c):
            continue

        if grid[position[0]][position[1]] == "#":
            continue

        loop, _ = simulate(grid, position)

        if loop:
            count += 1

    return count

def main():
    grid = read_input("input_day6.txt")

    answer1, visited = part1(grid)
    answer2 = part2(grid, visited)

    print(f"Part 1: {answer1}")
    print(f"Part 2: {answer2}")

if __name__ == "__main__":
    main()
