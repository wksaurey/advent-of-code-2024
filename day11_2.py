def main():
    # filename = "input/day11_test.txt"
    filename = "input/day11.txt"
    stones_map = Stones_Map()
    with open(filename) as file:
        stones = file.readline().strip().split()
        for stone in stones:
            stones_map.increase_count(stone, 1)



    blinks = 75
    # plural = ''
    for blink_index in range(blinks):

        # print(f'{stones_map.len()} stones after {blink_index} blinks')
        # stones_map.print()
        for value in stones_map.stones:
            count = stones_map.get_count(value)
            if count == 0:
                continue

            # print(f'{value} -> ', end='')
            if value == '0':
                stones_map.add_to_map('1', count)
            elif len(value) % 2 == 0:
                value1 = str(int(value[:int(len(value)/2)]))
                value2 = str(int(value[int(len(value)/2):]))
                stones_map.add_to_map(value1, count)
                stones_map.add_to_map(value2, count)
                # print(stones_map.to_add[-2][0], end=' ')
            else:
                stones_map.add_to_map(str(int(value) * 2024), count)
            # print(stones_map.to_add[-1][0])

        stones_map.update_data()


        # print(f'After {blink_index+1} blink{plural}')
        # print(*stones_map)
        # print()
        # plural = 's'

    print(f'{stones_map.len()} stones after {blinks} blinks')

class Stones_Map():
    def __init__(self):
        self.stones = {}
        self.to_add = []
        self.to_remove = []

    def add_to_map(self, value, count):
        self.to_add.append((value, count))

    def increase_count(self, value, count):
        if value in self.stones:
            self.stones[value] += count
        else:
            self.stones[value] = count

    def get_count(self, value):
        self.to_remove.append(value)
        return self.stones[value]

    def update_data(self):
        for value in self.to_remove:
            self.stones[value] = 0
        for data in self.to_add:
            value, count = data
            self.increase_count(value, count)

        self.to_add = []
        self.to_remove = []

    def len(self):
        length = 0
        for value in self.stones:
            length += self.stones[value]
        return length

    def print(self):
        for value in self.stones:
            if self.stones[value] != 0:
                print(value, end=' ')
        print('\n')


main()