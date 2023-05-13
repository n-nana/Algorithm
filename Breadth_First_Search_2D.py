#BFS(2D)関数
#ABC301E - Pac-Takahashi

from collections import deque

INF = float("inf")
def bfs(y,x,G,ng): #始点の座標(y,x),grid,壁
    _H, _W = len(G), len(G[0])
    dist = [[INF]*_W for _ in range(_H)]
    dist[y][x] = 0
    deq = deque()
    deq.append([y,x])
    while len(deq) > 0:
        cy,cx = deq.popleft()
        for i in range(4):
            ny,nx = cy+dy[i],cx+dx[i]
            if not (0 <= ny < _H and 0 <= nx < _W):
                continue
            if A[ny][nx] == ng:
                continue
            if dist[ny][nx] == INF:
                dist[ny][nx] = dist[cy][cx] + 1
                deq.append([ny,nx])
    return dist

#--------------------------------------------------
def count_bit(n):
    _c = 0
    while n > 0:
        if n%2 == 1:
            _c += 1
        n //= 2
    return _c

#--------------------------------------------------
H,W,T = map(int,input().split())

dy = (0,-1,1,0)
dx = (-1,0,0,1)

A = [] #grid
P = [] #お菓子のある座標
K = 0
for i in range(H):
    a = list(input())
    for j in range(W):
        if a[j] == "S": 
            sy,sx = i,j
        elif a[j] == "G": 
            gy,gx = i,j
        elif a[j] == "o":
            P.append([i,j])
            K += 1
    A.append(a)

D = [] #お菓子pのある座標からの最短距離
for py,px in P:
    d = bfs(py,px,A,"#")
    D.append(d)
    
dp = [[INF]*K for _ in range(1<<K)] #最小移動回数
for v in range(K):
    dp[1<<v][v] = D[v][sy][sx]

for st in range(1, 1<<K):
    for u in range(K):
        for v in range(K):
            if u == v:
                continue
            if st&(1<<v) > 0:
                continue
            vy,vx = P[v]
            cost = D[u][vy][vx]
            dp[st|1<<v][v] = min(dp[st][u] + cost, dp[st|1<<v][v])

D_0 = bfs(sy,sx,A,"#")
if D_0[gy][gx] <= T:
    ans = 0
else:
    ans = -1

for st in range(1<<K):
    okashi = count_bit(st)
    for u in range(K):
        move = dp[st][u] + D[u][gy][gx]
        if move <= T:
            ans = max(ans, okashi)
        
print(ans)
