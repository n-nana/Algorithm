#ABC185F
#XORをとる問題

class FenwickTree:
    def __init__(self, n):
        self.n_ft = n
        self.bit = [0]*(n+1)
        
    def query(self, k):
        s = 0
        while k > 0:
            s ^= self.bit[k] ###
            k -= k&(-k)
        return s
        
    def update(self, k, a):
        while k <= self.n_ft:
            self.bit[k] ^= a ###
            k += k&(-k)
        
#-------------------
N,Q = map(int,input().split())
A = list(map(int,input().split()))
ft = FenwickTree(N)

for i in range(N):
    ft.update(i+1,A[i])

for _ in range(Q):
    c,x,y = map(int,input().split())
    if c == 1:
        ft.update(x,y)
#        print(ft.bit)
    else:
        res = ft.query(y) ^ ft.query(x-1) 
        print(res)
    
