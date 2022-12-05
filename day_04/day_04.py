from utils.utils import load_text_file


def calculate_overlapped_pairs(areas):
    pairs_total = 0

    for area in areas:
        overlap = area[0].intersection(area[1])
        if len(overlap) > 0:
            pairs_total = pairs_total + 1

    return pairs_total


def process_areas(line):
    areas = line.split(',')
    area_ranges = []
    for area in areas:
        start_stop = [int(num) for num in area.split('-')]
        area_ranges.append(set(range(start_stop[0], start_stop[1] + 1)))

    return area_ranges


if __name__ == '__main__':
    areas = load_text_file('input.txt', __file__, process_areas)
    print(calculate_overlapped_pairs(areas))
