from day_01.day_01 import calculate_calories_per_gnome
from utils.utils import load_text_file_get_grouped_numbers


def test_calculate_calories_per_gnome():
    gnomes = load_text_file_get_grouped_numbers('input_01.txt', __file__)
    assert calculate_calories_per_gnome(gnomes) == 45000
