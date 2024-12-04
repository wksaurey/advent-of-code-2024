from util import read_stripped_compressed_grid

def main():
    filename = 'bin/day4.txt'

    crossword = read_stripped_compressed_grid(filename)
    # print(crossword)

    count = 0
    matches = ['MAS', 'SAM']
    for line_index, line in enumerate(crossword):
        for value_index, value in enumerate(line):
            if value == 'A':
                if (line_index >= 1 and line_index < len(crossword) - 1 and
                        value_index >= 1 and value_index < len(line) - 1):

                    test_string1 = ''
                    for d_index in range(3):
                        test_value = crossword[line_index-1+d_index][value_index-1+d_index]
                        test_string1 += test_value
                    
                    test_string2 = ''
                    for d_index in range(3):
                        test_value = crossword[line_index-1+d_index][value_index+1-d_index]
                        test_string2 += test_value


                    if test_string1 in matches and test_string2 in matches:
                        print_square(line_index, value_index, crossword)
                        count += 1

    print(f'Count: {count}')
    # 1951 too low

def print_square(row_index, col_index, crossword):
    print('---')
    for i in range(row_index-1, row_index+2):
        print(''.join(crossword[i][col_index-1:col_index+2]))
                

main()
