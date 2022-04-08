# 素数判定（エラトステネス）

def isprime(n):
    table = [True for _ in range(n+1)]

    #（前処理）
    table[0], table[1] = False, False

    # Main
    for i in range(2, n+1):
        if not table[i]:
            continue
    
        m = i*2
        while m <= n:
            table[m] = False
            m += i
    
    return table

#-------------------------------
#n = 10
#print(isprime(n))

