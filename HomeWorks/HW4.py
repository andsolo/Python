# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, 
# которые встречаются в обоих наборах.
# На вход подается 2 числа через пробел: n m
# n - кол-во элементов первого множества.
# m - кол-во элементов второго множества.

"""
var1 = '5 5' 
var2 = '10 20 30 40 50' 
var3 = '10 20 30 40 50' 

a = set(var2.split())
b = set(var3.split())
c = a.intersection(b)
# c.discard(' ')
SortedValues = sorted(c)
for i in SortedValues:
    print(i, end = ' ')
"""

#-----------------------------------------------------------------------------
# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai
#  ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.

"""
arr = [5, 8, 6, 4, 9, 2, 7, 3]
arr_count = []

for i in range(len(arr) - 1):
    arr_count.append(arr[i - 1] + arr[i] + arr[i + 1])
arr_count.append(arr[0] + arr[-1] + arr[-2])

print(max(arr_count))
"""