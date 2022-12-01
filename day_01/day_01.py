from utils.utils import load_text_file_get_grouped_numbers


def calculate_calories_per_gnome(gnomes: list) -> int:
    gnome_totals = []
    for gnome in gnomes:
        gnome_total = sum(gnome)
        gnome_totals.append(gnome_total)

    gnome_totals = sorted(gnome_totals, reverse=True)

    return sum(gnome_totals[0:3])


if __name__ == '__main__':
    gnomes = load_text_file_get_grouped_numbers('input.txt', __file__)
    print(calculate_calories_per_gnome(gnomes))
