import re
from itertools import count


def read_rows_cols(filename):
    with open(filename, 'r') as file:
        rows = []
        cols = []
        for line in file:
            line_string = line.strip()
            rows.append(line_string)
        num_cols = len(rows[0].strip())
        for col_index in range(num_cols):
            col_string = ''
            for line_string in rows:
                col_string += line_string[col_index]
            cols.append(col_string)
        return rows, cols

def read_diagonals(grid):
    num_rows = len(rows)
    num_cols = len(rows[0])
    diagonals1 = []
    diagonals2 = []
    grid_pos_diagonal1 = []
    grid_pos_diagonal2 = []

    # diagonals moving from top left to bottom right as diagonals 1
    #   | abc |
    #   | def | = [g, dh, aei, bf, c]
    #   | ghi |
    #   | \\\ |
    #   | \\\ |
    #   | \\\ |
    for d in range(-num_rows + 1, num_cols):
        diagonal = ""
        diag_char_grid_positions = []
        for row in range(num_rows):
            col = row + d
            if 0 <= col < num_cols:
                diagonal += grid[row][col]
                diag_char_grid_positions.append([row,col])#assign each character a coordinate because my brain is not creative
        if len(diagonal) >= 3:
            diagonals1.append(diagonal) #Cutting off corners to avoid diagonals that are shorter than 3 characters
            grid_pos_diagonal1.append(diag_char_grid_positions)#assign lists of characters to master list in the same order the characters are added in the list of strings


    # diagonals moving from top right to bottom left as diagonals 2
    #   | abc |
    #   | def | = [a, bd, ceg, fh, i]
    #   | ghi |
    #   | /// |
    #   | /// |
    #   | /// |
    for d in range(num_rows + num_cols - 1):
        diagonal = ""
        diag_char_grid_positions = []
        for row in range(num_rows):
            col = d - row
            if 0 <= col < num_cols:
                diagonal += grid[row][col]
                diag_char_grid_positions.append([row, col])  # assign each character a coordinate because my brain is not creative
        if len(diagonal) >= 3:
            diagonals2.append(diagonal) #Cutting off corners to avoid diagonals that are shorter than 3 characters
            grid_pos_diagonal2.append(diag_char_grid_positions)  # assign lists of characters to master list in the same order the characters are added in the list of strings
    return diagonals1,grid_pos_diagonal1,diagonals2,grid_pos_diagonal2


def find_xmas(list):
    pattern_mas = r'MAS'
    pattern_sam = r'SAM'
    mas         = []
    sam         = []
    pos_m        = []
    pos_s        = []
    pos_list    = []

    for i in range(len(list)):
        #take string from each position in the list
        string = list[i]
        #seach string for all mas's and sam's
        mas += re.findall(pattern_mas,string)
        sam += re.findall(pattern_sam,string)
        #find character positions of each mas and sam in the string, position is the position of the 'a'
        match_m = re.finditer(pattern_mas,string)
        pos_m = [match.start() + 1 for match in match_m]
        match_s = re.finditer(pattern_sam,string)
        pos_s = [match.start() + 1 for match in match_s]
        #assemble mas and sam position lists and append to master pos_list
        char_pos_list = pos_m + pos_s
        pos_list.append(char_pos_list) #pos_list contains raw character position within the string. Not true grid coordinates
    #assemble list of located mas's and sams
    christmas_list = mas + sam
    #return assembled list of located mas's and sam's and the list of their locations.
    return christmas_list, pos_list

def print_list(list):
    for i in list:
        print(i)

def find_row_pos(row_pos):
    #converts raw row_pos data into grid coordinates
    coordinate_list = []
    for row in range(len(row_pos)):
        for col in row_pos[row]:
            coordinate = [row,col]
            coordinate_list.append(coordinate)
    return coordinate_list

def find_col_pos(col_pos):
    #converts raw col_pos data into grid coordinates
    coordinate_list = []
    for col in range(len(col_pos)):
        for row in col_pos[col]:
            coordinate = [row,col]
            coordinate_list.append(coordinate)
    return coordinate_list

def find_diag_pos(diag_pos,diag_gridpos):
    #converts raw diag1_pos data into grid coordinates by pulling the grid coordinates from the grid assigned when diagonal was parsed
    coordinate_list = []
    for i in range(len(diag_pos)):
        for j in diag_pos[i]:
            coordinate = diag_gridpos[i][j]
            coordinate_list.append(coordinate)
    return coordinate_list

def count_x_mas(row,col,count):
    count_list = []
    for i in row:
        for j in col:
            if i == j:
                count_list.append(i)
    new_count = len(count_list)
    new_count = count + new_count
    return new_count





rows, cols = read_rows_cols(input(f"Please input your filename\n-->"))
diag1,diag1_gridpos,diag2,diag2_gridpos = read_diagonals(rows)
print_list(rows)
print_list(cols)
print_list(diag1)
print_list(diag2)
rows, row_pos = find_xmas(rows)
cols, col_pos = find_xmas(cols)
diag1, diag1_pos = find_xmas(diag1)
diag2, diag2_pos = find_xmas(diag2)
row_pos = find_row_pos(row_pos)
col_pos = find_col_pos(col_pos)
diag1_pos = find_diag_pos(diag1_pos, diag1_gridpos)
diag2_pos = find_diag_pos(diag2_pos, diag2_gridpos)
x_mas_count = 0
# x_mas_count = count_x_mas(row_pos,col_pos,x_mas_count)
x_mas_count = count_x_mas(diag1_pos, diag2_pos, x_mas_count)
print(x_mas_count)
#1895 too high