import binascii
import base64


def hex_to_base64(value: str) -> str:
    return base64.b64encode(binascii.unhexlify(value)).decode()
