import copy


def read_input():
    data = open('day09', 'r').read().strip()
    data_block = []
    id_counter = 0

    for idx, number in enumerate(data):
        if idx % 2 == 0:
            data_block.extend([str(id_counter)] * int(number))
            id_counter += 1
        else:
            data_block.extend(['.'] * int(number))
    return data_block


def solve_first(data_block):
    for char in reversed(data_block):
        if char == '.':
            continue
        idx_of_dot = data_block.index('.')
        idx_of_block = len(data_block) - 1 - data_block[::-1].index(char)
        if idx_of_dot >= idx_of_block:
            break
        data_block[idx_of_dot], data_block[idx_of_block] = data_block[idx_of_block], '.'
    print(sum([int(value) * idx for idx, value in enumerate(data_block) if value != '.']))


def solve_second(data_block):
    already_moved = set()
    data_reverse_idx = len(data_block) - 1
    while True:
        if data_reverse_idx < 0:
            break
        data_reverse_char = data_block[data_reverse_idx]
        if data_reverse_char in already_moved:
            data_reverse_idx -= data_block.count(data_reverse_char)
            continue
        if data_reverse_char == '.':
            data_reverse_idx -= 1
            continue
        if data_reverse_char != '.':
            count_char = data_block.count(data_reverse_char)
            count_dots = 0
            first_dot_idx = -1
            for idy, char_rev in enumerate(data_block):
                if idy >= data_reverse_idx:
                    already_moved.add(data_reverse_char)
                    data_reverse_idx -= count_char
                    break
                if char_rev != '.':
                    first_dot_idx = -1
                    count_dots = 0
                else:
                    if first_dot_idx == -1:
                        first_dot_idx = idy
                    count_dots += 1
                    if count_dots >= count_char:
                        already_moved.add(data_reverse_char)
                        data_block = [i if i != data_reverse_char else '.' for i in data_block]
                        for i in range(count_char):
                            data_block[first_dot_idx + i] = data_reverse_char
                        data_reverse_idx -= count_char
                        break
    print(sum([int(value) * idx for idx, value in enumerate(data_block) if value != '.']))


if __name__ == '__main__':
    data = read_input()
    solve_first(copy.deepcopy(data))
    solve_second(copy.deepcopy(data))
