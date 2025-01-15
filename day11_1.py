def main():
    # filename = "input/day11_test.txt"
    filename = "input/day11.txt"
    stones = []
    with open(filename) as file:
        stones = file.readline().strip().split()

    # print(f'Initial Arrangement')
    # print(*stones)
    # print()

    blinks = 75
    plural = ''
    last_count = len(stones)
    last_delta = 0
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

        print(f'{len(stones)} Stones after {blink_index+1} blinks')
        current_count = len(stones)
        current_delta = current_count - last_count
        print(f'Delta {current_count - last_count}')
        print(f'Delta Delta {current_delta - last_delta}')
        last_count = current_count
        last_delta = current_delta
        # print(f'After {blink_index+1} blink{plural}')
        # print(*stones)
        # print()
        # plural = 's'

    print(f'{len(stones)} Stones after {blinks} blinks')

main()