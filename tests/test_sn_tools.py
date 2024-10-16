# -*- coding: utf-8 -*-

from sixnine import SixNine

original_sixnine: int = 69
text_sixnine: str = "six nine"

sn = SixNine()


def test_sixnine_init():
    assert sn.__str__() == str(original_sixnine)


def test_sixnine_int():
    assert sn.int() == original_sixnine


def test_sixnine_bin():
    assert sn.bin() == bin(original_sixnine)


def test_sixnine_oct():
    assert sn.oct() == oct(original_sixnine)


def test_sixnine_hex():
    assert sn.hex() == hex(original_sixnine)
