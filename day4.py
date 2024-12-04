from util import read_stripped_compressed_grid

def main():
    filename = 'bin/day4.txt'

    crossword = read_stripped_compressed_grid(filename)
    print(crossword)

    count = 0
    matches = ['XMAS', 'SAMX']
    for line_index, line in enumerate(crossword):
        for value_index, value in enumerate(line):
            if value == 'X':
                top = False 
                bottom = False 
                left = False 
                right = False
                if line_index >= 3:
                    top = True
                if len(crossword) - line_index > 3:
                    bottom = True
                if value_index >= 3:
                    left = 3
                if len(line) - value_index > 3:
                    right = 3

                if top:
                    test_string = ''
                    for i in range(line_index-3, line_index+1):
                        test_value = crossword[i][value_index]
                        test_string += test_value
                    if test_string in matches:
                        print(f'Top: {test_string}')
                        count += 1
                if bottom:
                    test_string = ''
                    for i in range(line_index, line_index+4):
                        test_value = crossword[i][value_index]
                        test_string += test_value
                    if test_string in matches:
                        print(f'Bottom: {test_string}')
                        count += 1
                if left:
                    test_string = ''.join(line[value_index-3:value_index+1])
                    if test_string in matches:
                        print(f'Left: {test_string}')
                        count += 1
                if right:
                    test_string = ''.join(line[value_index:value_index+4])
                    if test_string in matches:
                        print(f'Right: {test_string}')
                        count += 1

                if top and left:
                    test_string = ''
                    for d_index in range(4):
                        test_value = crossword[line_index-d_index][value_index-d_index]
                        test_string += test_value
                    if test_string in matches:
                        print(f'Top Left: {test_string}')
                        count += 1

                if top and right:
                    test_string = ''
                    for d_index in range(4):
                        test_value = crossword[line_index-d_index][value_index+d_index]
                        test_string += test_value
                    if test_string in matches:
                        print(f'Top Right: {test_string}')
                        count += 1

                if bottom and left:
                    test_string = ''
                    for d_index in range(4):
                        test_value = crossword[line_index+d_index][value_index-d_index]
                        test_string += test_value
                    if test_string in matches:
                        print(f'Bottom Left: {test_string}')
                        count += 1

                if bottom and right:
                    test_string = ''
                    for d_index in range(4):
                        test_value = crossword[line_index+d_index][value_index+d_index]
                        test_string += test_value
                    if test_string in matches:
                        print(f'Bottom Right: {test_string}')
                        count += 1


    print(f'Count: {count}')


                

main()
