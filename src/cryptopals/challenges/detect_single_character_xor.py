from cryptopals import utils
from operator import itemgetter
import pathlib


def challenge():
    input_file = pathlib.Path(__file__).parent / "4.txt"
    content = input_file.read_text().split('\n')

    decrypted = []
    for cipher in content:
        for key in range(128):
            try:
                plaintext = utils.decrypt(cipher, key).decode()
            except UnicodeDecodeError:
                continue

            decrypted.append(
                (
                    utils.score(plaintext),
                    chr(key),
                    plaintext,
                )
            )

    return sorted(decrypted, key=itemgetter(0))[-1]


if __name__ == "__main__":
    _, key, plaintext = challenge()
    print(f"key: {key}")
    print(repr(plaintext))
