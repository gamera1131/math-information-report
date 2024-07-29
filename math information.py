import sympy as sp
from sympy import isprime
import numpy as np
#アルファベットto数字の対応表
num_to_alp = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
alphabet = {'a':0,'b':1,'c':2,"d":3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
def alp_to_num(code): #pの算出
    #文字列をリスト化
    code_trs = list(code)
    code_len = len(code_trs)
    for i in range (code_len):
        for j in range (26):
            if (code_trs[i] == num_to_alp[j]):
                interim = num_to_alp[j]
                code_trs[i] = alphabet[interim]
    P = 0
    for i in range (code_len):
        P +=  code_trs[i]*pow(26,code_len - (i + 1))
    return P

def prime():#素数生成
    prime_Check_F = 0
    while (prime_Check_F == 0):
        rng = np.random.default_rng()
        code_trs = list(code)
        code_len = len(code_trs)
        if code_len < 5:
            pr = rng.integers(100,1000)
        elif code_len < 6:
            pr = rng.integers(1000,10000)
        else:
            pr = rng.integers(10000,100000)
        prime_F = isprime(pr)
        if prime_F == True:
            prime_Check_F = 1
            return pr

def prime2(max,L):
    prime_Check_F = 0
    while (prime_Check_F == 0):
        rng = np.random.default_rng()
        pr = rng.integers(max,L)
        prime_F = isprime(pr)
        if prime_F == True:
            prime_Check_F = 1
            return pr

def test(P,e,n,F):
    # C ≡ P ^ e (mod n)を求める
    C = 1
    for i in range(e):
        C = C * P % n
    cryptography = str(np.base_repr(C, 26))#26進数に
    cryptography_lis = list(cryptography)
    cryptography_len = len(cryptography_lis)

    #aがあるとき0が出てこないため調整処理
    code_trs = list(code)
    code_len = len(code_trs)
    if (F == 1):
        while (code_len > cryptography_len):
            cryptography_lis.insert(0,"0")
            cryptography_len += 1
    
    for i in range(cryptography_len):
        cryptography_lis[i] = int(cryptography_lis[i],26)
    
    sent = str()
    for i in range(cryptography_len):
        sent += num_to_alp[cryptography_lis[i]]
    return sent


#暗号化
code = input("暗号化したい文字列を入力してください>>>")
P = alp_to_num(code)
p = prime()
q = prime()
n = p*q
L = int((p-1) * (q-1) / 2)
if (p > q):
    e = prime2(p,L)
else:
    e= prime2(q,L)
F = 0
sent = test(P,e,n,F)
print("暗号文は",sent,"です")#暗号文

#復号化
d,y,g = sp.gcdex(e,L)
d %= L
C = alp_to_num(sent)
F = 1
P2 = test(C,d,n,F)
print("平文は",P2,"です")
