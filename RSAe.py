import os
import time
from toolfunc import euclid

def RSAenc(m, e, n):
    return pow(m,e,n)

def RSAdec(c, d, n):
    return pow(c,d,n)

def finde(p):
    phin = p-1
    a = []
    for i in range(phin):
        if euclid(i, phin) == 1:
            a.append(i)
        else:
            a.append(10**30)
    return a

def count(e,p):
    result = 0
    for i in range(p):
        if RSAenc(i,e,p)==i:
            result +=1
    return result

if __name__ == "__main__":
    start = time.time()
    p = 1009
    q = 3643
    list_e1 = finde(p)
    list_e2 = finde(q)
    count1 = [count(e,p) for e in list_e1]
    count2 = [count(e,q) for e in list_e2]
    min_p = min(count1)
    min_q = min(count2)
    out = [ele for ele in range((p-1)*(q-1)) if count1[ele % (p-1)]==min_p and count2[ele % (q-1)]==min_q]
    a = sum(out)
    end = time.time()
    print(a,f'用时{end-start}s')
