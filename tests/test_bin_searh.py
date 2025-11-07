from src.bin_search import bin_search


def test_middle():
    assert bin_search([1, 2, 3, 4, 5], 4) == 3


def test_start():
    assert bin_search([1, 2, 3, 4], 2) == 1


def test_not_in_list():
    assert bin_search([1, 2, 3, 4], 5) == -1


def test_different_types():
    assert bin_search([1, 2, 3, 4], 23.45) == -1


def test_empty_list():
    assert bin_search([], 1) == -1


def test_one_element():
    assert bin_search([5], 5) == 0


def test_duplicate_elements():
    assert bin_search([1, 2, 2, 3, 4], 2) == 1


def test_negative_numbers():
    assert bin_search([-5, -3, -1, 0, 2], -3) == 1