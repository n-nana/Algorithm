#GRL_GRL_4_B_Topological_Sort
#https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_4_B

from collections import deque

def TopologicalSort(_E, _P):
    deq = deque()
    _N = len(_P)
    for i in range(_N):
        if _P[i] == 0:
            deq.append(i)
    _res = []
    while deq:
        crr = deq.popleft()
        _res.append(crr)
        for nxt in _E[crr]:
            _P[nxt] -= 1
            if _P[nxt] == 0:
                deq.append(nxt)
    return _res

#-------------------------------
N,M = map(int,input().split())

E = [[] for _ in range(N)] #行き先
P = [0]*N #親の数
for _ in range(M):
    u,v = map(int,input().split())
    E[u].append(v)
    P[v] += 1
    
ans = TopologicalSort(E, P)
for a in ans:
    print(a)
   
