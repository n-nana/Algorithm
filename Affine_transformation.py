#ABC189E - Rotate and Flip
#アフィン変換

#https://atcoder.jp/contests/abc189/editorial/539
#https://ikatakos.com/pot/programming_algorithm/contest_history/atcoder/2021/0123_abc189
#https://craft-gogo.com/python-opencv-rotation/

#------------------------------------------
def dot1(a,b):
    Q = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                Q[i][j] += a[i][k]*b[k][j]
    return Q

#------------------------------------------
def dot2(a,b):
    Q = [0,0,0]
    for i in range(3):
        for k in range(3):
            Q[i] += a[i][k]*b[k]
    return Q[0],Q[1]

#------------------------------------------
N = int(input())
C = []
for _ in range(N):
    x,y = map(int,input().split())
    C.append((x,y,1))
    
A = [[1,0,0],[0,1,0],[0,0,1]] #Affine
P = []
P.append(A)

M = int(input())
for _ in range(M):
    op = list(map(int,input().split()))
    if op[0] == 1: #clockwise
        B = [(0,1,0),(-1,0,0),(0,0,1)]   
    elif op[0] == 2: #counterclockwise
        B = [(0,-1,0),(1,0,0),(0,0,1)]
    elif op[0] == 3: #invert with x=op[1]
        B = [(-1,0,2*op[1]),(0,1,0),(0,0,1)]
    elif op[0] == 4: #invert with y=op[1]
        B = [(1,0,0),(0,-1,2*op[1]),(0,0,1)]
    A = dot1(B,A) #行列: 掛ける順番
    P.append(A)
        
Q = int(input())
for _ in range(Q):
    a,b = map(int,input().split())
    X,Y = dot2(P[a],C[b-1])
    print(X,Y)
