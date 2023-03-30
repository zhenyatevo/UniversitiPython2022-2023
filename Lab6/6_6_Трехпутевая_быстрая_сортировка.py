def quickSort3Way(A, left = 0, right = None, verbose = False):
    # если параметр right == None, то это первый вызов и надо исправить его на реальное значение
    if right == None :
        right = len(A)-1

    # если массив пустой или состоит всего из одного элемента, заканчиваем
    if left >= right :
        return

    # инициализируем всевозможные указатели
    lt = left
    gt = right
    v = A[left]
    i = left

    # производим трехпутевое разбиение за один проход в соответствии с алгоритмом
    while i <= gt :
        if A[i] < v :
            c = A[lt]
            A[lt] = A[i]
            A[i] = c
            lt += 1
            i += 1 
        elif A[i] > v :
            c = A[gt]
            A[gt] = A[i]
            A[i] = c
            gt -= 1
        elif A[i] == v :
            i += 1
            
    # печатаем массив в нужном формате
    print(*A)

    # рекурсивно сортируем обе части (кроме той, что равна опорному элементу!)
    quickSort3Way(A, left, lt - 1)
    quickSort3Way(A, gt + 1, right)


# читаем список A (и возможно слово 'verbose' на второй строке)
A = list(map(int,input().split()))
# вызываем quickSort3Way
quickSort3Way(A)

"""
Прочитать слово verbose "обычным" способом не получится, т.к. в 80% тестов второй строки нет и ваша программа сломается при попытке ее чтения. Прочитать то, чего может и не быть, можно с помощью обработки исключений. Изучите и используйте код, приведенный ниже:

try:
    verbose = input()
    if verbose == 'verbose':
        verbose = True
except EOFError:
    verbose = False

"""
