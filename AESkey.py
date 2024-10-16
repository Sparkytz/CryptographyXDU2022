from Crypto.Cipher import AES
import base64
import binascii
from hashlib import sha1


def jiou(ka):
    k = []
    a = bin(int(ka, 16))[2:]
    for i in range(0, len(a), 8):
        if (a[i:i + 7].count('1') % 2 == 0):
            k.append(a[i:i + 7] + '1')
        else:
            k.append(a[i:i + 7] + '0')
    knew = hex(int(''.join(k), 2))
    return knew[2:]


# step 1
a = [1, 1, 1, 1, 1, 6]
b = [7, 3, 1, 7, 3, 1]
c = 0
for i in range(len(a)):
    c += a[i] * b[i]
    c %= 10
# print(c)
# 7

# step 2
passport = '12345678<8<<<1110182<1111167<<<<<<<<<<<<<<<4'
no = passport[:10]
birth = passport[13:20]
arrive = passport[21:28]
mrz = no + birth + arrive
h_mrz = sha1(mrz.encode()).hexdigest()
# print(h_mrz)
# a095f0fdfe51e6ab3bf5c777302c473e7a59be65

# step 3
k_seed = h_mrz[:32]
c = '00000001'
d = k_seed + c
h_d = sha1(bytes.fromhex(d)).hexdigest()
# print(h_d)
# eb8645d97ff725a998952aa381c5307909962536

# step 4
ka = jiou(h_d[:16])
kb = jiou(h_d[16:32])
key = ka + kb

# step 5
cipher = '9MgYwmuPrjiecPMx61O6zIuy3MtIXQQ0E59T3xB6u0Gyf1gYs2i3K9Jxaa0zj4gTMazJuApwd6+jdyeI5iGHvhQyDHGVlAuYTgJrbFDrfB22Fpil2NfNnWFBTXyf7SDI'
cipher = base64.b64decode(cipher)

aes = AES.new(bytes.fromhex(key), AES.MODE_CBC, bytes.fromhex('0' * 32))
result = aes.decrypt(cipher).decode()
print(result)
# Herzlichen Glueckwunsch. Sie haben die Nuss geknackt. Das Codewort lautet: Kryptographie!