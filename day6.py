from util import read_stripped_compressed_grid

def main():
    filename = 'bin/day6.txt'

    map = read_stripped_compressed_grid(filename)

    # find guard
    guard_chars = ['^', 'v', '>', '<']
    for row_index, line in enumerate(map):
        for col_index, value in enumerate(line):
            if value in guard_chars:
                guard = Guard(value, col_index, row_index, map)
            
    while move(guard, map):
        # display(map)
        pass

    print(f'Count: {calculate_path_length(map)}')

def calculate_path_length(map):
    count = 1
    for line in map:
        for value in line:
            if value == 'X':
                count +=1
    return count

def move(guard, map):
    coordinates = guard.get_next_cordinates()
    if not coordinates:
        return False

    next_x, next_y = coordinates
    next_value = map[next_y][next_x]

    if next_value == '#':
        guard.turn()
        return move(guard, map)

    map[guard.y][guard.x] = 'X'
    map[next_y][next_x] = guard.guard_char

    guard.x = next_x
    guard.y = next_y

    return True

def display(map):
    for line in map:
        print(''.join(line))
    print()

class Guard():
    def __init__(self, guard_char, x, y, map):
        self.guard_char = guard_char
        self.x = x
        self.y = y
        self.max_x = len(map[0]) - 1
        self.max_y = len(map) - 1

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
        

main()
