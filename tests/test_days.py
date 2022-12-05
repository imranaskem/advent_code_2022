from day_01.day_01 import calculate_calories_per_gnome
from day_02.day_02 import calculate_score, process_file as d2_process_file
from day_03.day_03 import sum_prority, process_rucksacks
from day_04.day_04 import calculate_overlapped_pairs, process_areas

from utils.utils import load_text_file_get_grouped_numbers
from utils.utils import load_text_file, load_text_file_process


def test_calculate_calories_per_gnome():
    gnomes = load_text_file_get_grouped_numbers('input_01.txt', __file__)
    assert calculate_calories_per_gnome(gnomes) == 45000


def test_calculate_score():
    moves = load_text_file('input_02.txt', __file__, d2_process_file)
    assert calculate_score(moves) == 12


def test_sum_priority():
    rucksacks = load_text_file_process('input_03.txt', __file__, process_rucksacks)
    assert sum_prority(rucksacks) == 70


def test_calculate_overlapped_pairs():
    areas = load_text_file('input_04.txt', __file__, process_areas)
    assert calculate_overlapped_pairs(areas) == 4
