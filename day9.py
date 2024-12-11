from util import read_stripped_lines

def main():
    filename = 'bin/day9_test.txt'

    disk_map = read_stripped_lines(filename, nums=True)[0]

    print(disk_map)

    disk = []
    is_file = True

    id = 0
    for value in disk_map:
        if is_file:
            disk.append(File(id, value))
            id += 1
        else:
            disk.append(File('.', value))
        is_file = not is_file

    print_disk(disk)

    defrag(disk)

def defrag(disk):
    file_index, file = get_file(disk) 
    space_index, space = get_space(disk)

    print(f'File: {file.id}')
    print(f'Space: {space.id}')

    while True:
        if file.len == 0:
            disk.pop(file_index)
            file_index, file = get_file(disk) 
        if space.len == 0:
            disk.pop(space_index)
            space_index, space = get_space(disk)
            file_index -= 1

        if space_index > file_index:
            return

def get_file(disk):
    for index in range(len(disk)-1, -1, -1):
        file = disk[index]
        if file.id != '.':
            return index, file

def get_space(disk):
    for index, file in enumerate(disk):
        if file.id == '.':
            return index, file
    
def print_disk(disk):
    for file in disk:
        file.print()
    print()

class File:
    def __init__(self, id, len):
        self.id = id
        self.len = len

    def print(self):
        print(str(self.id) * self.len, end='')

main()