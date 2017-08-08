#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Utilities
"""


def fixed_xor(buf1, buf2):
    bytes1 = bytearray.fromhex(buf1)
    bytes2 = bytearray.fromhex(buf2)
    xored = bytearray([a ^ b for a, b in zip(bytes1, bytes2)])

    return xored.hex()
