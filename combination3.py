#ABC358E - Alphabet Tiles
#https://atcoder.jp/contests/abc358/tasks/abc358_e

def ncr(nmax, mod):
    table = [[0]*(nmax+1) for _ in range(nmax+1)]
    for n in range(nmax + 1):
        c = 1
        table[n][0] = c
        for r in range(1, n+1):
            c *= (n-r+1)
            c *= pow(r, mod-2, mod)
            c %= mod
            table[n][r] = c
    return table

#---------------------------------------------------------
MOD = 998244353

K = int(input())
C = list(map(int,input().split()))

# 事前処理テーブル
T = ncr(K, MOD)

# Main_i番目のアルファベットまでみたときの長さnの文字列の個数
dp = [[0]*(K+1) for _ in range(27)]
dp[0][0] = 1
for i in range(26):
    r = C[i] #アルファベットiを追加
    for j in range(K+1):
        for k in range(r+1):
            n = j + k
            if dp[i][j] == 0:
                continue
            if n > K:
                continue
            dp[i+1][n] += dp[i][j]*T[n][k]
            dp[i+1][n] %= MOD
        
#for i in range(27):
#    print(dp[i])

ans = 0
for j in range(1,K+1):
    ans += dp[26][j]
    ans %= MOD
    
print(ans)
