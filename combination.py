def ncr(n, r, mod):
    if r > n:
        return 0
    x = 1
    for i in range(r):
        x *= (n-i)
        x *= pow(i+1, mod-2, mod)
        x %= mod
    return x

#print(ncr(10,5,10**9+7))
