"""
Интерполяция:
print (a, ' - ', b, ' - ', c) - вывод переменных через дефис 
или
print(f"{a} - {b} - {c}") 
или
print("{} - {} - {}".format(a, b, c))

Присвоение значений 
a = input()
a = input('Введите число')

Приведение типов данных 
round(1,548646, 2) -> 1,54 - округление. Используется например вот так:
print(round(a*b, 2))

Ветвление if, elif, else
username = input('Введите имя: ')
if username == 'Маша':
	print('Ура, это же Маша!')
elif username == 'Марина':
	print('Ура, это же Марина!')
elif username == 'Андрей':
	print('Ура, это же Андрей!')
else:
	print('Привет, ', username)


цикл while
i = 0
while i < 5:
	i = i + 1
    #if i == 3:
	#	break  # если использовать break то цикл else не будет выполняться
else:
	print('пожалуй хватит')
print(i)

цикл for, функция range 
r = range(0, 10, 2)==(начало, конец(не включительно), шаг) -> 0, 2, 4, 6, 8 
цикл:
for i in r:
	print(i) # -> 0, 2, 4, 6, 8
    
Cрезы:
text = 'съешь ещё этих мягких французских булок'
print(text[0])				# с
print(text[1])				# ъ
print(text[len(text)-1])	# к
print(text[-5])				# б
print(text[:])				# съешь ещё этих мягких французских булок
print(text[:2])				# съ
print(text[len(text)-2:])	# ок
print(text[2:9])			# ешь ещё
print(text[6:-18])			# ещё этих мягких
print(text[0:len(text):6])	# сеикакл
print(text[::6])			# сеикакл
text = text[2:9] + text[-5] + text[:2]	# ...
"""