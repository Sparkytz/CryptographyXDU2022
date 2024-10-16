#set2 challenge11
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes as randombytes
from numpy.random import randint
from padding import pkcs7padding
from ECBdetect import ECB_repeat_blocks
from base64 import b64decode
from ECB import encrypt_ecb
from CBCmode import AES_CBC_ENC, AES_CBC_DEC
import random

def AESkeyGenerator():
    key=randombytes(16)
    return key

def TextPad(text):
    n1 = randombytes(random.randint(5,10))
    n2 = randombytes(random.randint(5,10))
    text = n1 + text +n2
    return text

def EncrpyMode(text, key, mode):
    ciphertext = b''
    if mode == 0:
        ciphertext = encrypt_ecb(key, text)
    elif mode == 1:
        IV = randombytes(16)
        ciphertext = AES_CBC_ENC(key, text, IV)
    return ciphertext, IV

if __name__ == '__main__':
    text = bytes([0]*128)
    plaintext = pkcs7padding(TextPad(text), 16)
    key = AESkeyGenerator()
    mode = randint(0, 1)
    ciphertext, IV = EncrpyMode(plaintext, key, mode)

    flag = ECB_repeat_blocks(ciphertext)
    if flag > 0:
        print('加密模式为ECB')
    else:
        print('加密模式为CBC')
