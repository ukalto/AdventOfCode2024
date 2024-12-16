import copy


def read_map():
    with open('day06.txt', 'r') as file:
        map = []
        guard_pos = (-1, -1)
        for line in file.readlines():
            row = []
            for char in line.strip():
                row.append(char)
                if char == '^':
                    guard_pos = (len(map), len(row) - 1)
            map.append(row)
        return map, guard_pos


def solve_first(map, guard_pos):
    curr_direction = [-1, 0]  # Initially "up"
    count_steps = {guard_pos}
    while True:
        try:
            next_pos = (guard_pos[0] + curr_direction[0], guard_pos[1] + curr_direction[1])
            if map[next_pos[0]][next_pos[1]] == '#':
                # Turn right 90°
                curr_direction = [curr_direction[1], -curr_direction[0]]
            else:
                count_steps.add(next_pos)
                guard_pos = next_pos
                map[guard_pos[0]][guard_pos[1]] = 'X'
        except IndexError:
            break
    print(f'First: {len(count_steps)}')
    return count_steps


def solve_second(map, guard_pos, possible_loop_steps):
    count_loops = 0
    starting_pos = guard_pos
    original_map = map
    possible_loop_steps = {(41,42)}
    for row, col in possible_loop_steps:
        curr_direction = [-1, 0]  # Initially "up"
        map = copy.deepcopy(original_map)
        guard_pos = starting_pos
        loop_hit = 0
        if map[row][col] == '^':
            continue
        else:
            map[row][col] = 'O'
        while True:
            try:
                next_pos = (guard_pos[0] + curr_direction[0], guard_pos[1] + curr_direction[1])
                if loop_hit == 2:
                    count_loops += 1
                    break
                if map[next_pos[0]][next_pos[1]] == 'O':
                    print(f'Loop hit at {row, col}')
                    loop_hit += 1
                if map[next_pos[0]][next_pos[1]] == '#' or map[next_pos[0]][next_pos[1]] == 'O':
                    # Turn right 90°
                    curr_direction = [curr_direction[1], -curr_direction[0]]
                else:
                    guard_pos = next_pos
                    map[guard_pos[0]][guard_pos[1]] = 'X'
            except IndexError:
                break
    print(f'Second: {count_loops}')


if __name__ == '__main__':
    map, guard_pos = read_map()
    possible_loop_steps = solve_first(copy.deepcopy(map), guard_pos)
    solve_second(copy.deepcopy(map), guard_pos, possible_loop_steps)
