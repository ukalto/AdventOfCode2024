def read_input():
    with open('day05.txt', 'r') as file:
        data = file.read().split('\n\n')
        rules = [rule.split('|') for rule in data[0].split('\n')]
        updates = [line.split(',') for line in data[1].split('\n')]
        return rules, updates


def solve_first(rules, updates):
    pass


if __name__ == '__main__':
    rules, updates = read_input()
    solve_first(rules, updates)
