import re
debug = True

def main():
    filename = 'bin/day3.txt'
    test_string = 'xmul(2,)h%mul[2,4]$2kmul(1111,3)aldkmul(2, 2), mul(45,7)'

    with open(filename) as file:
        memory = file.readlines()

        total = 0
        enabled = True
        for line in memory:
            for index, value in enumerate(line):
                if value in ['m', 'd']:
                    if re.search("^mul\([0-9]{1,3},[0-9]{1,3}\)", line[index:]):
                        test = line[index: index + 12]
                        print(test)
                        if enabled:
                            total += calculate(re.search("^mul\([0-9]{1,3},[0-9]{1,3}\)", line[index:]).group())
                            enabled = False

                    elif re.search("^do\(\)", line[index:]):
                        test = line[index: index + 4]
                        print(test)
                        print('enable')
                        enabled = True
                    elif re.search("^don't\(\)", line[index:]):
                        test = line[index: index + 7]
                        print(test)
                        print('disable')
                        enabled = False

        print(f'Total: {total}')
        # 8133565 too low

def calculate(value):
    values = re.findall("[0-9]{1,3}", value)
    if len(values) > 2:
        print('Found more than 2 values')
    result = int(values[0]) * int(values[1])
    debug(f'{values[0]} X {values[1]} = {result}')
    return result

def debug(value):
    if debug:
        print(value)

main()