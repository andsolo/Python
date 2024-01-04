# Найдите сумму цифр трехзначного числа n.
# Результат сохраните в перменную res.
"""
n = 123
res = 0

while n > 0:
    x = n % 10
    res += x
    n = n // 10

print(res)
"""


# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали n журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое 
# количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# Выведите через пробел количество журавликов, сделанных Петей, Катей и Сережей
"""
n = 6
sergey = n // 6
petya = sergey
katya = (sergey + petya)*2

print (int(sergey), int(katya), int(petya))
"""


# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета с номером n и выводит на экран yes или no.
# n = 385916 -> yes
"""
n = 385916

FirstSimb = n // 1000
FirstSum = 0
x = 0 

while FirstSimb > 0:
    x = FirstSimb % 10
    FirstSum += x
    FirstSimb //= 10

SecSimb = n % 1000
SecSum = 0
y = 0

while SecSimb > 0:
    y = SecSimb % 10
    SecSum += y
    SecSimb //= 10

if FirstSum == SecSum:
    print("yes")
else:
    print("no")
"""


# Определите, можно ли от шоколадки размером a * b долек отломить c долек, если разрешается сделать один разлом 
# по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# Выведите yes или no соответственно.
"""
a = 3
b = 2
c = 4

if (a * b) > c:
    if c % a == 0 or c % b == 0:
        print('yes')
    else:
        print('no')
else:
    print('no')
"""