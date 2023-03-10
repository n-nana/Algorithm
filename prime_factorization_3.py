#前計算
#一つの素因数分解をlog(N)で可能（N=10**6のとき20）

def func(n):
    _N = mx
    i = 2
    while i*i <= _N:
        if n%i == 0: return i
        else: i += 1
    return n

mx = 10**6
#mx = 10**4
D = [-1]*(mx+1)
for i in range(2,mx+1):
    D[i] = func(i)

#----------------------------
#N = 196
#res = []
#while N != 1:
#    res.append(D[N])
#    N //= D[N]   
#print(res)
