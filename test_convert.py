#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tests for convert module
"""

import convert


def test_convert_hex_to_base64():
    actual = convert.hex_to_base64(
        '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69'
        '736f6e6f7573206d757368726f6f6d'
    )
    assert actual == 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3' \
                     'VzIG11c2hyb29t'
