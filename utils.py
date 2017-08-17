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


english_freq = {
    'a': 0.08167,
    'b': 0.01492,
    'c': 0.02782,
    'd': 0.04253,
    'e': 0.12702,
    'f': 0.02228,
    'g': 0.02015,
    'h': 0.06094,
    'i': 0.06966,
    'j': 0.00153,
    'k': 0.00772,
    'l': 0.04025,
    'm': 0.02406,
    'n': 0.06749,
    'o': 0.07507,
    'p': 0.01929,
    'q': 0.00095,
    'r': 0.05987,
    's': 0.06327,
    't': 0.09056,
    'u': 0.02758,
    'v': 0.00978,
    'w': 0.02360,
    'x': 0.00150,
    'y': 0.01974,
    'z': 0.00074,
}


def score(plaintext):
    """
    Based on chi-squared testing.
    """
    ignored = 0
    freq = {}
    for char in plaintext:
        if not char.lower() in english_freq:
            ignored += 1
            continue
        elif char.lower() in freq:
            continue

        freq[char.lower()] = plaintext.count(char)

    msg_len = len(plaintext) - ignored
    chi_squared = 0
    for letter, count in freq.items():
        observed = freq[letter.lower()]
        expected = english_freq[letter.lower()] * msg_len

        chi_squared += ((observed - expected) ** 2 ) / expected

    return chi_squared
