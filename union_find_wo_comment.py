class UnionFind:
    
    def __init__(self, n):
        self.par = [-1]*n # 要素の根（親）
        self.rank = [0]*n # 要素が属している木の高さ
        self.siz = [1]*n # 要素が属している木の大きさ（要素数）

    # xのroot(Find)
    def root(self, x):
        if self.par[x] == -1:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]
    
    # xとyをmerge(Union)
    def merge(self, x, y):
        rx,ry = self.root(x), self.root(y)
        if rx == ry: return False
        if self.rank[rx] < self.rank[ry]:
            rx,ry = ry,rx # rx: 親, ry: 子
        self.par[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1        
        self.siz[rx] += self.siz[ry]
        return True
            
    # xとyが同一のgroupかどうか
    def issame(self, x, y):
        return self.root(x) == self.root(y)
    
    # xが含まれる木のサイズ
    def size(self, x):
        return self.siz[self.root(x)]

#---------------------------------------------------
#N = int(input())
#uf = UnionFind(N)
#uf.root(X)
#uf.merge(X,Y)
#uf.issame(X,Y)
#uf.size(X)
