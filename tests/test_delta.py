import pytest

from root_finder.root import calc_delta, calc_root


def test_delta_zeroed_coeficients():
    assert calc_delta(0, 0, 0) == 0


def test_delta_zeroed_b():
    assert calc_delta(1, 0, 2) == ((-4) * 1 * 2)


def test_delta_zeroed_a():
    assert calc_delta(0, 1, 2) == 1


def test_delta_zeroed_c():
    assert calc_delta(1, 1, 0) == 1


def test_negative_delta():
    assert calc_delta(1, 1, 3) < 0


def test_zeroed_delta():
    assert calc_delta(4, 4, 1) == 0


def test_positive_delta():
    assert calc_delta(3, 4, 1) > 0


def test_non_real_roots():
    with pytest.raises(Exception) as _:
        assert calc_root(-1, 1, 0)


def test_root_with_zeroed_a():
    with pytest.raises(Exception) as _:
        assert calc_root(-1, 0, 0)


def test_unique_root():
    assert calc_root(0, 1, -2) == (1, 1)


def test_positive_roots():
    assert calc_root(1, 1, -2) == (0.5, 1.5)


def test_negative_roots():
    assert calc_root(1, 1, 2) == (-1.5, -0.5)


def test_positive_and_negative_roots():
    assert calc_root(4, 1, 1) == (-1.5, 0.5)
