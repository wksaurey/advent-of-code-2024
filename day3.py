import re
debug = True

def main():
    filename = 'bin/day3.txt'
    test_strings = [
        'xmul(2,)h%mul[2,4]$2kmul(1111,3)aldkmul(2, 2), mul(45,7)',
        "don't()mul(5,5)do()mul(2,4)mul(5,2)do()mul(8,7)"
    ]

    with open(filename) as file:
        memory = file.readlines()
        # memory = test_strings

        total = 0
        enabled = True
        for line in memory:
            # print('auto enable')
            # enabled = True
            for index, value in enumerate(line):
                if value in ['m', 'd']:
                    mul_pattern = re.search("^mul[(][0-9]{1,3},[0-9]{1,3}[)]", line[index:])
                    if mul_pattern:
                        if enabled:
                            print(f'{mul_pattern.group()}: ', end='')
                            total += calculate(re.search("^mul[(][0-9]{1,3},[0-9]{1,3}[)]", line[index:]).group())
                            enabled = False
                        else:
                            print(f'{mul_pattern.group()}: disabled')

                    do_pattern = re.search("^do[(][)]", line[index:])
                    if do_pattern:
                        print(f'{do_pattern.group()}: ', end='')
                        print('enable')
                        enabled = True

                    dont_pattern = re.search("^don't[(][)]", line[index:])
                    if dont_pattern:
                        print(f'{dont_pattern.group()}: ', end='')
                        print('disable')
                        enabled = False

        print(f'Total: {total}')
        # 8133565 too low
        # 9897377 too low

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