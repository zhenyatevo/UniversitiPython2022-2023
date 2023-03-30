import functools
m=list(map(int,input().split(" ")))
k=len(m)-1
for i in range(0,k):
    buf=1000
    m1=m
    c=0
    for j in range(0,len(m)-1):
        if m[j+1]< m[j]:
            buf = m[j]
            m[j]=m[j+1]
            m[j+1]=buf
            c+=1
    print(*m)
    k-=1
    if c==0:
        break
