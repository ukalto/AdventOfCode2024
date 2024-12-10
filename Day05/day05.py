def read_input():
    with open('day05.txt', 'r') as file:
        data = file.read().split('\n\n')
        rules = [rule.split('|') for rule in data[0].split('\n')]
        updates = [line.split(',') for line in data[1].split('\n')]
        return rules, updates


def solve_first(rules, updates):
    sum_error = 0
    for update in updates:
        i = 0
        for j in range(1, len(update)-1):
            test = [update[i], update[j]]
            if test not in rules:
                break
            i += 1
        if i+1 != len(update):
            sum_error += int(update[int(i/2+1)])
            print(update)
    print(sum_error)
if __name__ == '__main__':
    rules, updates = read_input()
    solve_first(rules, updates)
