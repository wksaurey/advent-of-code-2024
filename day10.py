from util import read_stripped_compressed_grid
import copy

def main():
    # filename = 'input/day10_test.txt'
    filename = 'input/day10.txt'
    # topo_map = list(map(lambda line: map(int, line), read_stripped_compressed_grid(filename)))
    topo_map = read_stripped_compressed_grid(filename, nums=True)
    # print_map(topo_map)

    trailheads = get_trailheads(topo_map)
    trails = []
    complete_trails = []

    for trailhead in trailheads:
        # trailhead.print_data()
        trails.insert(0, Trail(trailhead))

    # print()

    while len(trails) > 0:
        trail = trails.pop()
        trail_tail = trail.get_last()
        sections = get_sections(trail_tail, topo_map)
        for section in sections:
            new_trail = trail.trail_copy() 
            new_trail.append(section)
            if section.value == 9:
                new_trail.trailhead.peaks.append(section.location)
                new_trail.trailhead.score += 1
                # new_trail.trailhead.print_data()
                # for trail_section in new_trail.sections:
                    # trail_section.print_data()
                complete_trails.insert(0, new_trail)
            else:
                trails.insert(0, new_trail)

    total_score = 0
    for trailhead in trailheads:
        # trailhead.print_data()

        total_score += trailhead.score

    print(f'Total Score: {total_score}')

def get_sections(trailhead, topo_map):
    sections = []

    if trailhead.y > 0: # up
        section = check_section(trailhead, (trailhead.x, trailhead.y-1), topo_map)
        if section:
            sections.append(section)
    if trailhead.y < len(topo_map)-1: # down
        section = check_section(trailhead, (trailhead.x, trailhead.y+1), topo_map)
        if section:
            sections.append(section)
    if trailhead.x > 0: # left
        section = check_section(trailhead, (trailhead.x-1, trailhead.y), topo_map)
        if section:
            sections.append(section)
    if trailhead.x < len(topo_map[0])-1: # right
        section = check_section(trailhead, (trailhead.x+1, trailhead.y), topo_map)
        if section:
            sections.append(section)

    return sections

def check_section(trailhead, new_location, topo_map):
    new_value = get_section_value(new_location, topo_map) 
    if new_value - trailhead.value == 1:
        return Trail_Section(new_location, new_value)
    return None

def get_section_value(location, topo_map):
    return topo_map[location[1]][location[0]]

def get_trailheads(topo_map):
    trailheads = []
    for y, line in enumerate(topo_map):
        for x, value in enumerate(line):
            if value == 0:
                trailheads.append(Trail_Section((x, y), value))
    return trailheads

def print_map(topo_map):
    for line in topo_map:
        for value in line:
            print(value, end='')
        print()
    print()

class Trail_Section():
    trailhead_id_counter = 0
    def __init__(self, location, value):
        self.location = location
        self.x, self.y = location
        self.value = value
        if value == 0:
            self.score = 0
            self.trailhead_id = Trail_Section.trailhead_id_counter
            Trail_Section.trailhead_id_counter += 1
            self.peaks = []
            

    def is_trailhead(self):
        return self.value == 0

    def print_data(self):
        if self.is_trailhead():
            print(f'id:{self.trailhead_id} [{self.x},{self.y}] value:{self.value} score:{self.score}')
        else:
            print(f'[{self.x},{self.y}] value:{self.value}')

class Trail():
    def __init__(self, trailhead):
        self.trailhead = trailhead
        self.sections = [trailhead]

    def get_last(self):
        return self.sections[-1]

    def append(self, section):
        self.sections.append(section)

    def trail_copy(self):
        new_trail = Trail(self.trailhead)
        new_trail.sections = copy.copy(self.sections)
        return new_trail

main()