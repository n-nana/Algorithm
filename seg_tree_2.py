#ABC185F - Range Xor Query
#蟻本ver.ベース（SegTreeクラスにした）
#再帰処理をなくして動作をはやくした

def segfunc(x, y): #操作 <問題にあわせる>
    return x^y

ide_ele = 0 #単位元 <問題にあわせる>
#ide_ele = (1<<31) - 1

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
#        self.dat[k] += a
#        self.dat[k] = a
        while k > 0:
            k = (k-1)//2
            self.dat[k] = self.segfunc(self.dat[2*k + 1], self.dat[2*k + 2])

    def query(self, L, R):
        tmp = self.ide_ele
        L += self.num - 1
        R += self.num - 1
        while L < R:
            if L&1 == 0: #上の階層にdat[L]が含まれないのでここで計算
                tmp = self.segfunc(self.dat[L], tmp)
            if R&1 == 0: #上の階層にdat[R-1]が含まれないのでここで計算
                tmp = self.segfunc(self.dat[R-1], tmp)
            R -= 1 #右区間を更新前に調整
            L //= 2 #左区間を上の階層へ（L%2==0のときは右側にshiftする
            R //= 2 #右区間を上の階層へ
        return tmp
        
#---------------------
N,Q = map(int,input().split())
A = list(map(int,input().split()))
#A = [ide_ele]*N # 初期配列用 <問題にあわせる>

st = SegTree(A, segfunc, ide_ele)
for _ in range(Q):
    t,x,y = map(int,input().split())
    if t == 1:
        st.update(x-1, y) #0-indexで入力される場合はx,y
#        print(st.dat) #更新後の木を確認
    else:
        res = st.query(x-1, y) #0-indexで入力される場合はx,y+1
        print(res)
