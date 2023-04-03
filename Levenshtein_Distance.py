#編集距離（Levenshtein_Distance）
#https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_E&lang=ja

INF = float("inf")

S1 = str(input())
S2 = str(input())
N,M = len(S1),len(S2)

dp = [[INF]*(M+3) for _ in range(N+3)]
for i in range(N+1):
    dp[i][0] = i #S1のi文字目を削除した場合の編集距離
for j in range(M+1):
    dp[0][j] = j #S2のj文字目を削除した場合の編集距離

for i in range(N):
    for j in range(M):
        if S1[i] == S2[j]: #S1のi番目の文字とS2のj番目の文字が一致する場合
            dp[i+1][j+1] = min(dp[i][j], dp[i][j+1]+1, dp[i+1][j]+1, dp[i+1][j+1])
        else: #S1のi番目の文字とS2のj番目の文字が一致しない場合
            dp[i+1][j+1] = min(dp[i][j]+1, dp[i][j+1]+1, dp[i+1][j]+1, dp[i+1][j+1])
            
print(dp[N][M])
        
    
