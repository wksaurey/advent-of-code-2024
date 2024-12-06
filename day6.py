from util import read_stripped_compressed_grid

def main():
    filename = 'bin/day6_test.txt'

    map = read_stripped_compressed_grid(filename)

    # find guard
    guard_chars = ['^', 'v', '>', '<']
    for row_index, line in enumerate(map):
        for col_index, value in enumerate(line):
            if value in guard_chars:
                guard = Guard(value, col_index, row_index, map)
                guard.set_direction_history(map)

    for row_index, line in enumerate(map):
        for col_index, value in enumerate(line):
            if value == '.':
                map[row_index][col_index] = '#'
                while move(guard, map):
                    display(map)
                map[row_index][col_index] = '.'
                clear_path(map)
                reset_guard(guard, map)
                display(map)

    print(f'Count: {calculate_path_length(map)}')
    print(f'Loop Count: {guard.loop_count}')

def calculate_path_length(map):
    count = 1
    for line in map:
        for value in line:
            if value == 'X':
                count +=1
    return count

def move(guard, map, turning = False):
    coordinates = guard.get_next_cordinates()
    if not coordinates:
        return False

    next_x, next_y = coordinates
    next_value = map[next_y][next_x]

    if next_value == '#':
        guard.turn()
        return move(guard, map, turning=True)
    
    if guard.in_loop():
        guard.loop_count += 1
        return False

    if not turning:
        guard.update_direction_history()
    map[guard.y][guard.x] = 'X'
    map[next_y][next_x] = guard.guard_char

    guard.x = next_x
    guard.y = next_y

    return True

def clear_path(map):
    for row_index, line in enumerate(map):
        for col_index, value in enumerate(line):
            if value == 'X':
                map[row_index][col_index] = '.'

def reset_guard(guard, map):
    map[guard.initial_y][guard.initial_x] = guard.initial_guard_char
    map[guard.y][guard.x] = '.'
    guard.guard_char = guard.initial_guard_char
    guard.x = guard.initial_x
    guard.y = guard.initial_y
    guard.set_direction_history(map)

def display(map):
    for line in map:
        print(''.join(line))
    print()

class Guard():
    def __init__(self, guard_char, x, y, map):
        self.guard_char = guard_char
        self.initial_guard_char = guard_char
        self.initial_x = x
        self.initial_y = y
        self.x = x
        self.y = y
        self.max_x = len(map[0]) - 1
        self.max_y = len(map) - 1
        self.loop_count = 0
        self.direction_history = []

    def set_direction_history(self, map):
        for _ in map:
            self.direction_history.append([[]] * len(map[0]))

    def get_next_cordinates(self):
        if self.guard_char == '^':
            if self.y > 0:
                return (self.x, self.y - 1)
        elif self.guard_char == 'v':
            if self.y < self.max_y:
                return (self.x, self.y + 1)
        elif self.guard_char == '<':
            if self.x > 0:
                return (self.x - 1, self.y)
        elif self.guard_char == '>':
            if self.x < self.max_x:
                return (self.x + 1, self.y)

        return None

    def turn(self):
        if self.guard_char == '^':
            self.guard_char = '>'
        elif self.guard_char == 'v':
            self.guard_char =  '<'
        elif self.guard_char == '<':
            self.guard_char = '^'
        elif self.guard_char == '>':
            self.guard_char =  'v'

    def update_direction_history(self):
        self.direction_history[self.y][self.x].append(self.guard_char)

    def in_loop(self):
        return self.guard_char in self.direction_history[self.y][self.x]
        

main()
