m=list(map(int,input().split(" ")))

for i in range(0,len(m)-1):
    mi=m[i]
    num=i
    for j in range (i+1,len(m)):
        if mi > m[j]:
            mi=m[j]
            num=j
    #print(mi)
    m[num]=m[i]
    m[i]=mi
    print(*m)
