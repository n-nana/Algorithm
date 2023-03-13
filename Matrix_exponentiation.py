#ABC293E - Geometric Progression

#（参考）https://qiita.com/ophhdn/items/e6451ec5983939ecbc5b
#（参考）ABC129F - Takahashi's Basics in Education and Learning
#（参考）https://pione.hatenablog.com/entry/2021/04/04/231809
#（参考）蟻本3-4（P.180）    

#行列乗算
def mat_mul(_A, _B, _MOD): #行列A, 行列B, MOD
    _N = len(_A)
    _res = [[0]*_N for _ in range(_N)]
    
    for i in range(_N):
        for j in range(_N):
            for k in range(_N):
                _res[i][j] += _A[i][k]*_B[k][j]
                _res[i][j] %= _MOD
    return _res

#行列累乗
def mat_pow(_A, _X, _MOD): #行列A, 指数X, MOD
    _N = len(_A)
    _res = [[0]*_N for _ in range(_N)]
    
    for i in range(_N):
        _res[i][i] = 1
        
    while _X:
        if (_X&1): #odd
            _res = mat_mul(_res, _A, _MOD)
        _A = mat_mul(_A, _A, _MOD)
        _X >>= 1 #_X //= 2
        
    return _res

#---------------------------------------------------
A,X,M = map(int,input().split())

F = [[A,1],[0,1]] #漸化式を立てて、X乗する行列Fを求める
# [res,1] = [[A,1],[0,1]]**(X-1) * [A0,1]
G = mat_pow(F, X-1, M) #[[A,1],[0,1]]**(X-1)の計算

res = (G[0][0]+G[0][1])%M
print(res)

#print(*G,sep="\n")
