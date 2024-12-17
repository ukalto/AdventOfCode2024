def read_input():
    with open('day08', 'r') as file:
        return [[char for char in line.strip()] for line in file.readlines()]


if __name__ == '__main__':
    signal_field = read_input()
    print(signal_field)
