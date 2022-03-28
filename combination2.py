import math

def ncr2(n, r):
    c = int(math.factorial(n) / (math.factorial(n - r) * math.factorial(r)))
    return c

#print(ncr2(50,25))
