# 素因数分解

def fact(n):
    _N = n #上限
    ans = []
    i = 2
    while i*i <= _N:
        if n%i == 0:
            ans.append(i)
            n //= i
        else:
            i += 1
    if n != 1:
        ans.append(n)
    return ans

# N = 100
# print(fact(N))  

