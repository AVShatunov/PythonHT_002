"""
(!!!Подсказка на следующую задачу - превратите число в строку, а потом работайте с строкой)
Задача 5
Вывести цифры числа на каждой новой строке.
Пример:
     123567
     1
     2
     3
     4
     5
     6
     7
"""

# the_number = 456987
s = ''
while not s.isdigit():
    s = input("Введите число: ")
the_number = int(s)

s = str(the_number)

# variant 1
N = len(s)
i = 0
while i < N:
    print(s[i])
    i += 1

# variant 2
# for c in s:
#     print(c)
