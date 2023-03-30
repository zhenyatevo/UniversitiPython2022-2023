text = str(input())
k = int(input())
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
    while len(s) < k:
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

def FrequentWordsWithSorting(text, k):
    FrequentPatterns = []
    Index = []
    
    for i in range(len(text)- int(k)+1):
        part = text[i:i+k]
        Index.append(word(part))
        
    SortedIndex = sorted(Index)
    
    
    Count = [0]*len(SortedIndex)
    
    for i in range(0,len(SortedIndex)):
        if SortedIndex[i] != SortedIndex[i-1]:
            Count[i] = 1
        else :
            Count[i] = Count[i-1] + 1
             
    print(" ".join( map(str, Count) ) )    

    
    maxCount = max(Count)
    
    for i in range(len(Count)):
        if Count[i] == maxCount:
            FrequentPatterns.append(SortedIndex[i])       

    
    return FrequentPatterns

array = FrequentWordsWithSorting(text, k)
for i in array:
    print(NumberToPattern(i, k) , end = " " )
