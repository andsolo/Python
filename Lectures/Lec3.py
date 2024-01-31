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