from itertools import *
message = str(input())
d = int(input())
def HammingDistance(text1,text2):
    spisok = list(zip(text1,text2))
    count = 0 
    for i in spisok: 
        if i[0] != i[1]:
            count+=1    
    return count

def Neighbours(Pattern, d):
    # Базис №1
    if d == 0: 
        return Pattern

    # Базис №2
    if len(Pattern) == 1:
        return " ".join("ACGT")
    Neighborhood = set()
    
    # Рекурсивно находим d-соседей суффикса Pattern
    SuffixNeighbors = []
    for i in product("ACGT",repeat=len(Pattern[1:])):
        if HammingDistance(i,Pattern[1:]) <= d :
            r = "".join(i)
            SuffixNeighbors.append(r)
    
    # Цикл по всем найденным соседям - шаг 2 алгоритма (рекурсивная часть)
    for i in SuffixNeighbors:
        if HammingDistance(i,Pattern[1:]) < d:
            for x in "ACGT":
                Neighborhood.add(x+i)
        else:
            Neighborhood.add(Pattern[0:1]+i)
    return Neighborhood

array = Neighbours(message, d)
if d > 0 :
    for i in sorted(Neighbours(message, d)):
        print(i)
else:
    print(array)
