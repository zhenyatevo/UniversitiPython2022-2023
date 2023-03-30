m=list(map(int,input().split(" ")))

for i in range(0,len(m)-1):
    buf=1000
    for j in range(0,len(m)-1):
        if m[j+1]< m[j]:
            buf = m[j]
            m[j]=m[j+1]
            m[j+1]=buf
    print(*m)
