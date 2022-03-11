#ABC238E - Range Sums

class UnionFind:
    
    def __init__(self, n):
        self.par = [-1]*n #
        self.rank = [0]*n # 木の高さ
    
    #xのrootを取得
    def find(self, x):
        if self.par[x] == -1:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]
    
    #xとyを併合
    def unite(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            rx,ry = ry,rx #rx: 親, ry: 子
        self.par[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        
        return True
            
    #xとyが同一groupかどうか
    def check(self, x, y):
        return self.find(x) == self.find(y)


#---------------------------------------------------
N,Q = map(int, input().split())
uf = UnionFind(N+1)

for _ in range(Q):
    l,r = map(int, input().split())
    uf.unite(l-1,r)

#print(uf.par)

#0とNの親が同じであればYes
if uf.check(0,N):
    print("Yes")
else:
    print("No")



