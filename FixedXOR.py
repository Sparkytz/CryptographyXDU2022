#set1 challenge2
from sympy import false

def FixedXOR(a,b):
    if len(a)==len(b):
        c=int(a,16)^int(b,16)
        return hex(c)
    else:
        print("错误！长度不一致！")
        return false

a=input("a:")
b=input("b:")
c = FixedXOR(a,b)
print("c=", c)