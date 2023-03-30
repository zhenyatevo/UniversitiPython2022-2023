m=list(map(int,input().split(" ")))

for i in range(1, len(m)):
    temp = m[i]
    j = i - 1
    while (j >= 0 and temp < m[j]):
        m[j + 1] = m[j]
        j = j - 1
    m[j + 1] = temp
    print(*m)
