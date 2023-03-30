def partition(A, left, right):
    i = left + 1
    j = right
    if len(A) <= 1 :       
        return 
   
    while i <= j :
        while A[i] < A[left] and i < right :
            i += 1
        while A[j] > A[left] and j > left :
            j -= 1
        if i >= j :
            break
        c = A[i]
        A[i] = A[j]
        A[j] = c
        i += 1
        j -= 1
    c = A[left]
    A[left] = A[j]
    A[j] = c
    print(*A)
    return j

def quickSort(A, left = 0, right = None, verbose = False):
    # если параметр right == None, то это первый вызов и надо исправить его на реальное значение
    if right == None :
        right = len(A)-1
    
    # если массив пустой или состоит всего из одного элемента, заканчиваем
    if left >= right :
        return 
   
    # производим разбиение с помощью partition
    p = partition(A,left,right)

    # рекурсивно сортируем обе части
    quickSort(A, left, p-1 )
    quickSort(A, p+1, right )


# читаем список A (и возможно слово 'verbose' на второй строке)
A = list(map(int,input().split()))
# вызываем quickSort
quickSort(A)

"""
Прочитать слово verbose "обычным" способом не получится, т.к. в 80% тестов второй строки нет и ваша программа сломается при попытке ее чтения. Прочитать то, чего может и не быть, можно с помощью обработки исключений. Изучите и используйте код, приведенный ниже:

try:
    verbose = input()
    if verbose == 'verbose':
        verbose = True
except EOFError:
    verbose = False

"""
