import pytest

from root_finder.root import *

def test_zeroed_coeficients():
    assert calc_delta(0,0,0) == 0