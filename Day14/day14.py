def read_input(rows=7, cols=11):
    with open('day14', 'r') as file:
        map = [[0] * cols for _ in range(rows)]
        commands = []
        for line in file.readlines():
            values_p, values_v = line.strip().split(' ')
            px, py = [int(i) for i in values_p.split('=')[1].split(',')]
            vx, vy = [int(i) for i in values_v.split('=')[1].split(',')]
            if map[py][px] == 0:
                map[py][px] = 1
            else:
                map[py][px] = map[py][px] + 1
            commands.append([px, py, vx, vy])
        return commands, map


def solve_first(commands, map, steps=5, rows=7, cols=11):
    for step in range(steps):
        new_map = [[0] * cols for _ in range(rows)]

        for i, (px, py, vx, vy) in enumerate(commands):
            py = (py + vy) % rows
            px = (px + vx) % cols
            new_map[py][px] += 1
            commands[i] = [px, py, vx, vy]
        map[:] = new_map

    left_top, right_top, left_bottom, right_bottom = 0, 0, 0, 0
    for x, row in enumerate(map):
        if x == rows // 2:
            continue
        for y, char in enumerate(row):
            if y == cols // 2:
                continue
            if x < rows // 2 and y < cols // 2:
                left_top += char
            elif x < rows // 2 and y > cols // 2:
                right_top += char
            elif x > rows // 2 and y < cols // 2:
                left_bottom += char
            elif x > rows // 2 and y > cols // 2:
                right_bottom += char
    print(left_top * right_top * left_bottom * right_bottom)


if __name__ == '__main__':
    commands, map = read_input(103, 101)
    solve_first(commands, map, 100, 103, 101)
