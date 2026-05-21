# test/check_sorted_array_test.py

from src.check_sorted_array import check_sorted_array


def test_sorted_ascending():
    assert check_sorted_array([1, 2, 3, 4, 5]) is True


def test_not_sorted():
    assert check_sorted_array([3, 1, 4, 2]) is False


def test_single_element():
    assert check_sorted_array([10]) is True


def test_duplicates_sorted():
    assert check_sorted_array([1, 1, 2, 2]) is True


def test_empty_list():
    assert check_sorted_array([]) is True
