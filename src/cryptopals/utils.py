import binascii
import base64
from itertools import cycle


def hex_to_base64(value: str) -> str:
    return base64.b64encode(binascii.unhexlify(value)).decode()


def xor(a: str, b: str) -> str:
    return bytearray(
        a ^ b for a, b in zip(bytearray.fromhex(a), bytearray.fromhex(b))
    ).hex()


def score(text: str) -> int:
    score = 0
    for letter in text:
        if letter.upper() not in "ETAOIN SHRDLU":
            continue

        score += 1

    return score


def decrypt(cipher: bytes, key: int) -> bytes:
    return bytearray(c ^ key for c in bytearray.fromhex(cipher))


def repeating_key_xor(plaintext: str, key: str) -> str:
    return bytearray(
        byte ^ key for byte, key in zip(plaintext.encode(), cycle(key.encode()))
    ).hex()


def hamming_distance(a: str, b: str) -> int:
    xord = bytearray(x ^ y for x, y in zip(a.encode(), b.encode()))
    total = 0
    for x in xord:
        for bit in bin(x)[2:]:
            if bit != "1":
                continue
            total += 1
    return total
