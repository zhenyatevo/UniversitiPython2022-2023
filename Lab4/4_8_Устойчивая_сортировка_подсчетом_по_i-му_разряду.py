def counting_sort_i(i, nums):
    # преобразуем строку с числами в список
    nums_list = list(map(int, nums.split()))
    # вычисляем максимальное число в списке
    max_num = max(nums_list)
    # создаем вспомогательный массив для подсчета количества чисел
    count = [0] * 10
    # создаем вспомогательный массив для записи отсортированных чисел
    sorted_list = [0] * len(nums_list)
    # определяем коэффициент сдвига для выбранного разряда
    exp = 10 ** i
    # считаем количество чисел с одинаковым i-тым разрядом
    for num in nums_list:
        count[(num // exp) % 10] += 1
    # преобразуем массив count, чтобы он содержал позиции отсортированных чисел
    for j in range(1, 10):
        count[j] += count[j - 1]
    # сортируем числа по i-му разряду, сохраняя порядок сортировки для чисел с одинаковыми i-тыми разрядами
    for j in range(len(nums_list) - 1, -1, -1):
        num = nums_list[j]
        digit = (num // exp) % 10
        count[digit] -= 1
        sorted_list[count[digit]] = num
    # преобразуем список отсортированных чисел в строку
    sorted_str = ' '.join(map(str, sorted_list))
    return sorted_str


i = int(input())
nums = input()
print(counting_sort_i(i, nums))
