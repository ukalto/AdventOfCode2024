def read_input():
    with open('day04.txt', 'r') as file:
        return [[letter for letter in line.strip()] for line in file.readlines()]


def solve_first(grid):
    rows = len(grid)
    cols = len(grid[0])
    target = "XMAS"
    reversed_target = target[::-1]
    target_len = len(target)
    directions = [
        (0, 1),  # Right
        (1, 0),  # Down
        (1, 1),  # Down-Right Diagonal
        (1, -1),  # Down-Left Diagonal
    ]
    results = []

    def is_within_bounds(x, y):
        return 0 <= x < rows and 0 <= y < cols

    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                word = ""
                positions = []
                for i in range(target_len):
                    nr, nc = r + dr * i, c + dc * i
                    if is_within_bounds(nr, nc):
                        word += grid[nr][nc]
                        positions.append((nr, nc))
                    else:
                        break
                if word == target or word == reversed_target:
                    results.append(positions)

    print(len(results))


def solve_second(grid):
    rows = len(grid)
    cols = len(grid[0])
    count_xmas = 0
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            character = grid[r][c]
            if character == 'A':
                lu = grid[r - 1][c - 1]
                ru = grid[r - 1][c + 1]
                ld = grid[r + 1][c - 1]
                rd = grid[r + 1][c + 1]
                if lu == 'M' and ld == 'M' and ru == 'S' and rd == 'S':
                    count_xmas += 1
                elif lu == 'S' and ld == 'S' and ru == 'M' and rd == 'M':
                    count_xmas += 1
                elif lu == 'S' and ld == 'M' and ru == 'S' and rd == 'M':
                    count_xmas += 1
                elif lu == 'M' and ld == 'S' and ru == 'M' and rd == 'S':
                    count_xmas += 1
    print(count_xmas)


if __name__ == '__main__':
    data = read_input()
    solve_first(data)
    solve_second(data)
