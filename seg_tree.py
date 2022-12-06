#ABC185F - Range Xor Query

#以下、参考にさせていただいた、
#https://qiita.com/takayg1/items/c811bd07c21923d7ec69

#import sys
#sys.setrecursionlimit(10**7) #2*N-2程度でokか


def segfunc(x, y): #操作 <問題にあわせる>
    return x^y

ide_ele = 0 #単位元 <問題にあわせる>

class SegTree:
    def __init__(self, init_val, segfunc, ide_ele):
        """
        init_val: 配列の初期値
        n: 要素数
        num: n以上の最小の2のべき乗
        """
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        
        self.num = 1
        while self.num < n:
            self.num *= 2
            
        self.dat = [ide_ele]*(2*self.num - 1)
        for i in range(n): # Leaf initialize
            self.dat[self.num + i - 1] = init_val[i]
        for i in range(self.num - 2, -1, -1): # Node initialize
            self.dat[i] = self.segfunc(self.dat[2*i + 1], self.dat[2*i + 2])

    def update(self, k, a): #k番目(0-index)の値をaに更新
        k += (self.num - 1)
        self.dat[k] ^= a #　<問題にあわせる>
        while k > 0:
            k = (k-1)//2
            self.dat[k] = self.segfunc(self.dat[2*k + 1], self.dat[2*k + 2])

    def query(self, a, b, k, l, r):
        if b <= l or r <= a:
            return self.ide_ele
        if a <= l and r <= b:
            return self.dat[k]
        else:
            vl = self.query(a, b, 2*k + 1, l, (l+r)//2)
            vr = self.query(a, b, 2*k + 2, (l+r)//2, r)
            return self.segfunc(vl, vr)
        
#---------------------
N,Q = map(int,input().split())
A = list(map(int,input().split()))
#A = [ide_ele]*N # 初期配列用 <問題にあわせる>

st = SegTree(A, segfunc, ide_ele)
for _ in range(Q):
    t,x,y = map(int,input().split())
    if t == 1:
        st.update(x-1, y) #0-indexで入力される場合はx,y
#        print(st.dat)
    else:
        res = st.query(x-1, y, 0, 0, st.num) #0-indexで入力される場合はx,y+1
        print(res)
