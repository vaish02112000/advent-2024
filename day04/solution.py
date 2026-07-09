def count_xmas(grid):
    rows = len(grid)
    cols = len(grid[0])

    directions = [
        (-1, 0), (1, 0), (0, -1), (0, 1),
        (-1, -1), (-1, 1), (1, -1), (1, 1)
    ]

    word = "XMAS"
    count = 0

    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                found = True

                for i in range(len(word)):
                    nr = r + dr * i
                    nc = c + dc * i

                    if (
                        nr < 0
                        or nr >= rows
                        or nc < 0
                        or nc >= cols
                        or grid[nr][nc] != word[i]
                    ):
                        found = False
                        break

                if found:
                    count += 1

    return count


def count_x_mas(grid):
    rows = len(grid)
    cols = len(grid[0])

    count = 0

    for r in range(1, rows - 1):
        for c in range(1, cols - 1):

            if grid[r][c] != "A":
                continue

            diagonal1 = grid[r - 1][c - 1] + grid[r][c] + grid[r + 1][c + 1]
            diagonal2 = grid[r - 1][c + 1] + grid[r][c] + grid[r + 1][c - 1]

            if (
                diagonal1 in ("MAS", "SAM")
                and diagonal2 in ("MAS", "SAM")
            ):
                count += 1

    return count


def main():
    with open("input_day4.txt", "r") as file:
        grid = [line.strip() for line in file]

    print(f"Part 1: {count_xmas(grid)}")
    print(f"Part 2: {count_x_mas(grid)}")


if __name__ == "__main__":
    main()
