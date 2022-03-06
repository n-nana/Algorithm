
def gcd(x,y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)

def lcm(x,y):
    return x*y//gcd(x,y)
        
#A,B = 16,24
#A,B = 24,16
#print(gcd(A,B), lcm(A,B))
