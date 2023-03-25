#GRL_GRL_3_C_Strongly Connected Components
#https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_3_C

#（参考）
#https://manabitimes.jp/math/1250
#https://tjkendev.github.io/procon-library/python/graph/scc.html
#https://hkawabata.github.io/technical-note/note/Algorithm/graph/scc.html

#-----------------------------------------------------
import sys
sys.setrecursionlimit(10**7)

def SCC(_N, _E, _RE):
    
    def dfs(_crr):
        used[_crr] = True
        for _nxt in _E[_crr]:
            if not used[_nxt]:
                dfs(_nxt)
        order.append(_crr)
        
    def r_dfs(_crr, _idx):
        group[_crr] = _idx
        r_used[_crr] = True
        for _nxt in _RE[_crr]:
            if not r_used[_nxt]:
                r_dfs(_nxt, _idx)
      
    order = []
    used = [False]*N
    r_used = [False]*_N
    group = [-1]*N
    idx = 0
    
    for i in range(_N):
        if not used[i]:
            dfs(i)
    
    order.reverse()
    for _n in order:
        if not r_used[_n]:
            r_dfs(_n, idx)
            idx += 1
            
    return idx,group
            

#-----------------------------------------------------
N,M = map(int,input().split())

E = [[] for _ in range(N)]
RE = [[] for _ in range(N)]
for _ in range(M):
    u,v = map(int,input().split())
    E[u].append(v)
    RE[v].append(u)
    
mx, G = SCC(N,E,RE)
#print(mx) #group数
#print(G) #nodeの属するgr.

Q = int(input())
for _ in range(Q):
    u,v = map(int,input().split())
    if G[u] == G[v]:
        print(1)
    else:
        print(0)
        
