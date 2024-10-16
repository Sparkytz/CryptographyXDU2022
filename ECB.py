#set1 challenge7
from base64 import b64decode
from Crypto.Cipher import AES
from padding import pkcs7padding, pkcs7upad
# AES块大小
BLOCK_SIZE = AES.block_size


def encrypt_ecb(key, plaintext):
    # 创建一个AES cipher对象，使用ECB模式
    cipher = AES.new(key, AES.MODE_ECB)
    # 对明文进行填充，使其长度是块大小的倍数
    #padded_plaintext = bytes(plaintext.encode('utf-8','ignore'))
    #pad(plaintext.encode('utf-8'), BLOCK_SIZE)
    plaintext = pkcs7padding(plaintext, 16)
    # 加密填充后的明文
    ciphertext = pkcs7padding(cipher.encrypt(plaintext),16)

    return ciphertext


def decrypt_ecb(key, ciphertext):
    # 创建一个AES cipher对象，使用ECB模式
    cipher = AES.new(key, AES.MODE_ECB)

    # 解密密文
    plaintext = cipher.decrypt(ciphertext)

    # 去除填充，恢复原始明文
    plaintext = pkcs7upad(plaintext)
    return plaintext

if __name__ == '__main__':
    # 示例密钥（必须是16, 24, 或 32字节长）
    key = b'YELLOW SUBMARINE'

    # 示例明文
    with open("./txt/1.txt", 'r') as f:
        plaintext = b64decode(f.read())
    # 加密
    ciphertext = decrypt_ecb(key, plaintext)
    print(f"Ciphertext (hex): {ciphertext.hex()}\n")
    s=ciphertext.decode('utf-8', 'ignore')
    print(s)
    # 解密
    #decrypted_plaintext = decrypt_ecb(key, ciphertext)
    #print(f"Decrypted Plaintext: {decrypted_plaintext}")