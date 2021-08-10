from cryptopals import utils


def test_hex_to_base64():
    hex_ = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"  # noqa: E501
    b64 = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
    assert utils.hex_to_base64(hex_) == b64


def test_xor():
    a = "1c0111001f010100061a024b53535009181c"
    b = "686974207468652062756c6c277320657965"
    result = "746865206b696420646f6e277420706c6179"
    assert utils.xor(a, b) == result


def test_repeating_key_xor():
    plaintext = (
        "Burning 'em, if you ain't quick and nimble\n"
        "I go crazy when I hear a cymbal"
    )
    cipher = (
        "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272"
        "765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326"
        "302e27282f"
    )
    key = "ICE"
    assert utils.repeating_key_xor(plaintext, key) == cipher
