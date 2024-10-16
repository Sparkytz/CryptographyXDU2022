#set2 challenge16
from CBCmode import AES_CBC_DEC, AES_CBC_ENC
from Crypto import Random
from Crypto.Cipher import AES

class Oracle:
    def __init__(self):
        self.key=Random.new().read(AES.key_size[0])
        self.iv =Random.new().read(AES.block_size)
        self.prefix = "comment1=cooking%20MCs;userdata="
        self.suffix = ";comment2=%20like%20a%20pound%20of%20bacon"

    def encrypt(self, data):
        data = data.replace(';', '').replace('=', '')
        plaintext = (self.prefix + data + self.suffix).encode()
        return AES_CBC_ENC( self.key, plaintext,self.iv)

    def decrypt_and_check_admin(self, ciphertext):
        data = AES_CBC_DEC(self.key, ciphertext, self.iv)
        return b';admin=true;' in data

def find_block_length(encryption_oracle):
    mytext = ''
    ciphertext = encryption_oracle(mytext)
    initial_len = len(ciphertext)
    new_len = initial_len
    while new_len == initial_len:
        mytext += 'A'
        ciphertext = encryption_oracle(mytext)
        new_len = len(ciphertext)
    return new_len - initial_len

def find_prefix_length(encryption_oracle, block_length):
    ciphertext_a = encryption_oracle('A')
    ciphertext_b = encryption_oracle('B')
    common_len =0
    while ciphertext_a[common_len] == ciphertext_b[common_len]:
        common_len += 1
    common_len = int(common_len / block_length) * block_length
    for i in range(1, block_length +1):
        ciphertext_a = encryption_oracle('A' * i + 'X')
        ciphertext_b = encryption_oracle('A' * i + 'Y')
        if ciphertext_a[common_len:common_len + block_length] == ciphertext_b[common_len:common_len + block_length]:
            return common_len + (block_length - i)


def cbc_bit_flip(encryption_oracle):
    block_length= find_block_length(encryption_oracle.encrypt)
    prefix_length = find_prefix_length(encryption_oracle.encrypt, block_length)
    additional_prefix_bytes = (block_length - (prefix_length % block_length))% block_length
    total_prefix_length = prefix_length + additional_prefix_bytes
    plaintext = "?admin?true"
    additional_plaintext_bytes = (block_length -(len(plaintext) % block_length)) % block_length
    final_plaintext = additional_plaintext_bytes * '?' + plaintext
    ciphertext = encryption_oracle.encrypt(additional_prefix_bytes * '?' + final_plaintext)
    semicolon = ciphertext[total_prefix_length - 11] ^ ord('?')^ ord(';')
    equals = ciphertext[total_prefix_length - 5] ^ ord('?')^ ord('=')
    forced_ciphertext = ciphertext[:total_prefix_length - 11] + bytes([semicolon]) + \
                        ciphertext[total_prefix_length -10:total_prefix_length -5] + \
                        bytes([equals])+ ciphertext[total_prefix_length - 4:]
    return forced_ciphertext

if __name__ == '__main__':
    encryption = Oracle()
    f_ciphertext = cbc_bit_flip(encryption)
    dec_check = encryption.decrypt_and_check_admin(f_ciphertext)
    print(dec_check)
