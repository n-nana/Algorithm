# 素因数分解([素因数、個数] ver.)

def fact(n):
    ans = []
    i = 2
    while i*i <= N:
        if n%i == 0:
            cnt = 0
            while n%i == 0:
                cnt += 1
                n //= i
            ans.append([i,cnt]) #[素因数,個数]
        else:
            i += 1
    if n != 1:
        ans.append([n,1])
    return ans

#N = 100 #N = 10368
#print(fact(N)) 
