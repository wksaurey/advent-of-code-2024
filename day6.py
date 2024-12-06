from util import read_stripped_compressed_grid

def main():
    filename = 'bin/day6_test.txt'

    map = read_stripped_compressed_grid(filename)
    display(map)

    # find guard
    guard_chars = ['^', 'v', '>', '<']
    for row_index, line in enumerate(map):
        for col_index, value in line:
            pass
            

def display(map):
    for line in map:
        print(''.join(line))

class Guard():
    def __init__(self, guard_char, x, y, direction):
        self.guard_char = guard_char
        self.x = x
        self.y = y
        self.direction = direction

main()
