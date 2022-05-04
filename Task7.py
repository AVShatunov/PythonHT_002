'''
Задача 7
Найти произведение цифр числа.
    Пример:
    254314
    Произведение цифр числа - 480(2*5*4*3*1*4)
'''

# требуем число и только его!
s = ''
while not s.isdigit():
    s = input('Введите число: ')

i = 0;
n = len(s)
digits_product = 1
out_str = ''
while i < n:
    digits_product *= int(s[i])
    if i > 0:
        out_str += '*'
    out_str += s[i]
    i += 1

print('Произведение цифр числа -', digits_product, '(' + out_str + ')')