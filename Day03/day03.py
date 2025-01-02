import re


def solve_first():
    with open('day03', 'r') as file:
        print(sum([int(x) * int(y) for x, y in re.findall(r"mul\((\d{1,3}),\s?(\d{1,3})\)", ''.join([line.strip() for line in file.readlines()]))]))


def solve_second():
    with open('day03', 'r') as file:
        content = ''.join(line.strip() for line in file).split("don't()")
        dos = [content[0]] + [do.split("do()")[1:] for idx, do in enumerate(content[1:], start=1)]
        print(sum([int(x) * int(y) for x, y in re.findall(r"mul\((\d{1,3}),\s?(\d{1,3})\)", ''.join([str(do) for do in dos]))]))

if __name__ == '__main__':
    solve_first()
    solve_second()
