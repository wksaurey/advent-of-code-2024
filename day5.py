
def main():
    filename = 'bin/day5.txt'
    before_rules, updates = get_input(filename)

    ordered_total = 0
    un_ordered_total = 0
    for update in updates:
        if check_page_order(update, before_rules):
            middle = int(update[int(len(update)/2)])
            ordered_total += middle
        else:
            update = reorder_update(update, before_rules)
            middle = int(update[int(len(update)/2)])
            un_ordered_total += middle

    print(f'Ordered Total: {ordered_total}')
    print(f'Un-Ordered Total: {un_ordered_total}')


def reorder_update(update, before_rules):
    while not check_page_order(update, before_rules):
        for index, page in enumerate(update):
            for i in range(index):
                previous_page = update[i]
                if previous_page in before_rules and page in before_rules[previous_page]:
                    update.insert(index, update.pop(i))
    return update

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