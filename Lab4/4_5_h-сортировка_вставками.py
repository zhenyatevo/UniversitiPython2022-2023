n = int(input())
s = input()
massiv = list(map(int, s.split()))
for i in range(n, len(massiv)):
    index = i
    elem = massiv[i]
    while index>= n and elem < massiv[index-n]:
        massiv[index] = massiv[index-n]
        index-= n
    massiv[index]= elem
    print(*massiv)
