from util import read_stripped_lines

def main():
    filename = 'bin/day9_test.txt'
    # filename = 'bin/day9.txt'

    disk_map = read_stripped_lines(filename, nums=True)[0]

    disk = []
    is_file = True

    id = 0
    for value in disk_map:
        if value == 0:
            if is_file:
                id += 1
            is_file = not is_file
            continue
        if is_file:
            disk.append(File(id, value))
            id += 1
        else:
            disk.append(File('.', value))
        is_file = not is_file

    defrag(disk)
    print_disk(disk)

    checksum = 0
    index = 0
    for file in disk:
        if file.is_space():
            break

        for _ in range(file.len):
            # print(f'{file.id} * {index} = {file.id * index}')
            checksum += index * file.id
            index += 1

    print(f'Checksum: {checksum}')
    # 258894222412 too low

def defrag(disk):

    while True:
        print_disk(disk)
        # print(f'Disk len: {len(disk)}')
        # print(f'Space len {disk[-1].len}')
        file_index, file = get_file(disk) 
        space_index, space = get_space(disk)
        print(f'File: {file.id}')

        if space_index > file_index:
            break

        if file.len > space.len:
            if disk[-1].is_space():
                disk[-1].len += space.len
            else:
                disk.insert(len(disk), File(space.id, space.len))
            space.id = file.id
            file.len -= space.len
        elif space.len > file.len:
            disk.insert(space_index, file)
            if disk[-1].is_space():
                disk[-1].len += space.len
            else:
                disk.insert(len(disk), File(space.id, file.len))
            space.len -= file.len
            file_index, file = get_file(disk) 
            disk.pop(file_index)
        elif file.len == space.len:
            space.id = file.id
            if disk[-1].is_space():
                disk[-1].len += space.len
            else:
                disk.insert(len(disk), File(space.id, file.len))
            file_index, file = get_file(disk) 
            disk.pop(file_index)

        if disk[-1].is_space() and disk[-2].is_space():
            disk[-2].len += disk[-1].len
            disk.pop()

# def consolidate_space(disk):
#     index = 0
    
#     while index < len(disk)-1:
#         file0 = disk[index]
#         file1 = disk[index+1]
#         if file0.is_space() and file1.is_space():
#             file0.len += file1.len
#             disk.pop(index+1)
#         else:
#             index += 1


def get_file(disk):
    for index in range(len(disk)-1, -1, -1):
        file = disk[index]
        if not file.is_space():
            return index, file

def get_space(disk):
    for index, file in enumerate(disk):
        if file.is_space():
            return index, file
    
def print_disk(disk):
    for file in disk:
        file.print()
    print()

class File:
    def __init__(self, id, len):
        self.id = id
        self.len = len

    def is_space(self):
        return self.id == '.'

    def print(self):
        print(str(self.id) * self.len, end='')

main()