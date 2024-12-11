import random

from gmpy2 import *
from toolfunc import *
import math
import numpy

Frame=[]
for i in range(21):
    with open(f'F:\QQ Files\QQDownloads\RSA加密体制破译题目\密码挑战赛赛题三\附件3-2\Frame{i}','r') as f:
        Frame.append(f.read())
N=[]
e=[]
cipher=[]
for i in range(21):
    N.append(int(Frame[i][0:256],16))
    e.append(int(Frame[i][256:512],16))
    cipher.append(int(Frame[i][512:768],16))
#第一部分帧破解，使用因数碰撞,得到第1和18个Frame的模数具有公因子
def factor_collision():
    p=euclid(N[1],N[18])
    q1 = N[1]//p
    q18 = N[18]//p
    phi1 = (p-1)*(q1-1)
    phi18 = (p-1)*(q18-1)
    d1 = inv(e[1],phi1)
    d18 = inv(e[18],phi18)
    m1 = pow(cipher[1],d1,N[1])
    m18 = pow(cipher[18],d18,N[18])
    text1 = bytes.fromhex(str(hex(m1))[-16:])
    text18 = bytes.fromhex(str(hex(m18))[-16:])
    return text1,text18#'. Imagin', 'm A to B'
print(factor_collision())
#第二部分帧破解，采用广播攻击,破解Frame3，8，12，16，20
def broadcast_attack():
    b = [cipher[3],cipher[8],cipher[12],cipher[16],cipher[20]]
    n = [N[3],N[8],N[12],N[16],N[20]]
    x,m = CRT([1,1,1,1,1],b,n)
    i = 20
    '''down = 63*(10**152)
    up = 10**154
    while up - down > 100:
        if ((down+up)//2)**5 < x:
            down = (down+up)//2
        else:
            up = (down+up)//2
    #print(up,down)
    for i in range(7985094500508197619216095179109374591466840832845633905102428354228364957393952749844260287135965730215484818378063570600824813771406220340542500306493501,7985094500508197619216095179109374591466840832845633905102428354228364957393952749844260287135965730215484818378063570600824813771406220340542500306493572):
        if i**5 == x:
            print(i)
            print(iroot(x,5))
            break'''
    m3 = int(iroot(x,5)[0])
    text3 = bytes.fromhex(str(hex(m3))[-16:])
    print(text3)
    return text3#'t is a f'
#第三部分帧破解，使用费马分解
def fermat_factor(num):
    n = N[num]
    temp = iroot(n,2)[0]
    q = next_prime(temp)
    while n%q != 0:
        q = next_prime(q)
    p = n//q
    phin = (p-1)*(q-1)
    d = inv(e[num],phin)
    m10 = pow(cipher[num],d,n)
    text10 = bytes.fromhex(str(hex(m10))[-16:])
    print(text10)
    return text10#'will get'

#第四部分帧破解，采用Pollard Rho算法
def pollard_rho(n):
    while True:
        x = randint(2,int(iroot(n,2)[0]))
        y = x
        c = 1
        i = 0
        j = 1
        z = 1
        while True:
            i+=1
            x = (x**2 + c) % n
            z = z*abs(y-x)%n
            if x == y or z == 0:
                break
            if i%63 == 0 or i == j:
                g = euclid(z,n)
                if g>1:
                    return g,n//g
                if i==j:
                    y = x
                    j = j<<1

def pollard_p(n):
    a = 2
    x = 1
    while (True):
        a = pow(a, x, n)
        g = euclid(a - 1, n)
        if (g != 1):
            print(g)
            return g,n//g
        x += 1

def gettext(factor,num):
    phin = (factor[0]-1)*(factor[1]-1)
    d = inv(e[num],phin)
    m_num = pow(cipher[num],d,N[num])
    text_num = bytes.fromhex(str(hex(m_num))[-16:])
    print(text_num)
    return text_num

def text_2619():
    ls = [2,6,19]
    for i in ls:
        factor = pollard_p(N[i])
        gettext(factor,i)
    #text2=' That is'
    #text6=' "Logic '
    #text19='instein.'
#第五部分帧破解，采用共模攻击
def gongmo():
    s,s1,s2 = gcdext(e[0],e[4])
    m0 = pow(cipher[0],s1,N[0])*pow(cipher[4],s2,N[0])%N[0]
    text0 = bytes.fromhex(str(hex(m0))[-16:])
    print(text0)
    return text0#'My secre'
frame = ['My secre','t is a f','amous sa','ying of ','Albert E','instein.',' That is',' “Logic ','will get',' you fro','m A to B','. Imagin','ation wi','ll take ','you ever','ywhere."']
for i in frame:
    print(i)