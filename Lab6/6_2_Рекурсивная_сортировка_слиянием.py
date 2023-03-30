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
    
    return A

def mergeSort(A, left = 0, right = None, verbose = False):
    # если параметр right == None, то это первый вызов и надо исправить его на реальное значение
    if right == None :
        right = len(A)-1

    # если массив пустой или состоит всего из одного элемента, заканчиваем
    if left >= right :
        return
    # определяем середину
    mid = (left+right) // 2
    # рекурсивно сортируем обе половины
    mergeSort(A, left, mid )
    mergeSort(A, mid+1, right )

    # печатаем массив и производим слияние с помощью функции merge
    print(*A)
    merge(A, left, mid, right)
    return " ".join(map(str,A))
    

# читаем список A (и возможно слово 'verbose' на второй строке)
A = list(map(int,input().split()))
# вызываем mergeSort и не забываем напечатать результат его работы еще раз!
print(mergeSort(A))


"""
Прочитать слово verbose "обычным" способом не получится, т.к. в 80% тестов второй строки нет и ваша программа сломается при попытке ее чтения. Прочитать то, чего может и не быть, можно с помощью обработки исключений. Изучите и используйте код, приведенный ниже:

try:
    verbose = input()
    if verbose == 'verbose':
        verbose = True
except EOFError:
    verbose = False

"""
