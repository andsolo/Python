# Задача 17. Дан список чисел. Определите, сколько в нем встречается различных чисел.
"""
list1 = [1, 1, 2, 0, -1, 3, 4, 4]

# print(set(list1))     # - перевод списка в множество 
print(len(set(list1)))
"""
#-----------------------------------------------------------------------
# Задача 19. Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) 
# на K элементов вправо, K – положительное число.
# Input: [1, 2, 3, 4, 5] 
# k = 3 
# Output: [4, 5, 1, 2, 3]
"""
list1 = [1, 2, 3, 4, 5] 
k = 3
i = 0

while i < k:
    list1.append(list1[0])
    list1.pop(0)
    i += 1

print(list1)
"""
#-----------------------------------------------------------------------
# Задача 19. Напишите программу для печати всех уникальных значений в словаре.
"""
list1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
res_set = set()

for dict in list1:
    for key in dict:
        res_set.add(dict[key].strip())

print(res_set)
"""
#-----------------------------------------------------------------------
# Задача 23. Дан массив, состоящий из целых чисел. Напишите программу,
# которая подсчитает количество элементов массива, 
# больших предыдущего (элемента с предыдущим номером)
"""
list1 = [0, -1, 5, 2, 3]

res = 0

for i in range(0, len(list1)):
    if list1[i - 1] < list1[i]:
        res += 1

print(res)
"""