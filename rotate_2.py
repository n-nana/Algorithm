A = [[1, 2, 3], [4, 5, 6]]

print(*A,sep="\n")
print()
for k in range(4):
    A = [list(a)[::-1] for a in zip(*A)]
    print(k)
    print(*A,sep="\n")
    print()
    
