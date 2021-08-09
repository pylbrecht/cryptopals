import binascii
import base64


def hex_to_base64(value: str) -> str:
    return base64.b64encode(binascii.unhexlify(value)).decode()


def xor(a: str, b: str) -> str:
    return bytearray(
        a ^ b for a, b in zip(bytearray.fromhex(a), bytearray.fromhex(b))
    ).hex()
