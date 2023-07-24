#二次元累積和

class PrefixSum2D():
    
    def __init__(self, arr): #arr: 2次元配列(0-index)
        self.H = len(arr)
        self.W = len(arr[0])
        self.PS = [[0]*(self.W + 1) for _ in range(self.H + 1)]
        for i in range(self.H):
            for j in range(self.W):
                self.PS[i+1][j+1] = self.PS[i+1][j] + self.PS[i][j+1] - self.PS[i][j] + arr[i][j]
                
    def query(self, y0, x0, y1, x1)
        return self.PS[y1][x1] - self.PS[y1][x0] - self.PS[y0][x1] + self.PS[y0][x0]

#--------------------------------
#ABC311E - Defect-free Squares

"""
h,w,n = map(int,input().split())

A = [[0]*(w+1) for _ in range(h+1)]
for _ in range(n):
    y,x = map(int,input().split())
    A[y-1][x-1] = 1

ps = PrefixSum2D(A)
    
res = 0
for y in range(h):
    for x in range(w):
        ok = 0
        ng = min(h-y, w-x) + 1
        while abs(ng-ok) > 1: #正方形の辺の大きさでbinary-search
            d = (ok+ng)//2
            check = ps.query(y, x, y+d, x+d)
            if check == 0:
                ok = d
            else:
                ng = d
        res += ok
                
print(res)
"""

