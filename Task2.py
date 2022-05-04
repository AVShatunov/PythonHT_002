"""
Задача 2
Пользователь в цикле вводит 10 производных цифр. Выведите количество введеных пользователем цифр 5.
"""

N = 10
i = 0
i5 = 0
dig = ''
while i < 10:
    dig = input('Введите цифру №' + str(i+1) + ': ')
    if len(dig) > 0:
        if '5' == dig[0]:
            i5 += 1
        if dig[0].isdigit():
            i += 1

if i5 == 1:
    ending = 'у'
elif i5 >= 2 and i5 <= 4:
    ending = 'ы'
else:
    ending = ''
print('Вы ввели', i5, 'цифр' + ending + ' "5"')