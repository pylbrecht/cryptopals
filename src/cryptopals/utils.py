import binascii
import base64


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
