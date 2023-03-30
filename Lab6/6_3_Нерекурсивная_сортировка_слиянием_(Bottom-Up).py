A = list(map(int,input().split()))
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
    #print(" ".join(map(str,A)))
    return Index

def mergeSortNonRec(A):
    # запоминаем длину массива
    n = len(A)

    # инициализируем переменную, в которой будем хранить длину сливаемых массивов
    width = 1

    # запускаем внешний цикл, который будет перебирать удваивающиеся значения width
    while width < n:
        i = 0
        # запускаем цикл, который будет сливать половины подмассивов размером 2*width
        while i < n:
            merge(A,i,min(i+width-1,n-1),min(i+2*width-1,n-1))
            # не забываем увеличивать i на нужное значение
            i += 2*width
        # не забываем увеличивать width на нужное значение
        width *= 2

        # выводим массив в нужном формате
        print (*A)

# читаем массив A
# ...
# вызываем mergeSortNonRec
mergeSortNonRec(A)
