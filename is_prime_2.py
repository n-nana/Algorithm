#sqrt(n)

def isprime(n):
    if n <= 1:
        return False
    _i = 2
    while _i*_i <= n:
        if n%_i == 0:
            return False
        _i += 1
    return True

#k = 10**9 + 7
#print(isprime(k))
