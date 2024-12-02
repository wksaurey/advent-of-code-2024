from util import read_stripped_columns

filename = 'bin/day1.txt'

locations = read_stripped_columns(filename, nums=True)
for location_data in locations:
    location_data.sort()

distance_total = 0
for left_value in locations[0]:
    value_count = 0
    for right_value in locations[1]:
        if left_value == right_value:
            value_count += 1
    distance_total += left_value * value_count


print(f'Total: {distance_total}')