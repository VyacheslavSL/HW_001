# Пользователь вводит число, Вам необходимо вывести число Пи с той точностью знаков после запятой,
#  сколько указал пользователь(БЕЗ round())


number = int(input('Введите число, показывающее количество знаков после запятой в числе ПИ: '))
import math

a = int(math.pi * (10**number))
res = a / 10**number
print(res)





