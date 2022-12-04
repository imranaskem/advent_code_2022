from day_01.day_01 import calculate_calories_per_gnome
from day_02.day_02 import calculate_score, process_file as d2_process_file

from utils.utils import load_text_file_get_grouped_numbers
from utils.utils import load_text_file


def test_calculate_calories_per_gnome():
    gnomes = load_text_file_get_grouped_numbers('input_01.txt', __file__)
    assert calculate_calories_per_gnome(gnomes) == 45000


def test_calculate_score():
    moves = load_text_file('input_02.txt', __file__, d2_process_file)
    assert calculate_score(moves) == 12
