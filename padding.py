#set2 challenge9
from idlelib.iomenu import encoding


def pkcs7padding(text, bs):
    length = len(text)
    bs=int(bs)
    bytes_length = len(text)
    padding_size = length if (bytes_length == length) else bytes_length
    padding = (bs - padding_size % bs) %bs
    if 0< padding <16:
        text_padding = text + bytes([padding]*padding)
    else:
        text_padding = text
    return text_padding

def is_pkcs7(text):
    a = text[-text[-1]:]
    flag = all(a[i] == len(a) for i in range(len(a)))
    return flag

def pkcs7upad(text):
    if is_pkcs7(text):
        l = text[len(text)-1]
        text = text[:-l]
        return text
    else:
        return text

if __name__=="__main__":
    text=bytes(input("文本：\n"), encoding='utf-8')
    bs=input("块长：\n")
    text_padding = pkcs7padding(text, bs)
    print("填充文本：\n", text_padding)
    print(is_pkcs7(text_padding),'\n')
    print(pkcs7upad(text_padding))