#set2 challenge12
from idlelib.iomenu import encoding

from ECB import encrypt_ecb
from Crypto.Cipher import AES
from base64 import b64decode
from Crypto.Random import get_random_bytes as randombytes

def Textbytenum():
    str = 'A'
    key = b'YELLOW SUBMARINE'
    cipher = AES.new(key, AES.MODE_ECB)
    for i in range(1,17):
        s = bytes(str * i, encoding='utf-8')
        try:
            ciphertext = cipher.encrypt(s)
            return len(s)
        except:
            continue

def AES_128_ECB(mytext, unknowtext, randkey, pos):
    alphabet = [chr(i) for i in range(0, 256)]
    text1 = mytext + bytes(chr(unknowtext[pos]), encoding='utf-8')
    ciphertext1 = encrypt_ecb(randkey, text1)
    for i in range(256):
        text2 = mytext + bytes(alphabet[i], encoding = 'utf-8')
        ciphertext2 = encrypt_ecb(randkey, text2)
        if ciphertext1 == ciphertext2:
            out = alphabet[i]
            break
        else:
            out = ''
    return out

if __name__ == '__main__':
    str = b'Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK'
    str = b64decode(str)
    l = len(str)
    n = Textbytenum() - 1
    outcome = ''
    mytext = bytes('A' * n, encoding='utf-8')
    key = randombytes(16)
    for i in range(len(str)):
        outcome = outcome + AES_128_ECB(mytext, str, key, i)
    print(outcome)


