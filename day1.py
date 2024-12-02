from util import read_stripped_columns

filename = 'bin/day1.txt'

locations = read_stripped_columns(filename, nums=True)
for location_data in locations:
    location_data.sort()
print(locations)

distance_total = 0
for index in range(len(locations[0])):
    distance = abs(locations[0][index] - locations[1][index])
    distance_total += distance

print(f'Total: {distance_total}')