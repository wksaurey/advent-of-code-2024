import re
debug = True

def main():
    filename = 'bin/day3.txt'
    test_string = 'xmul(2,)h%mul[2,4]$2kmul(1111,3)aldkmul(2, 2), mul(45,7)'

    with open(filename) as file:
        memory = file.readlines()

        total = 0
        for line in memory:
            instructions = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)", line)

            for instruction in instructions:
                values = re.findall("[0-9]{1,3}", instruction)
                if len(values) > 2:
                    print('Found more than 2 values')
                result = int(values[0]) * int(values[1])
                debug(f'{values[0]} X {values[1]} = {result}')
                total += result

        print(f'Total: {total}')
        # 28476021 too low

def debug(value):
    if debug:
        print(value)

main()