# Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.
# Найдите количество и выведите его.
"""
list_1 = [1, 2, 3, 4, 5]
k = 3
res = 0

for i in range(0, len(list_1)):
    if list_1[i] == k:
        res += 1

print(res)
"""
# ------------------------------------------------------------------------
# Требуется найти в массиве list_1 самый близкий по значению элемент к заданному числу k и вывести его.
# Считать, что такой элемент может быть только один. Если значение k совпадает с этим элементом - выведите его.
"""
list_1 = [1, 2, 3, 4, 5]
k = -6
minDif = 1000
countDif = 1000
res = 0

for i in list_1:
    countDif = k - i
    if countDif < minDif:
        res = i
        minDif = countDif

print(res)
"""

# ------------------------------------------------------------------------
# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
"""
k = 'ноутбук'
points_en = {1:'AEIOULNSTR',
      	2:'DG',
      	3:'BCMP',
      	4:'FHVWY',
      	5:'K',
      	8:'JX',
      	10:'QZ'}
points_ru = {1:'АВЕИНОРСТ',
      	2:'ДКЛМПУ',
      	3:'БГЁЬЯ',
      	4:'ЙЫ',
      	5:'ЖЗХЦЧ',
      	8:'ШЭЮ',
      	10:'ФЩЪ'}

text = k.upper()

res = 0

for i in text:
    if i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
        for j in points_en:
            if i in points_en[j]:
                res += j
    else:
        for j in points_ru:
            if i in points_ru[j]:
                res += 1
print(res)
"""