#ABC137E - Coins Respawn

#-----------------------------------------------------
INF = float("inf")

class BellmanFord:
    
    def __init__(self, n):
        self.num = n
        self.dist = [INF]*n
        self.negative_cycle = [False]*n
    
    # 距離算出
    def measure(self, s, g, E): #s:始点, g:終点, E:辺情報(u,v,cost)
        self.dist[s] = 0
        for loop in range(self.num - 1):
            for i in range(len(E)):
                u,v,c = E[i][0],E[i][1],E[i][2]
                if self.dist[u] == INF:
                    continue
                if self.dist[v] > self.dist[u] + c:
                    self.dist[v] = self.dist[u] + c
        
        return self.dist[g]
    
    # 閉路検出
    def detect(self, p, E): #p:負の閉路であるかどうか検出したい点, E:辺
        for loop in range(self.num):
            for i in range(len(E)):
                u,v,c = E[i][0],E[i][1],E[i][2]
                if self.dist[u] == INF:
                    continue
                if self.dist[v] > self.dist[u] + c:
                    self.dist[v] = self.dist[u] + c
                    self.negative_cycle[u] = True
                if self.negative_cycle[u]:
                    self.negative_cycle[v] = True
        
        return self.negative_cycle[p]
              
#-----------------------------------------------------
N,M,P = map(int,input().split())
 
edge = []
for _ in range(M):
    a,b,c = map(int,input().split())
    edge.append((a-1, b-1, P-c))
    
bf = BellmanFord(N)
ans = bf.measure(0, N-1, edge) #距離計算
cycle = bf.detect(N-1, edge) #閉路検出

if cycle:
    print("-1")
else:
    print(max((-1)*ans, 0))
