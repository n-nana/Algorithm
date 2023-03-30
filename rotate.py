T000 = [["a","b","c"],["d","e","f"],["g","h","i"]]
T000 = [["a","b","c"],["d","e","f"]]

#右回り90度
T090 = T000[::-1]
T090 = list(map(list,(zip(*T090))))

#右回り180度
T180 = T000[::-1]
for i in range(len(T180)):
    T180[i] = T180[i][::-1]

#右回り270度
T270 = list(map(list,(zip(*T000))))
T270 = T270[::-1]

print(*T000,sep="\n")
print()
print(*T090,sep="\n")
print()
print(*T180,sep="\n")
print()
print(*T270,sep="\n")
print()
