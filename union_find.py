class UnionFind:
    
    # インスタンス変数の初期化
    # インスタンス変数へアクセスするときは "self.インスタンス変数"
    def __init__(self, n):
        self.par = [-1]*n # 要素の根（親）
        self.rank = [0]*n # 要素が属している木の高さ
        self.siz = [1]*n # 要素が属している木の大きさ（要素数）

    # xのroot(Find)
    def root(self, x):
        if self.par[x] == -1:
            return x
        else:
            # 経路圧縮（xの親: par[x]を根に設定する）
            self.par[x] = self.root(self.par[x])
            return self.par[x]
    
    # xとyをmerge(Union)
    def merge(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry: return False
        
        # union by rank（rankが大きい方:rxに小さい方:ryをmerge）
        if self.rank[rx] < self.rank[ry]:
            rx,ry = ry,rx # rx: 親, ry: 子
        self.par[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
            
        # 集合サイズを更新
        self.siz[rx] += self.siz[ry]
        
        return True
            
    # xとyが同一のgroupかどうか
    def issame(self, x, y):
        return self.root(x) == self.root(y)
    
    # xが含まれる木のサイズ
    def size(self, x):
        return self.siz[self.root(x)]

#---------------------------------------------------
#N,Q = map(int,input().split())
#uf = UnionFind(N)

#for _ in range(Q):
#    c,x,y = map(int,input().split())
#    if c == 0: 
#        uf.merge(x,y)
#    else:
#        if uf.issame(x,y): 
#            print(1)
#        else: 
#            print(0)

