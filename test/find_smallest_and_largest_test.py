# test_find_smallest_and_largest.py

from src.find_smallest_and_largest import find_smallest_and_largest


def test_normal_array():
    assert find_smallest_and_largest([5, 2, 9, 1, 7]) == (1, 9)


def test_single_element():
    assert find_smallest_and_largest([10]) == (10, 10)


def test_negative_numbers():
    assert find_smallest_and_largest([-5, -2, -9, -1]) == (-9, -1)


def test_mixed_numbers():
    assert find_smallest_and_largest([-10, 0, 5, 3]) == (-10, 5)


def test_duplicates():
    assert find_smallest_and_largest([4, 4, 4, 4]) == (4, 4)


def test_sorted_array():
    assert find_smallest_and_largest([1, 2, 3, 4, 5]) == (1, 5)


def test_reverse_sorted_array():
    assert find_smallest_and_largest([9, 8, 7, 6, 5]) == (5, 9)
