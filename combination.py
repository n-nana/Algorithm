def ncr(n, r, mod):
    if r > n:
        return 0
    rec = 1
    for i in range(r):
        rec *= (n-i)
        rec *= pow(i+1, mod-2, mod)
        rec %= mod
    return rec

#print(ncr(10,5,10**9+7))
