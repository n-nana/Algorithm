# 文字列検索アルゴリズム 
# Rabin-Karp法（ローリングハッシュ）

def Rabin_Karp(_str, _sub_str):
    n, m = len(_str), len(_sub_str)
    if n < m:
        return -1

    # CONSTANTS
    B_1, B_2 = 26, 27 # 基数 1, 2
    MOD_1, MOD_2 = 10**9+33, 2**31-1

    # B_1, B_2のm乗を計算
    MX_1, MX_2 = pow(B_1, m, MOD_1), pow(B_2, m, MOD_2)

    # 長さmのstringのhash pairを求める関数
    def hash_pair(string):
        h_1, h_2 = 0, 0 #hash
        f_1, f_2 = 1, 1 #factor
        for i in range(m-1, -1, -1):
            word = ord(string[i])
            h_1 += ((word - 97)*(f_1))%MOD_1
            f_1 = (f_1*B_1)%MOD_1
            h_2 += ((word - 97)*(f_2))%MOD_2
            f_2 = (f_2*B_2)%MOD_2
        return [h_1%MOD_1, h_2%MOD_2]

    # 01_sub-stringのhash pairを求める
    hash_sub_str = hash_pair(_sub_str)

    # 02_stringのhashを求める（始点: idxをスライドする）
    for idx in range(n-m+1):
        if idx == 0: # stringのhash pairの初期値
            hash_str = hash_pair(_str)
        else: # stringのhash pairを更新
            hash_str[0] = (((hash_str[0]*B_1)%MOD_1
                            - ((ord(_str[idx-1]) - 97)*(MX_1))%MOD_1 #左端の文字を削除
                            + (ord(_str[idx+m-1]) - 97))%MOD_1) #右側に文字を追加
            hash_str[1] = (((hash_str[1]*B_2)%MOD_2
                            - ((ord(_str[idx-1]) - 97)*(MX_2))%MOD_2
                            + (ord(_str[idx+m-1]) - 97))%MOD_2)

        if hash_sub_str == hash_str:
            print(idx) # _strと_sub_strが一致したら_strの開始idxを出力
#            return idx

    return -1


#----------------------------------------------------------------
# 参考01: Approach 3: Rabin-Karp algorithm (Double Hash)
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/solution/

# 参考02: Rolling Hashの概要など
# https://qiita.com/hirominn/items/80464ee381c8d400725f

# 参考03: 文字列アルゴリズム
# https://ikatakos.com/pot/programming_algorithm/string_search

#----------------------------------------------------------------
# 問題01: ALDS1_14_B_String Search（一致する文字列のidxを出力する問題）
# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_14_B&lang=ja

T = input()
P = input()

Rabin_Karp(T,P)
