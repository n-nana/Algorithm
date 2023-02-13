# DPL_3_B_Largest Rectangle
# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_3_B&lang=ja
# 正方形ver.もあるっぽい -> https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_3_A&lang=ja

H,W = map(int,input().split())
C = []
for _ in range(H):
    c = list(map(int,input().split()))
    C.append(c)

res = 0
dp = [0]*(W+1)
for i in range(H):
    for j in range(W):
        if C[i][j] == 1:
            dp[j] = 0
        else:
            dp[j] += 1
            
    P = []
    for right in range(W+1):
        left = right
        while (len(P)>0) and (P[-1][1] >= dp[right]):
            left,H = P.pop()
            res = max((right-left)*H, res)
        P.append([left,dp[right]])

print(res)
