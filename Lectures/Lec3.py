# Функция - это фрагмент программы, испрльзуемый многократно
# Пример написания функции:
"""
def sum_str(*args):   #обьявляем функцию
    res = ''
    for i in args:
        res += i
    return res

print(sum_str('q', 'e', 'l'))               #передаем аргументы в функцию 
print(sum_str('q', 'e', 'l', 'r', 'f'))     #передаем аргументы в функцию
"""

# функция Фибоначчи:
"""
def fib(n):
    if n in [1, 2]:
        return 1
    return fib(n - 1) + fib(n - 2)

list_1 = []
for i in range(1, 10):
    list_1.append(fib(i))
print(list_1)
"""
#-----------------------------------------------------------------------------
#                       Алгоритмы сортировок
#   Быстрая сортировка
"""
def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)

print(quick_sort([4, 2, 56, 7, 19, 75, 77]))
"""

#   Сортировка слиянием
"""
def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

list1 = [1, 4, 6, 2, 6, 3, 6, 2, 4, 75, 3, 54, 33, 23]
merge_sort(list1)
print(list1)
"""