class Rolling_Hash():
    def __init__(self, string, base, mod):
        n = len(string)
        self.base = base
        self.mod = mod
        self.power = [1]*(n+1)
        self.h = [0]*(n+1)
    
        for i in range(1, n+1):
            self.power[i] = self.power[i-1]*self.base%self.mod
        for i in range(1, n+1):
            word = ord(string[i-1]) - ord("a")
            self.h[i] = (self.h[i-1]*self.base + word)%self.mod
    
    def get_hash(self, l, r):
        hash_value = (self.h[r] - self.h[l]*self.power[r-l])%self.mod
        return hash_value

#-----------------------------------------------------
B = 26
MOD = 10**9+33

#-----------------------------------------------------
# 参考01: 
# https://note.com/omotiti/n/nf173d0d9f218

# 参考02: modの乱数化や2次元への拡張など
# https://tjkendev.github.io/procon-library/python/string/rolling_hash.html

#-----------------------------------------------------
# 問題01: ALDS1_14_B_String Search（一致する文字列のidxを出力する問題）
# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_14_B&lang=ja

T = input()
P = input()

ht = Rolling_Hash(T, B, MOD)
hp = Rolling_Hash(P, B, MOD)

m = len(P)
p_val = hp.get_hash(0,m)
for idx in range(len(T) - len(P) + 1):
    t_val = ht.get_hash(idx,idx+m)
    if t_val == p_val:
        print(idx)
