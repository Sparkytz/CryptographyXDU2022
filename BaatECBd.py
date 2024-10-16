#set2 challenge14
from random import randbytes, randint

from ECB import encrypt_ecb
from Crypto.Cipher import AES
from base64 import b64decode
from Crypto.Random import get_random_bytes as randombytes
from AES128ECB import AES_128_ECB, Textbytenum

def randbytedetect(randbyte, unknowtext):
    key = randombytes(16)
    data1 = b'a'
    data2 = b'A'
    text1 = randbyte + data1 + unknowtext
    text2 = randbyte + data2 + unknowtext
    ciphertext1 = encrypt_ecb(key, text1)
    ciphertext2 = encrypt_ecb(key, text2)
    for i in range(len(ciphertext2)):
        if ciphertext1[i] != ciphertext2[i]:
            return i
        else:
            continue

def gettext(pos, text):
    unknowtext = text[pos:len(text)]
    return unknowtext

def getplaintext(randtext, mytext, unknowtext, key):
    pretext = randtext + unknowtext
    pos = randbytedetect(randtext, unknowtext)
    text = gettext(pos, pretext)
    outcome = ''
    for i in range(len(text)):
        outcome = outcome + AES_128_ECB(mytext, text, key, i)
    return outcome

if __name__ == '__main__':
    randbyte = randbytes(randint(1, 100))
    origintext = b'Tm93IGdlbmVyYXRlIGEgcmFuZG9tIGNvdW50IG9mIHJhbmRvbSBieXRlcyBhbmQgcHJlcGVuZCB0aGlzIHN0cmluZyB0byBldmVyeSBwbGFpbnRleHQuIFlvdSBhcmUgbm93IGRvaW5nOgpBRVMtMTI4LUVDQihyYW5kb20tcHJlZml4IHx8IGF0dGFja2VyLWNvbnRyb2xsZWQgfHwgdGFyZ2V0LWJ5dGVzLCByYW5kb20ta2V5KQpTYW1lIGdvYWw6IGRlY3J5cHQgdGhlIHRhcmdldC1ieXRlcy4='
    unknowtext = b64decode(origintext)
    n = Textbytenum() - 1
    key = randombytes(16)
    mytext = bytes('A' * n, encoding='utf-8')
    out = getplaintext(randbyte, mytext, unknowtext, key)
    print(out)


