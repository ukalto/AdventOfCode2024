from itertools import product

def read_input():
    with open('day07', 'r') as file:
        data = []
        for line in file.readlines():
            result, numbers = line.strip().split(':')
            result = int(result)
            numbers = list(map(int, numbers.split()))
            data.append((result, numbers))
        return data

def calculate(numbers, operators):
    result = numbers[0]
    for num, op in zip(numbers[1:], operators):
        if op == '+':
            result += num
        elif op == '*':
            result *= num
        elif op == '||':
            result = int(f'{result}{num}')
    return result

def solve_first(data):
    sum_possible = 0
    for target_result, numbers in data:
        n = len(numbers) - 1
        for ops in product(['+', '*'], repeat=n):
            if calculate(numbers, ops) == target_result:
                sum_possible += target_result
                break
    print(sum_possible)

def solve_second(data):
    sum_possible = 0
    for target_result, numbers in data:
        n = len(numbers) - 1
        for ops in product(['+', '*', '||'], repeat=n):
            if calculate(numbers, ops) == target_result:
                sum_possible += target_result
                break
    print(sum_possible)

if __name__ == '__main__':
    input = read_input()
    solve_first(input)
    solve_second(input)