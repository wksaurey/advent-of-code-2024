from util import read_stripped_grid

def main():
    filename = 'bin/day2.txt'

    reports = read_stripped_grid(filename, nums=True)

    safe_count = 0
    for report in reports:
        # report_safety = is_safe(report)
        # print(report_safety)
        if is_safe(report):
            safe_count += 1
        else:
            print(report)

    print(f'Safe Count: {safe_count}')
    # 518 too low

def is_safe(report, problem_dampening=True):
    is_increasing = True
    for index, level in enumerate(report):
        if index == 0:
            continue

        last_level = report[index-1]

        if index == 1:
            is_increasing = last_level > level

        if (last_level > level) != is_increasing:
            if problem_dampening:
                return dampen(report)
            else:
                return False

        if abs(last_level - level) > 3 or abs(last_level - level) < 1:
            if problem_dampening:
                return dampen(report)
            else:
                return False
    return True

def dampen(report):
    for index in range(len(report)):
        sub_report = report[:index] + report[index+1:]
        if is_safe(sub_report, problem_dampening=False):
            return True

    return False

main()