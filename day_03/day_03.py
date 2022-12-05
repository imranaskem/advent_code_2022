from utils.utils import load_text_file_process


def process_rucksacks(file):
    groups = []
    group = []
    count = 0
    for line in file:
        ruck = line.replace('\n', '')
        if count == 3:
            groups.append(group)
            group = []
            count = 0
        group.append(ruck)
        count = count + 1
    groups.append(group)
    return groups


def sum_prority(rucksacks):
    priority_total = 0

    for rucksack in rucksacks:
        duplicate_item = set(rucksack[0]).intersection(rucksack[1]).intersection(rucksack[2])

        for char in duplicate_item:
            if char.isupper():
                priority_total = priority_total + ord(char) - 38
                continue
            if char.islower():
                priority_total = priority_total + ord(char) - 96
                continue
            raise ValueError('Item is not a letter')

    return priority_total


if __name__ == '__main__':
    rucksacks = load_text_file_process('input.txt', __file__, process_rucksacks)
    print(sum_prority(rucksacks))
