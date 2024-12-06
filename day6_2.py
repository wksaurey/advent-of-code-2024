from util import read_stripped_compressed_grid
import copy

def main():
    filename = 'bin/day6_test.txt'

    original_map = read_stripped_compressed_grid(filename)
    print_map(original_map)

    for row_index, line in enumerate(original_map):
        for col_index, value in enumerate(line):
            test_map = copy.deepcopy(original_map)
            if value == '.':
                test_map[row_index][col_index] = '#'
                print_map(test_map)

def print_map(working_map):
    for line in working_map:
        print(''.join(line))
    print()

class Guard():
    def __init__(self):
        self.x
        self.y


main()