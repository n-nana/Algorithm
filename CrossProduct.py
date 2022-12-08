def CrossProduct(p, p1, p2): #外積
    return (p[0]-p2[0])*(p1[1]-p2[1]) - (p1[0]-p2[0])*(p[1]-p2[1])

P = [(0,0),(4,0),(0,4),(1,1),(2,2),(3,3)] #座標(xi,yi)
N = len(P)

#判定例
for c1 in range(N-2): #座標c1
    for c2 in range(c1+1, N-1): #座標c2
        for c3 in range(c2+1, N): #座標c3
            for k in range(N): #判定対象の座標k
                if (k == c1) or (k == c2) or (k == c3): #kがc1,c2,c3の場合は何もしない
                    continue
                # 外積の符号がすべて同じであればkはc1,c2,c3の内側にある
                cp23 = CrossProduct(P[k], P[c2], P[c3]) #k,c2,c3の外積
                cp31 = CrossProduct(P[k], P[c3], P[c1]) #k,c3,c1の外積
                cp12 = CrossProduct(P[k], P[c1], P[c2]) #k,c1,c2の外積
                
                is_inside = False #初期値
                # 線分上の点を含める場合は等号で、含まない場合は不等号で判定
                if cp23 >= 0 and cp31 >= 0 and cp12 >= 0:
                  is_inside = True
                elif cp23 <= 0 and cp31 <= 0 and cp12 <= 0:
                  is_inside = True
                
                if is_inside:
                  print(P[k]," is inside of", P[c1], "and", P[c2], "and", P[c3])
                else: 
                  print(P[k]," is outside of", P[c1], "and", P[c2], "and", P[c3])
