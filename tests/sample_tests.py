from nose.tools import *

from sample import add_func

def test_add():
    assert_equal(add_func(1,2), 3)

