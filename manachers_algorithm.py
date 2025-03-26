def manachers_algorithm(s):
    # 文字列の前処理
    transformed = '#' + '#'.join(s) + '#'
    n = len(transformed)
    P = [0] * n
    C = R = 0

    for i in range(1, n-1):
        mirror = 2*C - i
        if i < R:
            P[i] = min(R - i, P[mirror])

        # 中心拡張
        while (i + P[i] + 1 < n and 
               i - P[i] - 1 >= 0 and
               transformed[i+P[i]+1] == transformed[i-P[i]-1]):
            P[i] += 1

        # 右端の更新
        if i + P[i] > R:
            C, R = i, i + P[i]
    max_len, center_idx = max((val, idx) for idx, val in enumerate(P))
    start = (center_idx - max_len) // 2
    return s[start:start + max_len]

#-------------------------------------------------
S = "testtt"
res = manachers_algorithm(S)
print(res)

#-------------------------------------------------
#https://atcoder.jp/contests/abc398/tasks/abc398_f
