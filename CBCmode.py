#set2 challenge10
from idlelib.iomenu import encoding
from Crypto.Cipher import AES
from ECB import encrypt_ecb, decrypt_ecb
from base64 import b64decode


def XORdata(bdata1, bdata2):
    s=bytes([x ^ y for x, y in zip(bdata1, bdata2)])
    return s

def AES_CBC_ENC(key, text, IV):
    ciphertext = b''
    pre = IV
    for i in range(0, len(text), 16):
        cur_plaintext = text[i:i+16]
        cur_ciphertext = XORdata(cur_plaintext, pre)
        cipherblock = encrypt_ecb(key, cur_ciphertext)
        ciphertext = ciphertext + cipherblock
        pre = cipherblock
    return ciphertext

def AES_CBC_DEC(key, text, IV):
    plaintext = b''
    pre = IV
    for i in range(0, len(text), 16):
        cur_ciphertext = text[i:i+16]
        plainblock = decrypt_ecb(key, cur_ciphertext)
        cur_plaintext = XORdata(plainblock, pre)
        plaintext = plaintext + cur_plaintext
        pre = cur_ciphertext
    return plaintext

if __name__ == '__main__':
    with open('./txt/2.txt', 'r', encoding=encoding) as f:
        text = b64decode(f.read())
    key = b'YELLOW SUBMARINE'
    IV = b'\x00\x00\x00\x00'
    plaintext = AES_CBC_DEC(key, text, IV)
    s = plaintext.decode('utf-8', 'ignore')
    print(s)
