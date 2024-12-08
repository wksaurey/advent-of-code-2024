from util import read_stripped_compressed_grid

def main():
    filename = 'bin/day8_test.txt'

    grid = read_stripped_compressed_grid(filename)
    print_grid(grid)

    antennas = get_antennas(grid)
    print(antennas)

def get_antennas(grid):
    antennas = {}
    for y, line in enumerate(grid):
        for x, value in enumerate(line):
            if value != '.':
                if value not in antennas:
                    antennas[value] = []

                antennas[value].append((x, y))

    return antennas

def print_grid(grid):
    for line in grid:
        print(''.join(line))
    print()

main()