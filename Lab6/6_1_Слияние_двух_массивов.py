def merge(A, left, mid, right):
    AUX = []
    Index = []
    i = left
    j = mid+1
    
    while i <= mid and j<= right:      
        if A[i] <= A[j]:
            AUX.append(A[i])
            Index.append(i)
            i +=1            
        else:
            AUX.append(A[j])
            Index.append(j)
            j+=1
            
    if i <= mid :       
        AUX.extend(A[i:mid+1])
        Index+=(list(range(i,mid+1)) )
        
    if j <= right:
        AUX.extend(A[j:right+1])     
        Index +=(list(range(j, right+1)))
    A[left:right+1] = AUX     
    print(" ".join(map(str,A)))

    return Index


mas1 = list(map(int,input().split()))
mas2 = list(map(int,input().split()))
A = mas1 + mas2
left = 0
mid = len(mas1)-1
right = len(A)-1


print ( " ".join(map(str, merge(A, left, mid, right) ) ) )
