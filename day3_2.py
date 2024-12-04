import re

filename = 'bin/day3.txt'

pattern = "mul\(\d+,\d+\)|do\(\)|don't\(\)"
matches = re.findall(pattern, open(filename).read())

res = 0
flag = True
for match in matches:
    if match == "do()":
        flag = True
    elif match == "don't()":
        flag = False
    else:
        if flag:
            x, y = map(int, re.findall('\d+', match))
            res += x * y
print(res)