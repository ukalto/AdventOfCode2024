def read_input():
    with open('day05.txt', 'r') as file:
        data = file.read().split('\n\n')
        rules = [rule.split('|') for rule in data[0].split('\n')]
        updates = [line.split(',') for line in data[1].split('\n')]
        return rules, updates


def solve_first(rules, updates):
    sum_error = 0
    for update in updates:
        valid = True
        for i in range(len(update) - 1):
            for j in range(i + 1, len(update)):
                if [update[j], update[i]] in rules:
                    valid = False
                    break
            if not valid:
                break
        if valid:
            sum_error += int(update[int(len(update) / 2)])
    print(sum_error)


def solve_second(rules, updates):
    sum_error = 0
    invalid_updates = []
    for update in updates:
        valid = True
        for i in range(len(update) - 1):
            for j in range(i + 1, len(update)):
                if [update[j], update[i]] in rules:
                    invalid_updates.append(update)
                    valid = False
                    break
            if not valid:
                break

    for invalid_update in invalid_updates:
        sum_error += fix_invalid_update(invalid_update, rules)
    print(sum_error)


def fix_invalid_update(invalid_update, rules):
    final_update = ['0']*len(invalid_update)
    for iu in invalid_update:
        rule_breaks = 0
        for test in invalid_update:
            if [test, iu] in rules:
                rule_breaks += 1
        final_update[rule_breaks] = iu
    return int(final_update[int(len(final_update) / 2)])


if __name__ == '__main__':
    rules, updates = read_input()
    solve_first(rules, updates)
    solve_second(rules, updates)
