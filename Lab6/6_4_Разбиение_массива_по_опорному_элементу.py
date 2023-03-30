def partition(A, left, right):
    # инициализируем два указателя
    i = left + 1
    j = right

    # если разбивать нечего, то выходим
    if len(A) == 1 :
        print(*A)
        return 0
    if len(A) == 0 :
        #print(*A)
        return 

    # запускаем внешний цикл, который будет работать, пока указатели двигаются навстречу
    while i <= j :
        # перемещаем вперед указатель i (не забываем про границу массива!)
        while A[i] < A[left] and i < right :
            i += 1
        # перемещаем назад указатель j (не забываем про границу массива!)
        while A[j] > A[left] and j > left :
            j -= 1
        # делаем проверки согласно алгоритму, меняем значения местами и двигаем указатели
        if i >= j :
            break
        c = A[i]
        A[i] = A[j]
        A[j] = c
        i += 1
        j -= 1
    # после цикла i указывает на первый элемент второй группы, j - на последний элемент первой
    # ставим опорный элемент на нужное место и возвращаем его позицию
    c = A[left]
    A[left] = A[j]
    A[j] = c
    print(*A)
    return j
# читаем left, right, массив A
# ...
# вызываем partition и выводим результат
l, r = map(int,input().split())
A = list(map(int,input().split()))
print(partition(A, l, r))
