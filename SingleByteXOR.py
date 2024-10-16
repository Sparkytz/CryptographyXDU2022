#set challenge3
from collections import Counter
import string

# 定义字符频率表（基于英语文本的字符出现频率）
# 这里我们使用一个简单的频率表，但实际应用中可以使用更精确的数据
english_freq = {
    'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
    'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
    'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
    'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
    'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
    'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
    'y': .01974, 'z': .00074, ' ': .15000
    # ... 可以添加更多字符和它们的频率
    # 注意：为了简化，我们省略了低频字符和标点符号
}

# 定义可能的密钥范围
possible_keys = range(256)

# 加密的十六进制字符串
encrypted_hex = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

# 将十六进制字符串转换为字节
encrypted_bytes = bytes.fromhex(encrypted_hex)


# 函数：计算解密文本的得分
def score_text(text):
    # 只考虑字母字符，并计算它们的频率
    letter_counts = Counter(c.lower() for c in text if c.isalpha())
    total_letters = sum(letter_counts.values())

    # 计算得分（基于字符频率的加权和）
    score = sum(letter_counts[char] * english_freq.get(char, 0) for char in letter_counts)

    # 规范化得分（以便比较不同长度的文本）
    normalized_score = score / total_letters if total_letters > 0 else 0

    return normalized_score


# 尝试所有可能的密钥并找到得分最高的解密文本
best_score = 0
best_key = 0
best_text = ""

for key in possible_keys:
    decrypted_bytes = bytes([c ^ key for c in encrypted_bytes])
    decrypted_text = decrypted_bytes.decode('latin1', errors='ignore')  # 使用latin1解码，忽略错误
    print("current_score:",decrypted_text,"\n")
    # 计算解密文本的得分
    current_score = score_text(decrypted_text)

    # 更新最高得分、最佳密钥和最佳文本（如果当前得分更高）
    if current_score > best_score:
        best_score = current_score
        best_key = key
        best_text = decrypted_text

    # 输出结果
print(f"Best key: {best_key:#04x}")  # 以十六进制格式打印最佳密钥
print(f"Decrypted text:\n{best_text}")
#Cooking MC's like a pound of bacon