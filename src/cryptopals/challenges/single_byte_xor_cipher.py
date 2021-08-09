from cryptopals import utils
from operator import itemgetter
from collections import Counter


def challenge():
    cipher = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    decrypted = []
    for key in range(128):
        plaintext = utils.decrypt(cipher, key).decode()
        decrypted.append((
            utils.score(plaintext),
            chr(key),
            plaintext,
        ))

    return sorted(decrypted, key=itemgetter(0))[-1]


if __name__ == "__main__":
    _, key, plaintext = challenge()
    print(f"key: {key}")
    print(repr(plaintext))
