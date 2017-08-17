"""
The Cryptopals Crypto Challenges - Set 01
"""

import string

import utils


def challenge_03():
    """
    Single-byte XOR cipher
    """
    cipher = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    cipher = bytearray.fromhex(cipher)

    decrypted = []
    for char in string.ascii_uppercase:
        msg = bytearray([c ^ ord(char) for c in cipher])

        # (key, msg, score)
        decrypted.append((char, msg.decode(), utils.score(msg.decode())))

    return sorted(decrypted, key=lambda x: x[2])[0]


if __name__ == '__main__':
    print("Challenge 03 - Single-byte XOR cipher")
    result = challenge_03()
    print('key: %s\nplain: %s' % (result[0], result[1]))
