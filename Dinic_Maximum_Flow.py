# 最大流問題、最小カット、2部マッチング、
# Dinic法　計算量: V*V*E

#------------------------------------
from collections import deque

class MaximumFlow():
    def __init__(self, adjacency_list):
        self.n = len(adjacency_list)
        self.E = adjacency_list

    def bfs(self, s):
        dist = [-1]*self.n
        dist[s] = 0
        deq = deque()
        deq.append(s)
        while len(deq) > 0:
            crr = deq.popleft()
            for nxt, cap, rev in self.E[crr]:
                if cap > 0 and dist[nxt] == -1:
                    dist[nxt] = dist[crr] + 1
                    deq.append(nxt)
        return dist
            
    def dfs(self, v, t, f, removed, D):
        if v == t:
            return f
        
        while removed[v] < len(self.E[v]):
            nxt, cap, rev = self.E[v][removed[v]]
            if cap > 0 and D[v] < D[nxt]:
                flow = self.dfs(nxt, t, min(f, cap), removed, D)
                if flow > 0:
                    self.E[v][removed[v]][1] -= flow
                    self.E[nxt][rev][1] += flow
                    return flow
            removed[v] += 1
        return 0
    
    def calc(self, s, t):
        flow = 0
        INF = float("inf")
        while True:
            D = self.bfs(s)
            if D[t] == -1:
                return flow
            
            removed = [0]*self.n
            while True:
                f = self.dfs(s, t, INF, removed, D)
                if f == 0:
                    break
                flow += f
    
#------------------------------------
#鉄則_B69 - Black Company 2
#https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ep
#2部マッチング
#------------------------------------

N,M = map(int,input().split())
C = []
for _ in range(N):
    c = input()
    C.append(c)

mx = N + 24 + 2 #社員 + 時間帯 + 始点と終点
E = [[] for _ in range(N + 24 + 2)]
s,t = mx-2, mx-1 #始点, 終点

# 始点ー社員間のedge
for i in range(N):
    idx_v = len(E[i])
    idx_u = len(E[s])
    E[s].append([i,10,idx_v]) #最大流量（10時間）
    E[i].append([s,0,idx_u])

# 社員ー時間帯間のedge
for i in range(N):
    for j in range(24):
        if C[i][j] == "0":
            continue
        u = i
        v = j + N
        idx_v = len(E[v])
        idx_u = len(E[u])
        E[u].append([v,1,idx_v])
        E[v].append([u,0,idx_u])

# 時間帯ー終点間のedge
for j in range(N, N+24):
    idx_v = len(E[t])
    idx_u = len(E[j])
    E[j].append([t,M,idx_v]) #最大流量（M人、これ以上は流量不要）
    E[t].append([j,0,idx_u])
    
        
mf = MaximumFlow(E)
res = mf.calc(s, t)

if res == M*24: #各時間帯にM人配置できるかどうか
    print("Yes")
else:
    print("No")
