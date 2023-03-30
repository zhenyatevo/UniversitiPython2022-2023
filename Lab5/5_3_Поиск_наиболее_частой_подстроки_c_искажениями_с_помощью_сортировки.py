from itertools import *

message = str(input())
k1,d1 = map(int , input().split())

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
        return {"A","C","G","T"}
    Neighborhood = set()
    
    # Рекурсивно находим d-соседей суффикса Pattern
    SuffixNeighbors = []
    
    if Pattern is not set():
        SuffixNeighbors = Neighbours(Pattern[1:],d)
        
    else:
        SuffixNeighbors = Neighbours(Neighborhood,d)
    
    # Цикл по всем найденным соседям - шаг 2 алгоритма (рекурсивная часть)
    for i in SuffixNeighbors:
        if HammingDistance(i,Pattern[1:]) < d:
            for x in {"A","C","G","T"}:
                Neighborhood.add(x+i)
        else:
            Neighborhood.add( Pattern[0:1]+i)
    return Neighborhood


def word(text):
    place = ""
    for i in range(len(text)):
        if text[i] == "A":
            place+="0"
        if text[i] == "C":
            place+="1"
        if text[i] == "G":
            place+="2"
        if text[i] == "T":
            place+="3"   
    return int(place,base=4)

def NumberToPattern(index, k): 
    place = ""
    s = ""      
    while index > 0:
        s += str(index%4)
        index //= 4
    while len(s)<k:
        s+="0"
    s =  s[::-1] 
    for i in range(len(s)):
        if s[i] == "0":
            place+="A"
        if s[i] == "1":
            place+="C"
        if s[i] == "2":
            place+="G"
        if s[i] == "3":
            place+="T"      
    return place

def FrequentWordsWithMismatches(text, k, d):
    Index = []
    FrequentPatterns = []
    NeighborhoodArrays = []
    # Цикл, который заполняет список NeighborhoodArrays всеми d-соседями всех подстрок длины k строки text
    # Попробуйте совместить шаги 1 и 2 алгоритма в одном цикле
    for i in range(len(text)-int(k)+1):      
        NeighborhoodArrays.append( Neighbours(text[i:i+int(k)], d) )
   
    for i in range(len(NeighborhoodArrays)):
       
        for j in NeighborhoodArrays[i]:        
            Index.append(word(j))
    # Цикл (или вызов функции map?), который преобразует все элементы NeighborhoodArrays в числа
    

    SortedIndex = sorted(Index)
    

    Count = [0]*len(SortedIndex)
    for i in range(0,len(SortedIndex)):
        if SortedIndex[i] != SortedIndex[i-1]:
            Count[i] = 1
        else :
            Count[i] = Count[i-1] + 1
            
    maxCount = max(Count)

    for i in range(len(Count)):
        if Count[i] == maxCount:
            FrequentPatterns.append(SortedIndex[i]) 
            
    return FrequentPatterns


array = FrequentWordsWithMismatches(message, k1, d1)
if d1 > 0 :
    for i in array:
        print(NumberToPattern(i, k1) , end = " " )
else:
    print(message)
