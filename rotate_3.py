def rotate(crr):
    _H,_W = len(crr),len(crr[0])
    nxt = [["."]*_H for i in range(_W)]
    for y in range(_H):
        for x in range(_W):
            nxt[x][_H-1-y] = crr[y][x]
    return nxt

A = [[1,2,3],[4,5,6]]
for _ in range(4):
    for i in range(len(A)):
        print(A[i])
    A = rotate(A)
    print()
