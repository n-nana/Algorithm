#BFS(1D)関数
#PAST03_M - 行商計画問題

from collections import deque

INF = float("inf")
def bfs(start, edge): #始点,edge
    _N = len(edge)
    dist = [INF]*_N
    dist[start] = 0
    deq = deque()
    deq.append(start)
    while len(deq) > 0:
        crr = deq.popleft()
        for nxt in edge[crr]:
            if dist[nxt] == INF:
                dist[nxt] = dist[crr] + 1
                deq.append(nxt)
    return dist

#--------------------------------------------------
N,M = map(int,input().split())

E = [[] for _ in range(N)]
for _ in range(M):
    u,v = map(int,input().split())
    E[u-1].append(v-1)
    E[v-1].append(u-1)

s = int(input())
s -= 1

K = int(input())
T = list(map(int,input().split()))
for i in range(K):
    T[i] -= 1
    
D = []
for t in T:
    d = bfs(t,E)
    D.append(d)
    
dp = [[INF]*K for _ in range(1<<K)]
for v in range(K):
    dp[1<<v][v] = D[v][s]

for st in range(1<<K):
    for u in range(K):
        for v in range(K):
            if u == v:
                continue
            if st&(1<<v) > 0:
                continue
            town_u,town_v = T[u],T[v] #idxの変換
            cost = D[u][town_v]
            dp[st|(1<<v)][v] = min(dp[st|(1<<v)][v], dp[st][u] + cost)

ans = INF
for v in range(K):
    ans = min(ans, dp[(1<<K) - 1][v])
    
print(ans)
#print(*dp,sep="\n")
#print(*D,sep="\n")
