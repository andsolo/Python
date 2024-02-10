# Винни пух
# вывод: Парам пам-пам
'''
stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'

stroka1 = stroka.split()
# print(stroka1)
vowels = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]

count_vowels = []

for i in stroka1:
    count = len([x for x in i if x.lower() in vowels])
    count_vowels.append(count)

# print(count_vowels)
if len(stroka1) == 1:
    print('Количество фраз должно быть больше одной!')
else:
    if count_vowels.count(count_vowels[0]) == len(count_vowels):
        print('Парам пам-пам')
    else:
        print('Пам парам')
'''
#------------------------------------------------------------------
# Таблица
'''
def print_operation_table(operation, num_rows=9, num_columns=9):
    if num_rows < 2 or num_columns < 2:
        print('ОШИБКА! Размерности таблицы должны быть больше 2!')
    else:
        print(' '.join(list(map(str, range(1, num_columns + 1)))))
        for i in range(2, num_rows + 1):
            print(i, end = ' ')
            for j in range(2, num_columns + 1):
                print(operation(i, j), end=' ')
            print()

# print_operation_table(lambda x, y: x * y) 

print_operation_table(lambda x, y: x * y, 3, 2)
'''