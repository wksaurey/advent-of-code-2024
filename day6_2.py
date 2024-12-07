from util import read_stripped_compressed_grid
import copy

def main():
    filename = 'bin/day6_test.txt'

    original_map = read_stripped_compressed_grid(filename)
    print_map(original_map)

    guard = Guard(original_map)

    loop_count = 0
    for row_index, line in enumerate(original_map):
        for col_index, value in enumerate(line):
            test_map = copy.deepcopy(original_map)
            if value == '.':
                test_map[row_index][col_index] = '#'
                print_map(test_map)
                if is_loop(guard, test_map):
                    loop_count += 1

def is_loop(guard, test_map):
    next = guard.next_pos(test_map) 
    if not next:
        return False
        
    if next == '#':
        guard.turn()
        # turn

def print_map(working_map):
    for line in working_map:
        print(''.join(line))
    print()

class Guard():
    def __init__(self, original_map):
        self.direction = '^'
        for row_index, line in enumerate(original_map):
            for col_index, value in enumerate(line):
                if value == '^':
                    self.x = col_index
                    self.y = row_index

    def next_pos(self, test_map):
        if self.direction == '^':
            if self.y <= 0:
                return None
            return test_map[self.y-1][self.x]

        elif self.direction == 'v':
            if self.y >= len(test_map) - 1:
                return None
            return test_map[self.y+1][self.x]

        elif self.direction == '<':
            if self.x <= 0:
                return None
            return test_map[self.y][self.x-1]

        elif self.direction == '>':
            if self.x >= len(test_map[0]) - 1:
                return None
            return test_map[self.y][self.x+1]

    def turn(self):
        guard_directions = ['^', '>', 'v', '>']
        index = guard_directions.index(self.direction)
        index += 1
        if index >= guard_directions[len]:
            index = 0
        self.direction = guard_directions[index]

main()