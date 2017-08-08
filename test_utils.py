#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tests for `utils` module.
"""

import utils


def test_fixed_xor():
    buf1 = r'1c0111001f010100061a024b53535009181c'
    buf2 = r'686974207468652062756c6c277320657965'
    expected = r'746865206b696420646f6e277420706c6179'
    assert utils.fixed_xor(buf1, buf2) == expected
