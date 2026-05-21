# test/check_prime_number_test.py

from src.check_prime_number import check_prime_number


def test_small_primes():
    assert check_prime_number(2) is True
    assert check_prime_number(3) is True
    assert check_prime_number(5) is True
    assert check_prime_number(7) is True


def test_non_primes():
    assert check_prime_number(1) is False
    assert check_prime_number(0) is False
    assert check_prime_number(4) is False
    assert check_prime_number(9) is False
    assert check_prime_number(15) is False


def test_negative_numbers():
    assert check_prime_number(-5) is False
    assert check_prime_number(-1) is False


def test_large_prime():
    assert check_prime_number(29) is True
