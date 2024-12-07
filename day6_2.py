from util import read_stripped_compressed_grid
import copy
from time import time

def main():
    filename = 'bin/day6.txt'

    original_map = read_stripped_compressed_grid(filename)

    start = time()
    loop_count = 0
    map_version = 0
    for row_index, line in enumerate(original_map):
        for col_index, value in enumerate(line):
            test_map = copy.deepcopy(original_map)
            if value == '.':
                test_map[row_index][col_index] = '#'
                guard = Guard(original_map)
                # print(f'Map Version {map_version}')
                # print_map(test_map)
                map_version += 1
                if is_loop(guard, test_map):
                    loop_count += 1

    print(f'Loop Count: {loop_count}')
    print(f'Completed in {time() - start} seconds')

def is_loop(guard, test_map):
    while True:
        next_char, next_y, next_x = guard.next_pos(test_map) 

        if next_char == None:
            return False

        if next_char == '#':
            obstacle = Obstacle_History(next_x, next_y, guard.direction)
            if obstacle in guard.obstacle_history:
                return True
            guard.obstacle_history.append(obstacle)
            guard.turn()

        else:
            guard.x = next_x
            guard.y = next_y

def print_map(working_map):
    for line in working_map:
        print(''.join(line))
    print()

class Guard():
    def __init__(self, original_map):
        self.direction = '^'
        self.obstacle_history = []
        for row_index, line in enumerate(original_map):
            for col_index, value in enumerate(line):
                if value == '^':
                    self.x = col_index
                    self.y = row_index

    def next_pos(self, test_map):
        if self.direction == '^':
            if self.y <= 0:
                return (None, None, None)
            return (test_map[self.y-1][self.x], self.y-1, self.x)

        elif self.direction == 'v':
            if self.y >= len(test_map) - 1:
                return (None, None, None)
            return (test_map[self.y+1][self.x], self.y+1, self.x)

        elif self.direction == '<':
            if self.x <= 0:
                return (None, None, None)
            return (test_map[self.y][self.x-1], self.y, self.x-1)

        elif self.direction == '>':
            if self.x >= len(test_map[0]) - 1:
                return (None, None, None)
            return (test_map[self.y][self.x+1], self.y, self.x+1)

    def turn(self):
        guard_directions = ['^', '>', 'v', '<']
        index = guard_directions.index(self.direction)
        index += 1
        if index >= len(guard_directions):
            index = 0
        self.direction = guard_directions[index]

class Obstacle_History():
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def __eq__(self, other):
        return (self.x == other.x and
                self.y == other.y and
                self.direction == other.direction)
main()