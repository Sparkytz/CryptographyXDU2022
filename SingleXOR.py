#set1 challenge4

latter_frequency = {
    'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
    'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
    'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
    'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
    'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
    'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
    'y': .01974, 'z': .00074, ' ': .15000
}


# s = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

def English_Scoring(t):
    return sum([latter_frequency.get(chr(i), 0) for i in t.lower()])


def Single_XOR(s, single_character):
    t = b''
    # print(s,single_character)
    # s = bytes.fromhex(s)
    # t: the XOR'd result
    for i in s:
        t = t + bytes([i ^ single_character])
        # t = re.sub(r'[\x00-\x1F]+','', t) 
        # remove the ascii control characters
    return t


def ciphertext_XOR(s, single_character):
    _data = []
    s = bytes.fromhex(s)
    # key = ord (single_character)
    # ciphertext = b''
    # for i in s :
    #     ciphertext = ciphertext + bytes([i ^ key])
    ciphertext = Single_XOR(s, single_character)
    # print(ciphertext)
    score = English_Scoring(ciphertext)
    data = {
        'Single character': single_character,
        'ciphertext': ciphertext,
        'score': score
    }
    _data.append(data)
    score = sorted(_data, key=lambda score: score['score'], reverse=True)[0]
    return score


if __name__ == '__main__':
    _data = []
    s = open('./txt/set1q4.txt').read().splitlines()
    for i in s:
        # print(i)
        for j in range(256):
            data = ciphertext_XOR(i, j)
            _data.append(data)
    best_score = sorted(_data, key=lambda score: score['score'], reverse=True)[0]
    print(best_score)
    for i in best_score:
        print("{}: {}".format(i.title(), best_score[i]))

    # print(f'{j}:{t},{score}')

