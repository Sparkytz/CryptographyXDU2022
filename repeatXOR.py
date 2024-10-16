#set1 challenge5
from binascii import hexlify


def repeatXOR(text, key):
    ciphertext = b''
    i=0
    for e in text:
        a = bytes([e ^ key[i]])
        ciphertext = ciphertext + a
        i = i+1 if i<len(key)-1 else 0
    #print(hexlify(ciphertext))
    return ciphertext

if __name__ =='__main__':
    text = b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    key = b'ICE'
    repeatXOR(text, key)