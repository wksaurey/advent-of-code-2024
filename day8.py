from util import read_stripped_compressed_grid

def main():
    filename = 'bin/day8.txt'

    grid = read_stripped_compressed_grid(filename)
    print_grid(grid)

    antennas = get_antennas(grid)
    # print(antennas)

    # print()
    antinodes = get_antinodes(antennas, grid)

    for antinode in antinodes:
        x, y = antinode

    print(f'Antinodes: {len(antinodes)}')

def get_antinodes(antennas, grid):
    antinodes = []
    for antenna_type in antennas:
        for i in range(len(antennas[antenna_type])):
            for j in range(i+1, len(antennas[antenna_type])):
                x1, y1 = antennas[antenna_type][i]
                x2, y2 = antennas[antenna_type][j]
                dx = x1 - x2
                dy = y1 - y2

                index = 0
                direction = 1
                while True:
                    antinode = (x1 + index * dx, y1 + index * dy) 
                    x, y = antinode
                    if (x < 0 or x >= len(grid[0]) or 
                            y < 0 or y >= len(grid)):
                        if direction == 1:
                            direction = -1
                            index = 0
                            continue
                        else:
                            break
                    if antinode in antinodes:
                        index += direction
                        continue

                    # print(f'({x}, {y})')
                    if grid[y][x] == '.':
                        grid[y][x] = '#'
                        print_grid(grid)

                    antinodes.append(antinode)
                    index += direction

    return antinodes

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