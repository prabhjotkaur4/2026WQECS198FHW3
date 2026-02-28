import pytest

from foo_bar_baz import foo_bar_baz

def test_3Multiples():
    assert foo_bar_baz(3) == "1 2 Foo"
    assert foo_bar_baz(6) == "1 2 Foo 4 Bar Foo"
    assert foo_bar_baz(9) == "1 2 Foo 4 Bar Foo 7 8 Foo"

def test_5Multiples():
    assert foo_bar_baz(5) == "1 2 Foo 4 Bar"
    assert foo_bar_baz(10) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar"


def test_BothMultiples():
    assert foo_bar_baz(15) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz"

def test_NonMultiple():
    assert foo_bar_baz(1) == "1"

def test_Empty():
    assert foo_bar_baz(0) == ""

def test_NegativeMultiple():
    assert foo_bar_baz(-3) == ""
    assert foo_bar_baz(-5) == ""