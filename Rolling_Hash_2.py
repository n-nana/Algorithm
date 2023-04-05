class Rolling_Hash():
    def __init__(self, string, base_1, mod_1, base_2, mod_2):
        n = len(string)
        self.base = [base_1, base_2]
        self.mod = [mod_1, mod_2]
        self.power = [[1]*(n+1) for _ in range(2)]
        self.h = [[0]*(n+1) for _ in range(2)]
    
        for i in range(1, n+1):
            self.power[0][i] = self.power[0][i-1]*self.base[0]%self.mod[0]
            self.power[1][i] = self.power[1][i-1]*self.base[1]%self.mod[1]
        for i in range(1, n+1):
            word = ord(string[i-1]) - ord("a")
            self.h[0][i] = (self.h[0][i-1]*self.base[0] + word)%self.mod[0]
            self.h[1][i] = (self.h[1][i-1]*self.base[1] + word)%self.mod[1]
    
    def get_hash(self, l, r):
        h_1 = (self.h[0][r] - self.h[0][l]*self.power[0][r-l])%self.mod[0]
        h_2 = (self.h[1][r] - self.h[1][l]*self.power[1][r-l])%self.mod[1]
        hash_value = [h_1, h_2]
        return hash_value

#-----------------------------------------------------
B_1,B_2 = 26,27
MOD_1, MOD_2 = 10**9+33, 2**31-1

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

ht = Rolling_Hash(T, B_1, MOD_1, B_2, MOD_2)
hp = Rolling_Hash(P, B_1, MOD_1, B_2, MOD_2)

m = len(P)
p_val = hp.get_hash(0,m)
for idx in range(len(T) - len(P) + 1):
    t_val = ht.get_hash(idx,idx+m)
    if t_val == p_val:
        print(idx)
