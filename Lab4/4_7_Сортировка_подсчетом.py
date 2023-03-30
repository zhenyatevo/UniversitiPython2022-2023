m=list(map(int,input().split(" ")))

d={}
for i in range(0,len(m)):
    if m[i] in d:
        d[m[i]]+=1
    else: d[m[i]]=1

for key in sorted(d):
    for i in range(0,d[key]):
        print(key, end =" ")
