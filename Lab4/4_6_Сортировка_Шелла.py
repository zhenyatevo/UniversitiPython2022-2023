def SortInsert(h,spisok):
    spik = []
    for i in range(h,len(spisok)):
        index = i
        while (index-h) >= 0 and spisok[index] < spisok[index-h]:
            k = spisok[index]
            spisok[index] = spisok[index-h]
            spisok[index-h] = k 
            index -= h
            
    return " ".join(map(str,spisok))    
   
    
def SortShell(h5 , spisok1):
    spik = []
    for i in h5:
        count = SortInsert(i,spisok1)
        spik.append(count)   
    
    return spik


h = list(map(int,input().split()))
spisok = list(map(int,input().split()))

for i in h:
    spik = []
    count = SortInsert(i,spisok)
    spik.append(count)
    print("".join(spik)) 
