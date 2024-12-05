
def main():
    filename = 'bin/day5.txt'
    before_rules, updates = get_input(filename)
    print(updates)

    count = 0
    total = 0
    for update in updates:
        if check_page_order(update, before_rules):
            count += 1
            middle = int(update[int(len(update)/2)])
            print(middle)
            total += middle

    print(f'Count: {count}')
    print(f'Total: {total}')

def check_page_order(update, before_rules):
    for index, page in enumerate(update):
        # check if page is in the "before" attribute of all previous pages
        for i in range(index):
            previous_page = update[i]
            if previous_page in before_rules and page in before_rules[previous_page]:
                return False
    return True

def get_input(filename):
    with open(filename) as file:
        add_rules = True
        before_rules = {}
        updates = []
        for line in file:
            if line == '\n':
                add_rules = False
                continue

            if not add_rules:
                updates.append(line.strip().split(','))
                continue

            before, value = line.strip().split('|')
            if value in before_rules:
                before_rules[value].append(before)
            else:
                before_rules[value] = [before]


    return (before_rules, updates)



main()