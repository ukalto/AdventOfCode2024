def read_input():
    sorted_array = [[], []]
    with open('day01', 'r') as file:
        for line in file:
            distances = line.strip().split()
            sorted_array[0].append(int(distances[0]))
            sorted_array[1].append(int(distances[1]))
    return sorted_array


def solve_first(data):
    data[0].sort()
    data[1].sort()
    error_distance = sum([abs(i - j) for i, j in zip(data[0], data[1])])
    print(f"Total error distance: {error_distance}")

def solve_second(data):
    distance_dict = {}
    for value in data[1]:
        distance_dict[value] = distance_dict.get(value, 0) + 1

    error_distance = sum(value * distance_dict.get(value, 0) for value in data[0])

    print(f"Total error distance: {error_distance}")

if __name__ == '__main__':
    data = read_input()
    solve_first(data)
    solve_second(data)
