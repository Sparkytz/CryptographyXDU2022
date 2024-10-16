#set1 challenge8

def ECB_repeat_blocks(text):
    a = [text[i:i+16] for i in range(0, len(text), 16)]
    n = len(a) - len(set(a))
    return n

def ECB_n_compare(texts):
    best = (-1, 0)
    for i in range(len(texts)):
        re_n = ECB_repeat_blocks(texts[i])
        best = max(best, (i, re_n), key=lambda t:t[1])
    return best

if __name__ == '__main__':
    ciphertexts = [bytes.fromhex(line.strip()) for line in open('./txt/3.txt')]
    out = ECB_n_compare(ciphertexts)
    print(out[1],'\n')
    print(out[0])