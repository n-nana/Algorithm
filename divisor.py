def divisor(N):
    res = []
    for i in range(1, N+1):
        if i*i > N:
            break  
        if N%i != 0:
            continue
        res.append(i)
        if N//i != i:
            res.append(N//i)

    res.sort()
    return res

#print(divisor(30))
