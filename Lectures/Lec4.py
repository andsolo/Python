# В списке хранятся числа. Нужно выбрать только четные и вывести само число и его квадрат
# Например (2, 4)
                            # Функция Lambda
'''
list_1 = [1, 2, 3, 5, 8, 15, 23, 38]

def select(f, col):
    return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]

list_1 = [1, 2, 3, 5, 8, 15, 23, 38]
res = select(int, list_1)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)
res = list(select(lambda x: (x, x**2), res))
print(res)
'''
#-----------------------------------------------------------------------------
                            # MAP
"""
list_1 = [x for x in range(1, 20)]
print(list_1)
list_1 = list(map(lambda x: x + 10, list_1))
print(list_1)
"""

# С клавиатуры вводится некий набор чисел, в качестве разделителя используется пробел.
# Этот набор чисел будет считан в качестве строки. как превратить list строк в list чисел?
'''
data = '12 456 234 457 23 76 3 5657'

# print(data)
# data = data.split()
# print(data)

data = list(map(int, data.split()))
print(data)
'''
#-----------------------------------------------------------------------------
                            # FILTER
'''
data = [15, 65, 9, 36, 175]
res = list(filter(lambda x : x % 10 == 5, data))
print(res)
'''

#-----------------------------------------------------------------------------
                            # Первая задача, только с новыми функциями 
'''
list_1 = [1, 2, 3, 5, 8, 15, 23, 38]
res = map(int, list_1)
print(res)
res = filter(lambda x: x % 2 == 0, res)
print(res)
res = list(map(lambda x: (x, x**2), res))
print(res)
'''
