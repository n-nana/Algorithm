import math

class LowestCommonAncestor:
    def __init__(self, n):
        self._n = n
        self._logn = int(math.log2(self._n) + 2)
        self._depth = [0]*self._n
        self._distance = [0]*self._n
        self._ancestor = [[-1]*self._n for _ in range(self._logn)]
        self._edges = [[] for _ in range(self._n)]

    # u-v間(0-index)に重みwの辺を追加
    def add_edges(self, u, v, w = 1):
        self._edges[u].append((v, w))
        self._edges[v].append((u, w))

    # 根をrootにした木に対して計算
    def build(self, root = 0):
        stack = [root]
        while stack:
            cur = stack.pop()
            for nxt, w in self._edges[cur]:
                if self._ancestor[0][nxt] != cur and self._ancestor[0][cur] != nxt:
                    self._ancestor[0][nxt] = cur
                    self._depth[nxt] = self._depth[cur] + 1
                    self._distance[nxt] = self._distance[cur] + w
                    stack.append(nxt)

        for k in range(1, self._logn):
            for i in range(self._n):
                if self._ancestor[k - 1][i] == -1:
                    self._ancestor[k][i] = -1
                else:
                    self._ancestor[k][i] = self._ancestor[k - 1][self._ancestor[k - 1][i]]
                
    # uとv(0-index)のLCA
    def lca(self, u, v):
        if self._depth[u] > self._depth[v]:
            u, v = v, u

        for k in range(self._logn - 1, -1, -1):
            if ((self._depth[v] - self._depth[u])>>k)&1:
                v = self._ancestor[k][v]
        
        if u == v: return u

        for k in range(self._logn - 1, -1, -1):
            if self._ancestor[k][u] != self._ancestor[k][v]:
                u = self._ancestor[k][u]
                v = self._ancestor[k][v]
        
        return self._ancestor[0][u]
    
    # uとv(0-index)の距離
    def distance(self, u, v):
        return self._distance[u] + self._distance[v] - 2 * self._distance[self.lca(u, v)]
    
#-------------------------------------------
#PAST_D最小共通祖先
#https://atcoder.jp/contests/pastbook2022/tasks/pastbook2022_d

N = int(input())
tr = LowestCommonAncestor(N) #N頂点のtree

for _ in range(N-1):
    a,b = map(int,input().split())
    tr.add_edges(a-1,b-1,1) #辺を追加

tr.build() #LCA計算
    
Q = int(input())
for _ in range(Q):
    u,v = map(int,input().split())
    print(tr.lca(u-1,v-1) + 1) # 各queryに対し、LCAを求める
    
