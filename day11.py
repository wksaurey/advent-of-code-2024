def main():
    # filename = "input/day11_test.txt"
    filename = "input/day11.txt"
    stones = []
    with open(filename) as file:
        stones = file.readline().strip().split()

    # print(f'Initial Arrangement')
    # print(*stones)
    # print()

    blinks = 25
    plural = ''
    for blink_index in range(blinks):

        data_to_add = []
        index_offset = 0
        for index in range(len(stones)):
            stone = stones[index]
            if stone == '0':
                stones[index] = '1'
            elif len(stone) % 2 == 0:
                data_to_add.append((index+index_offset, stone[:int(len(stone)/2)]))
                stones[index] = str(int(stone[int(len(stone)/2):]))
                index_offset += 1
            else:
                stones[index] = str(int(stone) * 2024)

        for data in data_to_add:
                index, stone = data
                stones.insert(index, str(int(stone)))

        # print(f'After {blink_index+1} blink{plural}')
        # print(*stones)
        # print()
        # plural = 's'

    print(f'{len(stones)} Stones after {blinks} blinks')

main()