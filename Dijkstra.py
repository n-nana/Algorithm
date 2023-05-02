#PAST10K - 旅行計画
#dijkstra関数

import heapq

def dijkstra(s, _E, _N): #始点, 隣接リスト, 頂点数
    
    done = [False]*_N
    dist = [-1]*_N
    
    hq = []
    heapq.heapify(hq)
    
    heapq.heappush(hq, (0, s))
    dist[s] = 0
    
    while hq:
        d,crr = heapq.heappop(hq)
        if done[crr]:
            continue
        done[crr] = True
        for (nxt,cost) in _E[crr]:
            if dist[nxt] == -1 or dist[nxt] > dist[crr] + cost:
                dist[nxt] = dist[crr] + cost
                heapq.heappush(hq, (dist[nxt], nxt))
    
    return dist
    
#---------------------

N,M = map(int,input().split())

E1 = [[] for _ in range(N)]
E2 = [[] for _ in range(N)]
for _ in range(M):
    u,v,w = map(int,input().split())
    E1[u-1].append((v-1,w))
    E2[v-1].append((u-1,w))

dist1 = dijkstra(0, E1, N)
dist2 = dijkstra(N-1, E2, N)
for i in range(N):
    if dist1[i] == -1 or dist2[i] == -1:
        print(-1)
    else:
        print(dist1[i] + dist2[i])
