from util import read_stripped_lines, windows
from copy import copy

def main():
    filename = 'bin/day7.txt'

    data = read_stripped_lines(filename)

    total = 0
    for test in data:
        result = int(test.split(':')[0])
        values = list(map(int, test.split(':')[1].split()))

        if can_calculate(copy(values), result):
            total += result

    print(f'Total: {total}')

def can_calculate(values, result):
    if len(values) < 2:
        return values[0] == result

    x = values.pop(0)
    y = values.pop(0)

    return (can_calculate([x + y] + values, result) or
            can_calculate([x * y] + values, result))

main()