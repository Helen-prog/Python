# name = "Irina"  # строчный комментарий
# age = 26  # текст
#
# print("Hello", name)
# print("Мне", age, "лет")
#
# print(type(name))
# print(type(age))

# a = "строка"
# print(a)
# a = 56.7
# print(a, type(a))


# a = 4
# b = 5
# print(a, id(a))
# print(b, id(b))
# a = b  # 5
# print(a)
# print(a, id(a))
# print(b, id(b))

# name = "Irina"
# print(name)


# import keyword
# print(keyword.kwlist)

# a = b = c = 1
# print(a)
# print(b)
# print(c)


# a, b, c = 5, "Hello", 9.2
# print(a)
# print(b)
# print(c)

# a = 10
# b = 12
# print("a:", a)
# print("b:", b)

# a, b = b, a

# c = a  # 10
# a = b  # 12
# b = c  # 10

# print("a:", a)
# print("b:", b)

# Константы

# PI = 3.14
# print(PI)

# print("ст   ро   ка \
# символов")
# print('строка символов строка символов строка символов строка символов строка символов строка символов строка '
#       'символов строка символов строка символов строка символов строка символов строка символов ')

# print("    Строка \nсимволов")
# print("\tДокумент \"file.py\" находится по пути \rD:\\folder\\file.py")

# s1 = "Hello"
# s2 = "World"
# s3 = s1 + " " + s2 + "_____"  # конкатенация строк
# print(s3 * 5)

# print(6 + 2)
# print(6 - 2)
# print(6 * 2)
# print(6 / 2)
# print(7 / 2)
# print(7 // 2)
# print(7 ** 2)
# print(7 % 2)

# a = 5
# b = 7
# c = 3
# res = a + b + c
# print("сумма:", res)
# print("произведение", a * b * c)
# print("среднее ар.", res / 3)

# number = ((6 + 4) * 5) ** 2 + 7
# print(number)
#
# number = (6 + 4) * (5 ** 2 + 7)
# print(number)

# num = 10
# print(num)
#
# num += 5  # num = num + 5    num = 15
# print(num)
#
# num -= 3  # num = num - 3
# print(num)

# num = 9753  # 975
# print("Исходное число:", num)
# a = num % 10  # последняя цифра
# print("a:", a)
# num = num // 10
# print(num)
# b = num % 10
# print("b:", b)
# num = num // 10
# print(num)
# c = num % 10
# print("c:", c)
# num = num // 10
# print(num)
# d = num % 10
# print("d:", d)
# # a = 1
# # b = 2
# # c = 3
# # d = 4
# print("Обратное число:", a * 1000 + b * 100 + c * 10 + d)

# num = 4321
# res = num % 10 * 1000  # 1000
# num //= 10  # num = num // 10
# res += num % 10 * 100  # 200
# num //= 10
# res += num % 10 * 10
# num //= 10
# res += num % 10
# print(num)
# print(res)

# num1 = "2"
# num2 = 3
# num2 = str(num2)  # '3'
# res = num1 + num2
# print(res)
# # res = int(num1) + num2
# # print(res)
# # print(type(num1))
# print(type(num2))

# print(int(3.987))
# print(round(3.987))
# print(round(3.985, 2))

# name = "Виктор"
# age = 28
# print("Меня зовут", name, ". Мне", age, "лет.")
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# print("Меня зовут ", name, ". Мне ", age, " лет.", end=" ", sep="")
# print("Продолжение строки")

# name = input("Введите имя: ")
# print("Hello", name)

# num = int(input("Введите число: "))  # 5
# power = int(input("Введите степень: "))
# # num = int(num)
# # power = int(power)
# res = num ** power
# print("Число", num, "в степени", power, "равно:", res)

# b1 = True
# b2 = False
# print(type(b1))
# print(b1)
# print(b2)
#
# print(b1 + 5)  # 1 + 5 = 6
# print(b2 + 5)  # 0 + 5 = 5

# =====================================
# False => "", 0, 0.0, False, None
# =====================================

# print(bool("Python"))
# print(bool(""))
# print(bool(-5))
# print(bool(0))
# print(bool(0.1))
# print(bool(0.0))
# print(bool(False))
# print(bool(None))

# test = None
# print(test)
# print(type(test))
# test = 5
# print(test)

# print(7 == 7)
# print(2 + 5 == 7)
# print(7 != 10 - 3)
# print(8 > 5)
# print(8 < 5)
# print(8 >= 8)
# print(8 <= 8)
# print("hello" > "Hello")  # 104 > 72

# print(2 < 4 < 9)  # True : True => True
# print(2 < 4 > 9)  # True : False => False
# print(2 * 5 > 7 >= 4 + 3)  # True : True => True
# print(3 * 3 <= 7 >= 2)  # False : True => False

# print(5 - 3 == 2 and 1 + 7 > 4)
# print(5 - 3 == 2 and 1 + 7 > 10)
#
# print((3 == 2) and (8 > 10))   # False : False => False
# print((3 == 2) == (8 > 10))   # False == False => True


# print(5 - 3 == 2 or 1 + 7 > 4)
# print(5 - 3 == 2 or 1 + 7 > 10)

# print(not 9 - 7)  # not True
# print(not 7 - 7)  # not False

# a = 25
# b = 37
# if a > b:
#     print("Первое число больше второго")
#     print("a > b")
# else:
#     print("Второе число больше первого")
#     print("b > a")

# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешен")
# else:
#     print("Доступ запрещен")

# a = input("Введите первое число: ")
# b = input("Введите второе число: ")

# if a > b:
#     print("a > b")
# if a == b:
#     print("a == b")
# if a < b:
#     print("a < b")

# if a > b:
#     print("a > b")
# elif a == b:
#     print("a == b")
# else:
#     print("a < b")

# a = 5
# print(id(a), type(a))

# a = input("Введите первую строну: ")
# b = input("Введите вторую строну: ")
# c = input("Введите третью строну: ")
#
# if a == b == c:  # '10' == '50' == 'abc'
#     print("Треугольник равносторонний")
# elif a == b or a == c or b == c:
#     print("Треугольник равнобедренный")
# # elif a != b != c:
# else:
#     print("Треугольник разносторонний")

# day = int(input("Введите день недели (цифрой): "))  # 2
# if 1 <= day <= 5:  # (day >= 1) and (day <= 5)
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("понедельник")
#     if day == 2:
#         print("вторник")
#     if day == 3:
#         print("среда")
#     if day == 4:
#         print("четверг")
#     if day == 5:
#         print("пятница")
# elif day == 6 or day == 7:
#     print("Выходной день - ", end="")
#     if day == 6:
#         print("суббота")
#     if day == 7:
#         print("воскресенье")
# else:
#     print("Такого дня недели не существует")


# day = int(input("Введите день недели (цифрой): "))  # 2
# st = ""
# if 1 <= day <= 5:  # (day >= 1) and (day <= 5)
#     print("Рабочий день - ", end="")
#     if day == 1:
#         st = "понедельник"
#     if day == 2:
#         st = "вторник"
#     if day == 3:
#         st = "среда"
#     if day == 4:
#         st = "четверг"
#     if day == 5:
#         st = "пятница"
# elif day == 6 or day == 7:
#     print("Выходной день - ", end="")
#     if day == 6:
#         st = "суббота"
#     if day == 7:
#         st = "воскресенье"
# else:
#     st = "Такого дня недели не существует"
#
# print(st)


# day = int(input("Введите день недели (цифрой): "))  # 2
# if day == 1:
#     print("Рабочий день - понедельник")
# elif day == 2:
#     print("Рабочий день - вторник")
# elif day == 3:
#     print("Рабочий день - среда")
# elif day == 4:
#     print("Рабочий день - четверг")
# elif day == 5:
#     print("Рабочий день - пятница")
# elif day == 6:
#     print("Выходной день - суббота")
# elif day == 7:
#     print("Выходной день - воскресенье")
# else:
#     print("Такого дня недели не существует")


# n = int(input("Введите количество ворон: "))
# if 0 <= n <= 9:
#     # ...  # pass
#     print("На ветке", end=" ")
#     if n == 1:
#         print(n, "ворона")
#     if 2 <= n <= 4:  # elif
#         print(n, "вороны")
#     if 5 <= n <= 9 or n == 0:  # else:
#         print(n, "ворон")
# else:
#     print("Ошибка ввода")

# password = "qwerty"
#
# match password:
#     case 'admin':
#         print("Администратор")
#     case 'user':
#         print("Пользователь")
#     case "moderator":
#         print("Модератор")
#     case _:
#         print("Пароль не верен")

# day = "вторник"
# time = 18
#
# match day:
#     case "понедельник" | "вторник" | "среда" | "четверг" | "пятница" if 8 <= time <= 17:
#         print("Рабочий день")
#         if 12 <= time <= 14:
#             print("Сейчас перерыв")
#     case "суббота" | "воскресенье":
#         print("Выходной день")
#     case _:
#         print("Такого дня недели не существует или нерабочее время")


# a, b = 20, 20
# print(a if a < b else b)

# a, b = 30, 40
# print("a == b" if a == b else "a > b" if a > b else "b > a")

# try:  # попытаться
#     n = int(input("Введите целое число: "))
#     print(n * 2)
# except ValueError:
#     print("Что-то пошло не так")
#
# print("Код далее")

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except ValueError:
#     print("Нельзя вводить строки")
# except ZeroDivisionError:
#     print("Нельзя делить на 0")

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print("Нельзя вводить строки или Нельзя делить на 0")
# else:  # когда в блоке try не возникло исключения
#     print("Все нормально. Вы ввели числа", n, "и", m)
# finally:  # выполнится в любом случае
#     print("Конец программы")

# n = input("Введите первое число: ")  # '3'
# m = input("Введите второе число: ")  # 'wwww'
#
# try:
#     n = int(n)  # 3
#     m = int(m)  # 'wwww'
# except ValueError:
#     n = str(n)  # '3'
#     # m = str(m)
# finally:
#     print(n + m)


# Цикл

# i = 0  # счетчик
# while i < 5:  # условие
#     print("i =", i)
#     i += 1  # шаг цикла   i = i + 1

# итерация - один шаг цикла

# i = 100
# while i >= 0:
#     print("i =", i)
#     i -= 10

# i = 2
# while i <= 20:
#     print(i, end=" ")
#     i += 2
# print()
# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print(i, end=" ")
#     i += 1
#
#
# print()
# i = 1
# while i <= 20:
#     # проверка на нечетность числа
#     # if i % 2 == 1:
#     # if i % 2 != 0:
#     if i % 2:  # 5 % 2
#         print(i, end=" ")
#     i += 1

# n = int(input("Укажите кол-во символов: "))
# print("*" * n)

# n = int(input("Укажите кол-во символов: "))
# i = 0
# while i < n:
#     print("*", end="")
#     i += 1

# n = int(input("Укажите кол-во символов: "))
# i = 0
# while i < n:
#     print("*")
#     i += 1

# n = int(input("Укажите кол-во символов: "))
# i = 0
# while i < n:
#     if i % 2 == 0:
#         print("+", end="")
#     else:
#         print("-", end="")
#     i += 1

# a = int(input("Введите начало диапазона: "))  # 1
# b = int(input("Введите конец диапазона: "))  # 5
# res = 0
# while a <= b:
#     if a % 2:  # 1 3 5
#         res += a  # res = res + a   9 = 4 + 5
#     a += 1
#
# print("Сумма целых нечетных чисел:", res)

# n = input("Введите целое число: ")
#
# while type(n) is not int:  # !=
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое!")
#         n = input("Введите целое число: ")
#
# if n % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")

# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен!")

# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1

# while True:
#     n = int(input("Введите положительное число: "))
#     if n < 0:
#         break
# res = 1
# while True:
#     n = int(input("Введите число: "))
#     if n == 0:
#         break
#     res *= n  # res = res * n
#
# print("Результат:", res)

# res = 0
# while True:
#     n = int(input("Введите число: "))
#     res += n  # res = res + n
#     if n == 0:
#         break
#
# print("Результат:", res)


# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# else:
#     print("Цикл окончен, i =", i)

# i = 1
# while i < 5:
#     print("Внешний цикл: i =", i)
#     j = 1
#     while j < 4:
#         print("\tВнутренний цикл: j =", j)
#         j += 1
#     i += 1

# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i * j, end="\t\t")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 3:
#     j = 0
#     while j < 6:
#         print("^", end="")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if j % 2 == 0:
#             print("+", end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1


# i = 1
# while i < 5:
#     print("Внешний цикл: i =", i)
#     j = 1
#     while j < 4:
#         print("\tВнутренний цикл: j =", j)
#         n = 1
#         while n < 4:
#             print("\t\tВнутренний цикл: n =", n)
#             n += 1
#         j += 1
#     i += 1

# for element in collection:
#     print(element)


# for i in "Hello!", "World":
#     print(i)

# print(range(5))

# range(start, stop, step)  start=0, step=1
# n = 20
# for i in range(n, 0, -2):
#     print(i, end=" ")
#
# print()
#
# i = 20
# while i != 0:
#     print(i, end=" ")
#     i -= 2

# for i in range(10, 100):  # 11
#     if i % 10 == i // 10:
#         print(i, end=" ")

# for i in range(10):
#     if i == 3:
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break


# for i in range(10):
#     print(i, end=" ")
#     if i == 5:
#         break
# else:
#     print("\nЦикл окончен")

# for i in range(3):
#     print("+++")
#     for j in range(2):
#         print("-----")

# w = int(input("Введите ширину: "))
# h = int(input("Введите высоту: "))
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i == h - 1 or j == 0 or j == w - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()


# print([i * 2 for i in "Python"])
# print([i for i in range(30) if i % 2 == 0])


# Список (list)

# num = [8, 6, 7, 4, 9, 2, 3, "one"]
# print(num)
# # print(num[0])
# # print(num[1])
# # print(num[6])
# # print(num[-1])
# # print(len(num))
# # print(type(num))
# num[1] = 256
# print(num)
# num[3] += 100
# print(num)
# num[-1] += "two"
# print(num)
# print(len(num))

# s = []
# print(s, type(s))
#
# s1 = list("Hello")
# print(s1, type(s1))

# print(range(5))
# print(list(range(5)))
# print(list(range(2, 10)))
# print(list(range(10, 2, -2)))

# [выражение for переменная in последовательность]

# print([0 for i in range(5)])  # [0, 0, 0, 0, 0]
# print([i ** 2 - 1 for i in range(5)])  # [0, 1, 2, 3, 4]  => [0, 1, 4, 9, 16]
# print([i * 3 for i in "Hello"])  # ['HHH', 'eee', 'lll', 'lll', 'ooo']

# a = [1, 2, 3]
# b = [4, 5]
# c = a + b
# print(c)
# d = c * 3
# print(d)

# a = [0] * int(input("Введите количество элементов списка: "))
# print(a)  # [15, 7, 0, 0, 0, 0]
# for i in range(len(a)):  # for i in range(6):
#     a[i] = int(input("-> "))
#
# print(a)

# a = [input("-> ") for i in range(int(input("n = ")))]  # [input("-> ") for i in range(5)]
# print(a)

# lst = ["a", "b", "c", "d"]
#
# for i in range(1, len(lst) - 1):  # 0 1 2 3
#     print(lst[i], end=" ")  # lst[1]
#
# print()
#
# for i in lst:  # a b c d
#     print(i, end=" ")

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
# res = 0
# for i in range(len(a)):
#     if a[i] < 0:
#         res += a[i]
#
# print("Сумма отрицательных элементов:", res)

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
# res = 0
# for i in a:
#     if i < 0:
#         res += i
#
# print("Сумма отрицательных элементов:", res)

# lst = list(range(21, 41))
# print(lst)
# s = k = 0
# for i in range(len(lst)):
#     if lst[i] % 2 == 0:
#         k += 1
#     else:
#         s += lst[i]
#
# print("Количество четных элементов списка:", k)
# print("Сумма нечетных элементов списка:", s)

# lst = list(range(21, 41))
# print(lst)
# s = k = 0
# for i in lst:
#     if i % 2 == 0:
#         k += 1
#     else:
#         s += i
#
# print("Количество четных элементов списка:", k)
# print("Сумма нечетных элементов списка:", s)


# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)

# for i in range(len(a)):
#     if i % 2 == 0:
#         print(a[i], end=" ")

# for i in range(0, len(a), 2):  # range(0, 7, 2)
#     print(a[i], end=" ")


# i = 0
# while i < 7:
#     print(i)  # 0 2 4 6
#     i += 2

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
# for i in range(1, len(a)):  # 0 1 2 3 4 5
#     if a[i] > a[i - 1]:  # a[1] > a[0]
#         print(a[i], end=" ")

# print(a[1] > a[0])
# print(a[i] > a[i - 1])

# i = 0  # 5
# while i < 5:  # 5 < 5
#     j = 0  # 0
#     while j < i:  # 0 < 4
#         print(" ", end="")
#         j += 1
#     print("*")
#     i += 1


# i = 0  # 5
# while i < 5:
#     print(" " * i, "*", sep="")
#     i += 1

# for i in range(5):  # for(i = 1; i < 5; i += 2)
#     print(" " * i, "*", sep="")

# список[start:stop:step]  # [0:len():1]
# s = [5, 9, 3, 7, 1, 8]  # len(s) = 6
# print(s[1:])
# print(s[1:3])
# print(s[1:3:1])
# print(s[4:0:-1])
# print(s[10:11])


# lst = list(range(1, 8))
# print(lst)  # [1, 2, 3, 4, 5, 6, 7]
# # print(lst[::-1])
# # print(lst[::2])
# # print(lst[1::2])
# # print(lst[:1])
# # print(lst[-1:])
# # print(lst[-4:-3])
# # print(lst[3:4])
# # print(lst[-3:])
# # print(lst[4:1:-1])
# # print(lst[2:5])
# lst[1:3] = [0, 0, 0, 0]
# print(lst)
# lst[1:1] = [20, 30]
# print(lst)
# lst[1:2] = [100]
# print(lst)
# lst[1] = 120
# print(lst)
# print(len(lst))
# lst[11:] = [45]
# print(lst)
# print(len(lst))

# print(dir(list))


# lst = list(range(1, 8))
# print(lst)  # [1, 2, 3, 4, 5, 6, 7]
# lst.append(99)
# print(lst)
# lst.extend([100, 101, 102])
# print(lst)
# lst.insert(3, 33)
# print(lst)

# s = []  # [3, 9, 8, 7, 1]
# n = int(input("Кол-во элементов списка: "))
# for num in range(n):
#     x = int(input("Введите число: "))
#     # s.append(x)
#     s.insert(0, x)
# print(s)

# a = [5, 9, 2, 1, 4, 3, 2, 4]  #
# b = [4, 2, 1, 3, 7, 2]
# c = []  # [2, 1, 4, 3]
#
# # for i in a:  # 2
# #     for j in b:  # 4
# #         if i in c:
# #             continue
# #         if i == j:
# #             c.append(i)
# #             break
#
# for i in a:
#     if i in b and i not in c:
#         c.append(i)
#
# print(c)

# a = [1, 2, 3]
# b = [11, 22, 33, 4, 5]
# c = []
#
# if len(b) > len(a):
#     for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):  # range(3, 5)
#         c.append(b[i])
# else:
#     for i in range(len(b)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(b), len(a)):  # range(3, 5)
#         c.append(a[i])
#
# print(c)


# lst = [1, 11, 2, 22, 3, 3, 4, 5, 3, 3]
# # print(lst)
# # lst[:] = []
# # del lst[:]
# # print(lst)
#
# # last = lst.pop(8)
# # print(lst)
# # print(last)
#
# # ind = -9
# # # try:
# # #     lst.pop(ind)
# # # except IndexError:
# # #     print("Такого индекса не существует")
# # if len(lst) * -1 <= ind < len(lst):  # (ind < len(lst)) and ind >= len(lst) * -1
# #     lst.pop(ind)
# # else:
# #     print("Такого индекса не существует")
# # # print(len(lst) * -1)  # -8
# # print(lst)
# # lst.clear()
# # print(lst)
# # print(lst.count(2))
# # print(lst.index(3, 6, 9))
# # if 4 in lst:
# #     print(lst.index(4))
# # b = lst.copy()
# # print("lst:", lst, id(lst))
# # print("b:", b, id(b))
# # b.append(100)
# # lst.append(200)
# # print("lst:", lst)
# # print("b:", b)
#
# # lst.reverse()
# # print(lst)
# # lst2 = list(reversed(lst))
# # print(lst2)
# # print(lst)
#
# # lst.sort(reverse=True)
# # print(lst)
#
# st = ["Виталий", "Сергей", "Александр", "Анна"]
# print(st)
# # st.sort(key=len, reverse=True)  #
# # print(st)
#
# st2 = sorted(st, key=len, reverse=True)
# print(st2)
# print(st)

# print()

# import random

# print(random.random())
# print(random.randint(5, 9))
# print(random.randrange(1, 9))
# print(round(random.uniform(10.5, 25.5), 2))

# city = ['Москва', 'Новосибирск', 'Воронеж', 'Сочи', 'Екатеринбург']
# s = [11, 55, 22, 33, 66, 77, 44, 88, 99, 12, 45, 78, 98, 65, 32, 10]
#
# # print(random.choice(city))
# # print(random.choice(s))
# #
# # print(random.choices(city, k=3))
# # print(random.choices(s, k=3))
#
# random.shuffle(city)
# random.shuffle(s)
#
# print(city)
# print(s)

import random

# lst = [random.randint(50, 100) for i in range(10)]
# print(lst)
# print(len(lst))
# print(min(lst))
# print(max(lst))
# print(sum(lst))

# lst = [random.randint(0, 100) for i in range(10)]
# print(lst)
# max_ = max(lst)
# print("MAX:", max_)
# lst.remove(max_)
# lst.insert(0, max_)
# print(lst)

# lst = [random.randint(0, 100) for i in range(10)]
# print(lst)
# min_ = min(lst)
# print("MIN:", min_)
# ind_min = lst.index(min_)
# print("INDEX:", ind_min)
# del lst[:ind_min]
# print(lst)


# n1 = int(input("Введите размер первого списка: "))
# n2 = int(input("Введите размер второго списка: "))
# a = [random.randint(0, 10) for i in range(n1)]
# b = [random.randint(0, 10) for j in range(n2)]
# print("Первый список:", a)
# print("Второй список:", b)
# # c = a + b
# # print(c)
# # c = []
# # for i in range(len(a)):
# #     if a[i] not in c:
# #         c.append(a[i])
# # for i in range(len(b)):
# #     if b[i] not in c:
# #         c.append(b[i])
# # print(c)
# # c = []
# # for i in range(len(a)):
# #     if a[i] in b and a[i] not in c:
# #         c.append(a[i])
# c = [min(a), min(b), max(a), max(b)]
# print(c)


# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# print(m)
# # print(len(m))  # 3
# # print(m[1][2])
#
# print("Вариант 1")
# for row in range(len(m)):
#     # print(m[row])
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t")
#     print()
#
# print("Вариант 2")
# for x in m:
#     # print(x)
#     for y in x:
#         print(y, end="\t")
#     print()


# import math
#
# print(math.sqrt(4))
# print(math.ceil(3.2))
# print(math.floor(3.8))
# print(math.pi)

# import math as m
#
# print(m.sqrt(4))
# print(m.ceil(3.2))
# print(m.floor(3.8))
# print(m.pi)

# from math import *
#
# print(sqrt(4))
# print(ceil(3.2))
# print(floor(3.8))
# print(pi)

# from math import sqrt, ceil, floor, pi
#
# print(sqrt(4))
# print(ceil(3.2))
# print(floor(3.8))
# print(pi)

# from math import pi
#
# radius = int(input("Введите радиус: "))
# print("Площадь окружности:", pi * (radius ** 2))

import time
import locale

# print(time.time())
# print(time.ctime(46439896))
# print(time.localtime())
# t = time.localtime()
# print(t.tm_mday, t.tm_mon, t.tm_year)
# print(time.strftime("Today is %B %d, %Y."))
# print(time.strftime("%m/%d/%Y, %H:%M:%S"))
#
# locale.setlocale(locale.LC_ALL, "ru")
# print(time.strftime("Сегодня: %B %d, %Y."))

# start = time.time()
# print("Программа запущена")
# time.sleep(5)
# print("Программа завершена через", time.time() - start, "сек")

# Функции

# def hello(name):  # аргументы
#     print("Hello", name)
#
#
# hello("Irina")  # параметры
# hello("Igor")

# def get_sum(a, b):
#     print(a + b)
#
#
# x = 2
# y = 5
# get_sum(x, y)
# get_sum(12, 3)

# def get_sum(a, b):
#     print("Сумма:", end=" ")
#     return a + b
#
#
# x = 2
# y = 5
# res = get_sum(x, y)
# print(res)

# def maximum(one, two):
#     if one > two:
#         return one
#     else:
#         return two
#
#
# m = maximum(9, 16)
# print(m * 2)

# def cube(a):
#     return a * a * a
#
#
# for i in range(1, 11):
#     print(i, "в кубе =", cube(i))

# def change(lst):
#     # end = lst.pop()
#     # start = lst.pop(0)
#     # lst.insert(0, end)
#     # lst.append(start)
#     lst[0], lst[-1] = lst[-1], lst[0]
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['с', 'л', 'о', 'н']))


# def is_greater(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# # print(is_greater(10, 2))
# # print(is_greater(2, 12))
# a = 10
# b = 12
#
# if is_greater(a, b):
#     print(a, "больше", b)
# else:
#     print(b, "больше", a)

# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:
#         if 'A' <= ch <= 'Z':
#             has_upper = True
#         if 'a' <= ch <= 'z':
#             has_lower = True
#         if '0' <= ch <= '9':
#             has_num = True
#
#     if len(password) >= 8 and has_upper and has_lower and has_num:
#         return True
#     return False
#
#
# p = input("Введите пароль: ")
# if check_password(p):
#     print("Это надежный пароль")
# else:
#     print("Это ненадежный пароль")


# def get_sum(a=1, b=1, c=0, d=1):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))
# print(get_sum(1, 5))
# print(get_sum(1, 5, d=2))
# print(get_sum(c=1))

# def display_info(name, age):
#     print("Name:", name, "\nAge:", age, end="\n\n")
#
#
# display_info("Ira", 23)
# display_info(23, "Ira")
# display_info(age=23, name="Ira")
# # display_info("Igor", age=23, name="Ira")


# a = 'Hello'
# b = 'Hello'
# print(a == b)
# print(a is b)
# print()
# lst1 = [1, 2, 3]
# lst2 = [1, 2, 3]
# print(lst1 == lst2)
# print(lst1 is lst2)
# print(lst1, id(lst1))
# print(lst2, id(lst2))

# a = [1, 2, 3]
# print(a, id(a))
# a.append(4)
# print(a, id(a))

# Кортежи (tuple)

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())
# print(tpl[1])
# tpl[1] = 200


# a = (5, 6, 8, 7, 9)
# a = (5,)
# print(a, type(a))
#
# b = tuple("Hello")
# print(b, type(b))

# a = (5, 6, 8, 7, 9)
# print(a[2])
# print(a[1:3])

# from random import randint
#
# # tpl = tuple(i for i in range(5))
# # tpl = tuple(input("-> ") for i in range(5))
# tpl = tuple(randint(10, 20) for i in range(5))
# print(tpl)

# t1 = tuple("Hello")
# t2 = tuple("World")
# # print(t1)
# # print(t2)
# t3 = t1 + t2
# print(t3)
# print(len(t3))
# print(t1 * 2)
# print(t3.count('l'))
# print(t3.index('l', 4, 9))
# if 'a' in t3:
#     print(t3.index('a'))
# else:
#     print("Такого символа нет")

# for i in t3:
#     print(i, end=" ")

# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             first = tpl.index(el)  # 1
#             second = tpl.index(el, first + 1) + 1  # 5
#             return tpl[first:second]
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return tuple()  # ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# from random import randint
#
#
# def set_tpl(a, b):
#     return tuple(randint(a, b) for i in range(10))
#
#
# tpl1 = set_tpl(0, 5)
# tpl2 = set_tpl(-5, 0)
# print(tpl1)
# print(tpl2)
# tpl3 = tpl1 + tpl2
# print(tpl3)
# print("0 =", tpl3.count(0))

# t = (10, 11, [1, 2, 3], [4, 5, 6], ['Hello', "World"])
# print(t, id(t))
# t[4][0] = "new"
# t[4].append("hi")
# print(t, id(t))

# Распаковка кортежа

# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t  # x, y, z = 1, 2, 3
# print(x, y, z)

# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married
#
#
# first_name, year, married = get_user()  # first_name, year, married = name, age, is_married
# # user = get_user()
# # print(user)
# # first_name, year, married = user
# print(first_name, year, married)
# # print(user[0])
# # print(user[1])
# # print(user[2])

# t = (1, 2, 3)
# del t

# lst = [1, 2, 3, 4, 5]
# print(lst, type(lst))
# tpl = tuple(lst)
# print(tpl, type(tpl))
# lst1 = list(tpl)
# print(lst1, type(lst1))

# countries = (
#     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6)))
# )
#
# print(countries)
# print()
# for country in countries:
#     country_name, country_population, cities = country
#     print("\nСтрана: ", country_name, ", население: ", country_population, sep="")
#     for city in cities:
#         city_name, city_population = city
#         print("\tГород: ", city_name, ", население: ", city_population, sep="")


# Множество (set)

# s = {"banana", "apple", "orange", "banana", "apple"}
# print(s, type(s), len(s))
# # print(s[0])
# for i in s:
#     print(i)

# a = [1, 2, 3]
# s = set(a)
# print(s, type(s))

# from random import randint
#
# # s = {input("-> ") for i in range(6)}
# s = {randint(50, 100) for i in range(6)}
# print(s)

# t = {"red", "green", "blue"}
# print("green" in t)
# print("yellow" in t)

# lst = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# # s = [i for i in lst if 'a' not in i]
# # s = ['A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in lst]
# # s = tuple('A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in lst)
# # s = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in lst}
# s = ['A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in lst if i[1] == 'c']
# print(s)

# t = {"red", "green", "blue"}
# print(t)
# t.add("yellow")
# print(t)
# t.remove("yellow")
# # t.remove("yellow1")  # KeyError
# print(t)
# t.discard("green")
# print(t)
# t.pop()
# print(t)
# t.clear()
# print(t)

# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# # c = a | b
# # c = a.union(b)
# # c = a & b
# # c = a - b
# # c = a ^ b
# # a |= b
# # a &= b
# # a -= b
# a ^= b
# # print(c)
# print(a)

# a = {0, 1, 2, 3, 4}
# b = {3, 2, 1}
# print(a <= b)

# a = set("Hello")
# b = set("How are you")
# s = a & b
# for i in s:
#     print(i, end=" ")

# drawing = {'Марина', 'Женя', 'Света'}
# music = {'Костя', 'Женя', 'Илья'}
#
# print("Одно хобби:", drawing ^ music)
# print("Оба хобби:", drawing & music)
#
# drawing = drawing - (drawing & music)
# print(drawing)

# s = frozenset([1, 2, 3, 4, 5, 6])
# print(s, type(s))

# s = frozenset(["hello", "world", "hello"])
# print(s, type(s))

# Словарь (dict)

# lst = [1, 2, 3]
# d = {1: "one", "two": 2, "three": 3}
# print(lst)
# print(d)
# print(lst[1])
# print(d["two"])
# print(d[1])

# d = {"one": 1, "two": 2}
# print(d, type(d))
#
# d1 = dict(one="один", two=2)
# print(d1, type(d1))
#
# lst = [
#     ['one', 'один'],
#     ['two', 'два'],
#     ['three', 'три'],
# ]
#
# d2 = dict(lst)
# print(d2)

# print({i: input("-> ") for i in range(2, 9)})


# d = {0: "text", "one": 1, (5, 7): "Кортеж", "Список": [9, 8, 7], True: 1, False: "ложь", 1: "один"}
# print(d)
# print(d["Список"][1])
# print(d[(5, 7)][-1])
# print("one" in d)
# print("ложь" in d)

# d = {"one": 1, "two": 2, "three": 3}
# print(d)
# # for key in d:
# #     print(key, ":", d[key])
# print(d["one"])
# del d["one"]
# print(d)

# d = {"x1": 3, "x2": 7, "x3": 5, "x4": -1}
# res = 1
# for key in d:
#     res *= d[key]
#
# print(res)

# d = dict()
# d[1] = input("-> ")
# d[2] = input("-> ")
# d[3] = input("-> ")
# d[4] = input("-> ")
# d = {i: input("-> ") for i in range(1, 5)}
# print(d)
# x = int(input("Какой элемент исключить: "))
# del d[x]
# print(d)

# goods = {
#     "1": ['Core-i3-4330', 9, 4500],
#     "2": ['Core i5-4670K', 3, 8500],
#     "3": ['AMD FX-6300', 6, 3700],
#     "4": ['Pentium G3220', 8, 2100],
#     "5": ['Core i5-3450', 5, 4600],
# }
#
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], "руб", sep="")
#
# while True:
#     n = input("№: ")
#     if n == "0":
#         break
#     else:
#         if n in goods:
#             while True:
#                 try:
#                     qty = int(input("Количество: "))
#                     goods[n][1] += qty
#                     break
#                 except ValueError:
#                     print("Значение некорректное. Введите число.")
#         else:
#             print("Такого ключа не существует")
#
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], "руб", sep="")


# print(dir(dict))

# d = {"x1": 3, "x2": 7, "x3": 5, "x4": -1}

# print(d.keys())
# print(d.values())
# print(d.items())
#
# for i in d.keys():
#     print(i, end=" ")
# print()
# for i in d.values():
#     print(i, end=" ")
# print()
# for i, j in d.items():
#     print(i, ":", j, ",", end=" ")

# print(list(d))
# print(list(d.keys()))
# print(list(d.values()))
# print(list(d.items()))

# d2 = d.copy()
#
# print("D =", d)
# print("D2 =", d2)
#
# d["x2"] = 100
# d2["x4"] = 200
#
# print("D =", d)
# print("D2 =", d2)

# value1 = d["x2"]
# print(value1)
#
# value = d.get("x2", "Такого ключа не существует")
# print(value)

# q = {"one": 1, "two": 2, "three": 3}
# w = [("one", 1), ("two", 2), ("three", 3)]

# d.update(w)
# print(d)

# c = d | q
# print(c)

# item = d.pop("x2", "Такого ключа не существует")
# item = d.popitem()
# print(item)
# print(d)

# a = {
#     'first': {
#         1: "one",
#         2: "two",
#         3: "three"
#     },
#     'second': {
#         4: "four",
#         5: "five"
#     }
# }
#
# print(a)
#
# for x in a:
#     print(x)
#     for y in a[x]:
#         print("\t", y, " -> ", a[x][y], sep="")
#
# print()
# for x, y in a.items():
#     print(x)
#     for i, j in y.items():
#         print("\t", i, " -> ", j, sep="")

# s = "Hello"
# s = [9, 6, 8, 7, 4]
# d = {i: str(i) for i in s}
# print(d)

# x = {1: "one", 2: "two", 3: "three"}
#
# values = list(x.values())
# print(values)
#
# values1 = list(x.keys())
# print(values1)
#
# values1 = list(x.items())
# print(values1)


# a = ["one", 1, 2, 3, "two", 10, 20, "three", 15, 36, 60, "four", -20]
#
# d = dict()  # {"one": [1,2,3], "two": [10, 20]}
# s = None
#
# for i in a:
#     if type(i) is str:  # type(i) == str
#         d[i] = []
#         s = i  # "two"
#     else:
#         d[s].append(i)
#
#
# print(d)

# a = ['Dec', 'Jan', 'Feb']
# b = [12, 1, 2]
# # f = list(zip(a, b))  # [('Dec', 12), ('Jan', 1), ('Feb', 2)]
# f = dict(zip(a, b))  # {'Dec': 12, 'Jan': 1, 'Feb': 2}
# print(f)


# a = ['Dec', 'Jan', 'Feb']
# b = [12, 1, 2, 3, 4, 5]
# c = (7.2,)
# f = list(zip(a, b, c))
# # f = dict(zip(a, b, c))
# print(f)


# d1 = {'name': 'Igor', 'surname': 'Pavlov', 'job': 'Consultant'}
# d2 = {'name': 'Irina', 'surname': 'Petrova', 'job': 'Manager'}
#
# for (k1, v1), (k2, v2) in zip(d1.items(), d2.items()):
#     print(k1, "->", v1)
#     print(k2, "->", v2)
#
#
# for k, v in zip(d1.items(), d2.items()):
#     print(k, ":", v)

# pairs = [(1, "a"), (2, "b"), (3, "c")]
# a, b = zip(*pairs)
# print(a)
# print(b)


# letters = ['b', 'a', 'd', 'c']
# numbers = [3, 4, 1, 2]
# data1 = dict(zip(letters, numbers))
# print(data1)
# data2 = list(zip(numbers, letters))
# print(data2)
# data2.sort()
# print(data2)
# print(dict(data2))
# print({j: i for i, j in data2})


# one = {'b': 3, 'a': 4}
# two = {'d': 1, 'c': 2}
# print({**one, **two})  # {'b': 3, 'a': 4, 'd': 1, 'c': 2}

# a = [1, 2, 3, 4]
# b = [*a, 5, 6, 7]
# print(b)

# def func(*args):
#     return args
#
#
# print(func(5))
# print(func(5, 8, 6))
# print(func())

# def func(*args):  # ()
#     print("*args", *args)
#     print("args", args)
#     res = 0
#     for n in args:
#         res += n
#     return res
#
#
# print(func(1, 2, 3))
# print(func(5, 8, 6, 8, 9, 7, 4))
# print(func(5, 8, 6, 8))
# print(func())

# def func(a, b, *args):
#     return a, b, args
#
#
# # print(func(5, "aaa"))
# print(func(5, 12, 3, 4, 8))

# def func(**kwargs):
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))
# print(func())
# print(func(python="py"))
#
# print(dict(python="py"))
# print(dict({"python": "py"}))


# def func(one, two, *args, d=5, **kwargs):
#     return one, two, args, kwargs, d
#
#
# print(func(9, 8, 7, 5, 4, a=1, b=2, c=3, d=10))

# board = [" "] * 9
# game_over = False
# player = "X"
#
#
# def show():
#     print(board[0] + " | " + board[1] + " | " + board[2])
#     print("- + - + -")
#     print(board[3] + " | " + board[4] + " | " + board[5])
#     print("- + - + -")
#     print(board[6] + " | " + board[7] + " | " + board[8])
#
#
# def check():
#     return (
#         (board[0] == board[1] == board[2] == player) or
#         (board[3] == board[4] == board[5] == player) or
#         (board[6] == board[7] == board[8] == player) or
#         (board[6] == board[7] == board[8] == player) or
#         (board[0] == board[3] == board[6] == player) or
#         (board[1] == board[4] == board[7] == player) or
#         (board[2] == board[5] == board[8] == player) or
#         (board[0] == board[4] == board[8] == player) or
#         (board[2] == board[4] == board[6] == player)
#     )
#
#
# while not game_over:
#     show()
#     move = int(input("\nХод " + player + " (1-9): ")) - 1
#
#     if board[move] == " ":
#         board[move] = player
#     else:
#         print("Занято")
#         continue
#
#     if check():
#         show()
#         print("Пользователь " + player + " победил")
#         game_over = True
#     elif " " not in board:
#         show()
#         print("\nНичья")
#         game_over = True
#
#     player = "0" if player == "X" else "X"

# Области видимости (scope)

# Локальная
# Глобальная

# name = "Tom"
#
#
# def hi():
#     global name
#     name = "Sam"
#     surname = "Johnson"
#     print("Hello", name, surname)
#
#
# def bye():
#     print("Good bye", name)
#
#
# hi()
# bye()
# print(name)

# sum = 5
#
# lst = [8, 9, 6, 3, 2, 1]
# print(sum(lst))

# import builtins
#
# names = dir(builtins)
#
# for t in names:
#     print(t)

# def outer(who):
#     def inner():
#         print("Hello,", who)
#
#     inner()
#
#
# outer("World!")

# def outer():
#     a = 6  # 2
#
#     def inner(b):  # b = 3
#         a = 4  # 5
#         print("local a:", a)  # 6
#         print("sum:", a + b)  # 7
#
#     print("enclosed:", a)  # 3
#     inner(3)  # 4
#
#
# outer()  # 1

# x = 25
# t = 0
#
#
# def fn():
#     global t
#     a = 30  # 35
#
#     def inner():
#         nonlocal a
#         a = 35
#         print("inner:", a)
#
#     inner()
#     t = a
#
#
# fn()
#
# z = x + t  # 25 + 30  # 25 + 35
# print(z)  # 55        # 60

# def fn1():
#     x = 25  # 2
#
#     def fn2():
#         x = 33  # 4
#
#         def fn3():
#             x = 55  # 6
#
#         fn3()  # 5
#         print("fn2.x =", x)  # 7
#
#     fn2()  # 3
#     print("fn1.x =", x)  # 8
#
#
# fn1()  # 1

# x = 5
#
#
# def fn1():
#     x = 25  # 55
#
#     def fn2():
#         # x = 33  # 55
#
#         def fn3():
#             nonlocal x
#             x = 55  #
#
#         fn3()
#         print("fn2.x =", x)  # 33  # 55
#
#     fn2()
#     print("fn1.x =", x)  # 25  # 55
#
#
# fn1()  #

# def outer(a1, b1, a2, b2):
#     a = 0  # 1
#     b = 0  # 7
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#         # print("inner", [a, b])
#
#     inner()
#     return [a, b]
#
#
# print(outer(2, 3, -1, 4))  # [1, 7]


# def outer(a, b, c):
#     def inner(i, j):
#         return i * j
#
#     s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
#
#     return s
#
#
# print(outer(2, 4, 6))
# print(outer(5, 8, 2))
# print(outer(1, 6, 8))

# s = 0
#
#
# def outer(a, b, c):
#     def inner(i, j):
#         return i * j
#
#     global s
#     s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
#
#
# outer(2, 4, 6)
# print(s)
# outer(5, 8, 2)
# print(s)
# outer(1, 6, 8)
# print(s)


# def outer(a, b, c):
#     s = 0
#
#     def inner(i, j):
#         nonlocal s
#         s += i * j
#
#     inner(a, b)
#     inner(a, c)
#     inner(b, c)
#
#     return 2 * s
#
#
# print(outer(2, 4, 6))
# print(outer(5, 8, 2))
# print(outer(1, 6, 8))


# Замыкание

# def outer(n):
#     def inner(x):
#         return n + x  # 5 + 10
#
#     return inner
#
#
# fn = outer(5)
# print(fn(10))
#
# num = outer(6)
# print(num(10))

# def func1():
#     a = 1
#     b = 'line'
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         a = a + 1
#         b = b + "_1"
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())


# def func(city):
#     count = 0  # 2  # 0
#
#     def inner():
#         nonlocal count
#         count += 1
#         print(city, count)
#
#     return inner
#
#
# res1 = func('Москва')
# res1()
# res1()
# res1()
# res1()
# res1()
#
# res2 = func('Сочи')
# res2()
# res2()
# res2()
# res2()
#
# res1()

# def func(x, y):
#     return x + y
#
#
# print(func(5, 2))
# print(func(15, 12))
#
#
# # Анонимные функции (lambda-выражение)
#
# # print((lambda x, y: x + y)(5, 2))
# # print((lambda x, y: x + y)(15, 12))
#
# summa = lambda x, y: x + y
#
# print(summa(5, 2))
# print(summa(15, 12))


# print((lambda x, y: x + y)(5, 2))
# print((lambda x, y=2: x + y)(5))
# print((lambda x, y=2: x + y)(5, 3))
# print((lambda x=1, y=2: x + y)())
# print((lambda *args: args)(1, 2, 3, 4, 5, 6))

# c = (
#     lambda x: x * 2,
#     lambda x: x * 3,
#     lambda x: x * 4,
# )
#
# for t in c:
#     print(t('abc_'))

# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# res = outer(5)
# print(res(2))
#
# # ========================
#
#
# def outer(n):
#     return lambda x: n + x
#
#
# res = outer(5)
# print(res(2))
#
# # ========================
#
# outer = lambda n: lambda x: n + x
#
#
# res = outer(5)
# print(res(2))
#
# # ========================
#
# print((lambda n: lambda x: n + x)(5)(2))

# print((lambda a: lambda b: lambda c: a - b - c if a > 0 and b > 0 and c > 0 else a + b + c)(2)(4)(6))
# print((lambda a: lambda b: lambda c: a - b - c if a > 0 and b > 0 and c > 0 else a + b + c)(-2)(4)(6))

# d = {'b': 15, 'a': 30, 'c': 25}
# lst = list(d.items())
# print(lst)
# lst.sort(key=lambda i: i[1])
# print(lst)
# print(dict(lst))
# print(lst)
#
#
# d = {'b': 15, 'a': 30, 'c': 25}
# new_d = sorted(d.items(), key=lambda i: i[1])
# print(new_d)
# print(d)

# players = [{'name': 'Антон', 'last name': 'Бирюков', 'raiting': 9},
#            {'name': 'Алексей', 'last name': 'Бодня', 'raiting': 10},
#            {'name': 'Федор', 'last name': 'Сидоров', 'raiting': 4},
#            {'name': 'Михаил', 'last name': 'Семенов', 'raiting': 6}]
#
# res = sorted(players, key=lambda item: item['last name'])
# print(res)
#
# res = sorted(players, key=lambda item: item['raiting'])
# print(res)
#
# res = sorted(players, key=lambda item: item['raiting'], reverse=True)
# print(res)


# a = [(lambda x, y: x + y), (lambda x, y: x - y), (lambda x, y: x * y), (lambda x, y: x / y)]
# print(a[0](12, 5))

# d = {
#     1: lambda: print("Понедельник"),
#     2: lambda: print("Вторник"),
#     3: lambda: print("Среда"),
#     4: lambda: print("Четверг")
# }
#
# d[2]()

# import math
#
# area = {
#     'circle': lambda r: math.pi * r * r,
#     'rectangle': lambda a, b: a * b
# }
#
# print("Площадь окружности:", area['circle'](2))
# print("Площадь прямоугольника:", area['rectangle'](10, 13))

# map

# def mult(t):
#     return t * 2


# lst = [2, 8, 12, -5, -10]
#
# # lst2 = list(map(mult, lst))
# # print(lst2)
#
# lst3 = list(map(lambda t: t * 2, lst))
# print(lst3)

# print(list(map(lambda t: t * 2, [2, 8, 12, -5, -10])))


# tpl = (2.88, -1.75, 100.55)
#
# # tpl2 = tuple(map(lambda x: int(x), tpl))
# tpl2 = tuple(map(int, tpl))
# print(tpl2)

# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
#
# res = list(map(lambda x, y: (x, y), st, num))
#
# print(res)


# filter

# t = ('abcd', '', 'abc', 'cdfgh', 'def', 'ghi')
#
# # t2 = tuple(filter(lambda s: len(s) == 3, t))  # tuple('abc', 'def', 'ghi')
# t2 = tuple(filter(lambda s: s, t))  # tuple('abc', 'def', 'ghi')
# print(t2)
#
#
# print(bool(''))


# b = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# res = list(filter(lambda s: s > 75, b))
#
# print(res)

# @name
# def square(n):
#     return n ** 2
#
#
# print(square(5))


# Декораторы

# def hello():
#     return 'Hello, I am func "Hello"'
#
#
# def super_func(func):
#     print('Hello, I am func "super_func"')
#     print(func())
#
#
# super_func(hello)

# def hello():
#     return 'Hello, I am func "Hello"'
#
#
# test = hello
# print(test())


# def my_decorators(func):
#     def wrapper():
#         print("Core before")
#         func()
#         print("Code after")
#
#     return wrapper
#
#
# def func_test():
#     print('Hello, I am func "func_test"')
#
#
# test = my_decorators(func_test)
# test()

# def my_decorators(func):  # декорирующая функция
#     def wrapper():
#         print("-" * 30)
#         func()
#         print("=" * 30)
#
#     return wrapper
#
#
# @my_decorators   # декоратор
# def func_test():  # декорируемая функция
#     print('Hello, I am func "func_test"')
#
#
# @my_decorators
# def hello():
#     print('Hello, I am func "Hello"')
#
#
# func_test()
# hello()

# def circle(fn):
#     def wrap():
#         return '(' + fn() + ')'
#
#     return wrap
#
#
# def angle(fn):
#     def wrap():
#         return '<' + fn() + '>'
#
#     return wrap
#
#
# @angle
# @circle
# def expression():
#     return '5 + 2'
#
#
# print(expression())

# def cnt(fn):
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count = count + 1
#         fn()
#         print("Вызов функции:", count)
#
#     return wrap
#
#
# @cnt
# def hello():
#     print("Hello")


# @cnt
# def bye():
#     print("Bye")
#
#
# hello()
# hello()
# hello()
# bye()
# bye()
# hello()
# hello()


# def args_decorators(fn):
#     def wrap(arg1, args2):
#         print("*" * 30)
#         fn(arg1, args2)
#         print(arg1, args2)
#
#     return wrap
#
#
# @args_decorators
# def print_full_name(name, surname):
#     print("Меня зовут", name, surname)
#
#
# print_full_name("Ирина", "Федорова")


# def args_decorators(fn):
#     def wrap(*args, **kwargs):
#         print("args:", args)
#         print("kwargs:", kwargs)
#         fn(*args, **kwargs)
#
#     return wrap
#
#
# @args_decorators
# def print_full_name(a, b, c, d='Фамилия', study="Python"):
#     print(a, b, c, d, "изучают", study, end="\n\n")
#
#
# @args_decorators
# def bye():
#     print("Bye")
#
#
# print_full_name("Ирина", "Елизавета", "Светлана", study="JavaScript")
# print_full_name("Владимир", "Екатерина", "Виктор")
# bye()

# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, "=", end=" ")
#             fn(x, y)
#
#         return wrap
#
#     return args_dec
#
#
# @decor("Сумма:", "+")
# def summa(a, b):
#     print(a + b)
#
#
# @decor("Разность:", "-")
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(5, 2)

# def multiply(arg):
#     def outer(func):
#         def inner(*args, **kwargs):
#             return arg * func(*args, **kwargs)
#
#         return inner
#
#     return outer
#
#
# @multiply(3)
# def return_num(num):
#     return num
#
#
# print("Результат:", return_num(5))

# def typed(*args, **kwargs):
#     def wrapper(fn):
#         def wrap(*f_args, **f_kwargs):
#             for i in range(len(args)):
#                 if type(f_args[i]) is not args[i]:  # if type(f_args[i]) != args[i]:
#                     raise TypeError("Недопустимый тип данных")
#
#             for k in kwargs:
#                 if type(f_kwargs[k]) is not kwargs[k]:
#                     raise TypeError("Недопустимый тип данных в именованном параметре")
#
#             return fn(*f_args, **f_kwargs)
#
#         return wrap
#
#     return wrapper
#
#
# @typed(int, int, int)
# def typed_fn(x, y, z):
#     return x * y * z
#
#
# @typed(str, str, str)
# def typed_fn2(x, y, z):
#     return x + y + z
#
#
# @typed(str, str, z=int)
# def typed_fn3(x, y, z="Hello! "):
#     return (x + y) * z
#
#
# # print(typed_fn(3, 4, 5))
# # print(typed_fn(3, 4, "5"))
# # print(typed_fn("три", "4", "5"))
# # print(typed_fn2("Hello", "World", "!"))
# print(typed_fn3("Hello", "World___", z=5))
# # print(typed_fn3("Hello", "World___", z="!"))

# def args_decorator(tx=None, decorator_text=''):
#     def my_decorator(fn):
#         def wrap(*args):
#             print(decorator_text, end="")
#             fn(*args)
#         return wrap
#
#     if tx is None:
#         return my_decorator
#     else:
#         return my_decorator(tx)
#
#
# @args_decorator(decorator_text="Hello, ")
# def hello_world(text):
#     print(text)
#
#
# @args_decorator
# def hello_world2(text):
#     print(text)
#
#
# hello_world("world!")
# hello_world2("Hi!")

# print(0b1010)  # 0b - двоичная система счисления
# print(0o12)  # 0o - восьмеричная
# print(0xA)  # 0x - шестнадцатеричная
# print(0b1010 + 0o12 + 0xA)

# print(bin(18))  # 0b - двоичная система счисления
# print(oct(18))  # 0o - восьмеричная
# print(hex(18))  # 0x - шестнадцатеричная

# q = 'Pyt'
# w = "hon"
# e = q + w
# # print(e * 3)
# # print("y" in e)
# # print("w" in e)
# print(e)
# # print(e[1])
# # print(e[-1])
# # e[1] = "i"  // не работает
# print(e[1:4])
# print(e[:4])
# print(e[-1:0:-1])

# def changeCharToStr(s, c_old, c_new):
#     s2 = ""  # "Я изучаю Python. Мне нравится "
#     i = 0
#
#     while i < len(s):
#         if s[i] == c_old:
#             s2 = s2 + c_new
#         else:
#             s2 = s2 + s[i]
#         i = i + 1
#
#     return s2
#
#
# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования."
# str2 = changeCharToStr(str1, "N", "P")
# print("str1 =", str1)
# print("str2 =", str2)
#
# str3 = changeCharToStr(str1, "о", "О")
#
# print("str3 =", str3)

# print("Привет")
# print(u"Привет")

# print('C:\file.txt')
# print('C:\\file.txt')
# print(r'C:\file.txt')


# print(b'a1b2c2')
# print(b'a1b2c2'[1])

# name = "Дмитрий"
# age = 25
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# print("Меня зовут ", name, ". Мне ", age, " лет.", sep="")
# print(f"Меня зовут {name}. Мне {age} лет.")

# x = 10
# y = 5
# print(f"{x=}, {y=}")
# print(f"{x} x {y} / 2 = "
#       f"{x * y / 2}")

# print(f"{round(2.12345678, 2)}")
# print(f"{2.12345678:.2f}")

# dir_name = "my_doc"
# file_name = "data.txt"
# print(fr"home\{dir_name}\{file_name}")
#
# print("home\\" + dir_name + "\\" + file_name)

# "Hello World"
#
# '''Hello
#      World'''
#
# """Hello
#     World"""

# print(s)
# print(s1)
# print(s2)

# def square(n):
#     """Принимает число n, возвращает квадрат числа n"""
#     a = 5
#     return n ** 2
#
#
# print(square(5))
# print(square.__doc__)
# print(sum.__doc__)

# import math
#
#
# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     """
#     return 2 * math.pi * r * (r + h)
#
#
# print(cylinder(2, 4))

# print(ord('a'))
# print(ord('ш'))
# while True:
#     n = input("-> ")
#     if n != "-1":
#         print(ord(n))
#     else:
#         break
#
# print(chr(1104))


# a = 97
# b = 122
#
# # if a > b:
# #     for i in range(b, a + 1):
# #         print(chr(i), end=" ")
# # else:
# #     for i in range(a, b + 1):
# #         print(chr(i), end=" ")
# if b > a:
#     a, b = b, a
#
# for i in range(b, a + 1):
#     print(chr(i), end=" ")

# my_str = "Test string for me "
# arr = [ord(x) for x in my_str]
# print(f"ASCII коды: {arr}")
# arr = [int(sum(arr) / len(arr))] + arr
# print("Среднее арифметическое:", arr)
# arr += [ord(x) for x in input("-> ")[:3] if ord(x) not in arr]
# print(arr)
# print(arr.count(arr[-1]) - 1)
# arr.sort(reverse=True)
# print(arr)

# print(5 > 3)
# print("apple" > "Apple")  # 97 > 65

# from random import randint
#
# SHORTEST = 7
# LONGEST = 16
# MIN_ASCII = 33
# MAX_ASCII = 126
#
#
# def random_password():
#     random_length = randint(SHORTEST, LONGEST)
#     result = ""
#     for i in range(random_length):
#         random_char = chr(randint(MIN_ASCII, MAX_ASCII))
#         result += random_char
#     return result
#
#
# print("Ваш случайный пароль:", random_password())

# s = "hello, WORLD! I am learning Python."
# print(s.capitalize())  # Hello, world! i am learning python.
# print(s.lower())  # hello, world! i am learning python.
# print(s.upper())  # HELLO, WORLD! I AM LEARNING PYTHON.
# print(s.swapcase())  # HELLO, world! i AM LEARNING pYTHON.
# print(s.title())  # Hello, World! I Am Learning Python.

# print(s.count("h", 1, -2))
# print(s.lower().count("w"))  # "hello, world! i am learning python.".count("w")

# print(s.find("Python"))

# st = input("Введите два слова через пробел: ")
#
# first = st[:st.find(" ")]
# second = st[st.find(" ") + 1:]
# print(second + " " + first)

# print(s.find("e"))
# print(s.index("e"))
# print(s.rfind("e"))
# print(s.rindex("e"))

# print(s.endswith("on."))
# print(s.startswith("hel"))


# num = input("Введите число: ")
# if num.isdigit():
#     print(int(num) - 6)
# else:
#     print(num * 2)

# print('aBc123'.isalnum())  # наличие букв и цифр
# print("123".isdigit())  # наличие цифр
# print("%:?".isalnum())  # строка не пустая (присутствуют буквы или цифры)
# print("abc5#$".islower())  # наличие букв в нижнем регистре (могут присутствовать буквы и спецсимволы)
# print("AsE5#$".isupper())  # наличие букв в верхнем регистре (могут присутствовать буквы и спецсимволы)


# print("py".center(10, "-"))
# print("py".center(2))


# print("    p     y    ".lstrip())
# print("py    ".rstrip())
# print("      py    ".strip())
#
# print("http://www.python.org.ru".lstrip("/:pthsru"))
# print("http://www.python.org.ru".strip("/:pthsru"))


# def changeCharToStr(s, c_old, c_new):
#     s2 = ""  # "Я изучаю Python. Мне нравится "
#     i = 0
#
#     while i < len(s):
#         if s[i] == c_old:
#             s2 = s2 + c_new
#         else:
#             s2 = s2 + s[i]
#         i = i + 1
#
#     return s2
#
#
# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования. New"
# str2 = changeCharToStr(str1, "N", "P")
# # str2 = str1.replace("Nython", "Python")
# print("str1 =", str1)
# print("str2 =", str2)

# s = "-"
# seq = ('a', 'b', 'c')
# print(s.join(seq))
#
# print("..".join(['1', '2', '3']))
#
# lst = [3, 4, 6, 7]
#
# a = "_".join(map(str, lst))
#
# print(a)  # "3_4_6_7"
#
# print(a.split("_"))
#
#
# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования. New"
# print(str1.split())

# num = input("Введите числа для нахождения суммы через пробелов: ").split()
# # num = list(map(int, num))
# # print(sum(num))
#
# print(sum(map(int, num)))

# a = "Никонов Валерий Анатольевич"  # Никонов В.А.
# lst = a.split()
# print(lst)
# print(f"{lst[0]} {lst[1][0]}.{lst[2][0]}.")

import re

# s = "Я ищу совпадения в 2025 году. И я их найду в 2 счёта."
# reg = r"\."
#
# print(re.findall(reg, s))
# print(re.search(reg, s))
# print(re.search(reg, s).span())
# print(re.search(reg, s).start())
# print(re.search(reg, s).end())
# print(re.search(reg, s).group())
# print(re.split(reg, s))
# print(re.sub(reg, "!", s))

# s = "Я ищу совпадения в 2025 году. И я их найду в 2 счёта. 6789  Hello_World ели[-ели] 20000000"
# # reg = r"[205]"
# # reg = r"[12][0-9][0-9][0-9]"
# # reg = r"[А-Яа-яЁё]"
# # reg = r"[А-яЁё]"
# # reg = r"[A-Za-z]"
# # reg = r"\."
# # reg = r"[А-яёЁ.\]\[-]"
# # reg = r"[^0-9]"
# # reg = r"[^А-яЁёA-Za-z]"
# # reg = r"\d"
# # reg = r"\D"
# # reg = r"\w"
# # reg = r"\W"
# # reg = r"\s"
# # reg = r"\S"
# # reg = r"\w+"
# # reg = r"20*"
# # reg = r"^\w+\s+\w+"
# # reg = r"\d+$"
# # print(re.findall(reg, s))
#
# # Кол-во повторений
# # + - от 1 до бесконечности повторений
# # * - от 0 до бесконечности повторений
# # ? - от 0 до 1 повторения
#
#
# # st = "24-часовой формат 21:59"
# #
# # reg = "[0-2][0-9]:[0-5][0-9]"  # 0 [0-9]   1 [0-9]  2 [0-9] 3 [0-9] 4 [0-9] 5 [0-9]
# # print(re.findall(reg, st))
#
#
# # d = "Цифры: 7, ++17, -42, 0012, 0.3"
# # print(re.findall(r"[+-]?[\d.]+", d))
#
# # d = "05-03-1987 # Дата рождения"
# # print("Дата рождения:", re.sub(r"\s#.*", "", d))
# # print(re.sub(r"-", ".", d))
# #
# # print("Дата рождения:", re.sub(r"\s#.*", "", re.sub(r"-", ".", d)))
#
# # st = "author=Пушкин А.C.; title  = Евгений Онегин; price =200; year= 1831"
# # # req = r"\w+\s*=\s*[\w\s.]+"
# # req = r"\w+\s*=[^;]+"
# # print(re.findall(req, st))
#
# # st = "12 сентября 2025 года 235 456789654"
# # req = r"\d{,4}"  # {4} {2,4} {2,}
# # print(re.findall(req, st))
#
#
# # def validate_name(name):
# #     return re.findall(r"^[A-Za-z0-9_-]{3,16}$", name)
# #
# #
# # print(validate_name("Python_master"))
# # print(validate_name("Pyfgfgdt"))
#
#
# # text = "<body>Пример жадного соответствия регулярных выражений</body>"
# # print(re.findall('<.*?>', text))
# #
# # # *?, +?, ??
# # # {n, m}?, {n,}?, {,m}?
# #
# #
# # st = "12 сентября 2025 года 235 456789654"
# # req = r"\d{2,4}?"  # {4} {2,4} {2,}
# # print(re.findall(req, st))
#
# # st = "Петр, Ольга и Виталий отлично учатся!"
# # req = "Петр|Ольга|Марина"
# # print(re.findall(req, st))
#
# # st = "int = 4, float = 4.0f, double = 8.0, int"
# # # req = r"int\s*=\s*\d[.\w]*|float\s*=\s*\d[.\w]*"
# # # req = r"(?:int|float)\s*=\s*\d[.\w]*"
# # req = r"(int|float)\s*=\s*(\d[.\w]*)"
# # print(re.findall(req, st))
#
#
# # st = "Word2016, PS6, AI5"
# # req = r'([A-Za-z]+)(\d+)'
# # print(re.findall(req, st))
#
#
# # st = "5 + 7*2 - 4"
# # req = r'\s*([+*-])\s*'
# # print(re.split(req, st))
#
#
# # dd-mm-YYYY    3 от 01 по 31
#
# # a = "22-01-2025"
# # pattern = r"(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(19[0-9][0-9]|20[0-9][0-9])"
# # print(re.findall(pattern, a))
# reg = r"([0-9]+)\s(\D+)"
# print(re.findall(reg, s))
# print(re.search(reg, s).group())

# m = re.search(reg, s)
# print(m[0])
# print(m[1])
# print(m[2])

# s = "Самолет прилетает 10/23/2026. Будет рады вас видеть после 10/24/2026."
# reg = r"(\d{2})/(\d{2})/(\d{4})"
# print(re.sub(reg, r'\2.\1.\3', s))


# 10/23/2026 => 23.10.2026


# s = "yandex.com and yandex.ru"
# req = r"(([a-z0-9-]{2,}\.)+[a-z]{2,4})"
# print(re.sub(req, r"http://\1", s))


# Рекурсия

# def elevator(n):  # 0
#     if n == 0:
#         print("Вы в подвале")
#         return
#     # print("=>", n)  # стек: 5 4 3 2 1
#     elevator(n - 1)
#     print(n, end=" ")
#
#
# n1 = int(input("На каком вы этаже: "))
# elevator(n1)


# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res += i
#     return res

# def sum_list(lst):  # [9]
#     if len(lst) == 1:
#         return lst[0]  # 9
#     else:
#         return lst[0] + sum_list(lst[1:])  # 1 3 5 7
#
#
# print(sum_list([1, 3, 5, 7, 9]))  # 25


# def to_str(n, base):  # n = 15, base = 16
#     convert = "0123456789ABCDEF"
#     if n < base:  # 15 < 16
#         return convert[n]  # "F"
#     else:
#         return to_str(n // base, base) + convert[n % base]  # "E"
#
#
# print(to_str(254, 2))


# names = ["Adam", ["Bob", ["Chet", "Cat"], "Bard", "Bert"], "Alex", ["Bea", "Bill"], "Anna"]


# print(len(names))
# print(names[1])
# print(isinstance(names[1], list))
# print(names[1][1])
# print(isinstance(names[1][1], list))
# print(names[1][1][0])
# print(isinstance(names[1][1][0], list))
#
# def count_item(item_list):  #
#     count = 0  # 10
#     for item in item_list:  # ["Adam", ["Bob", ["Chet", "Cat"], "Bard", "Bert"], "Alex", ["Bea", "Bill"], "Anna"]
#         if isinstance(item, list):
#             count += count_item(item)
#         else:
#             count += 1
#
#     return count
#
#
# print(count_item(names))


# names = ["Adam", ["Bob", ["Chet", "Cat"], "Bard", "Bert"], "Alex", ["Bea", "Bill"], "Anna"]
#
#
# # names_new = names.copy()
# # ind = -1
# # while ind != 0:
# #     ind = 0
# #     temp_list = []
# #     for i in names_new:
# #         if isinstance(i, list):
# #             temp_list.extend(i)
# #             ind += 1
# #         else:
# #             temp_list.append(i)
# #
# #     names_new = temp_list
# #
# # print(names_new)
#
# def union(s):
#     if not s:  # s == []
#         return s
#     if isinstance(s[0], list):
#         return union(s[0]) + union(s[1:])
#     return s[:1] + union(s[1:])
#
#
# print(union(names))

# f = open("text.txt", "r")
# # f = open(r"D:\PythonBase\text.txt", "r", encoding="utf-8")
# print(f)
# print(*f)
# print(f.encoding)
# f.close()


# f = open("text.txt", "r")
# print(f.read(3))
# print(f.read())
# f.close()


# f = open("test.txt", "r")
# print(f.readline())
# print(f.readline(8))
# print(f.readline())
# print(f.readline())
# f.close()

# f = open("test.txt", "r")
# print(f.readlines(16))
# print(f.readlines())
# f.close()

# f = open("test.txt", "r")
# count = 0
# for line in f:
#     print(line)
#     count += 1
# f.close()
#
# print(count)


# f = open("test.txt", "r")
# print(len(f.readlines()))
# f.close()

#
# f = open("xyz1.txt", "a")
# # f.write("Hello\nWorld\n")
# f.write("New text.")
# f.close()


# lines = ["This is line 1\n", "This is line 2\n", "This is line 3\n",]
#
# f = open("first.txt", "a")
# f.writelines(lines)
# f.close()

# f = open("first.txt", "w")
# lst = [str(i) for i in range(1, 20)]
# print(lst)
# for index in lst:
#     f.write(index + "\t")
# f.close()

# f = open("text2.txt", "w")
# f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;")
# f.close()
#
#
# f = open("text2.txt", "r")
# read_file = f.readlines()
# f.close()
#
# print(read_file)
# read_file[1] = "Hello World!\n"
# print(read_file)
#
# f = open("text2.txt", "w")
# f.writelines(read_file)
# f.close()

# f = open("text.txt", "r")
# print(f.read(3))
# print(f.tell())
# print(f.seek(1))
# print(f.read())
# print(f.tell())
# f.close()

# f = open("text3.txt", "a+")
# print(f.write("I am learning Python"))
# # print(f.seek(3))
# # print(f.write("-new string-"))
# # print(f.tell())
# # print(f.write("NEW"))
# print(f.read())
# f.close()


# with open("text.txt", "w") as f:
#     print(f.write("0123456789"))
# print(f.closed)


# with open("text.txt", "r") as f:
#     for line in f:
#         print(line[:6])


# file_name = "res_1.txt"
# lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.777]
#
#
# def get_line(lt):
#     lt = list(map(str, lt))
#     return " ".join(lt)
#
#
# with open(file_name, 'w') as f:
#     f.write(get_line(lst))
#
# print("Done!")


# file_name = "res_1.txt"
#
#
# with open(file_name, 'r') as f:
#     num = f.read()
#
#
# num_list = list(map(float, num.split()))
# print(num_list)
# print(sum(num_list))

# file_name = "res_2.txt"

# with open(file_name, "w") as f:
#     f.write("Файл (англ. file) — абстракция операционной системы, представляющая собой набор данных, связанный в единое целое, доступ к которому осуществляется средствами файловых API.")


# def longest_worlds(file):
#     with open(file, "r") as text:
#         w = text.read().split()
#         print(w)
#         max_length = len(max(w, key=len))
#         print(max_length)
#         res = [word for word in w if len(word) == max_length]
#         if len(res) == 1:
#             return res[0]
#         return res
#
#
# print(longest_worlds(file_name))


# text = "Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\nСтрока №8\nСтрока №9\nСтрока №10\n"
# with open('open.txt', 'w') as f:
#     f.write(text)

# with open("open.txt", "r") as fr, open("two.txt", "w") as fw:
#     for line in fr:
#         line = line.replace("Строка", "Линия -")
#         fw.write(line)

# import os


# print(os.getcwd())
# print(os.listdir())
# print(os.listdir(".venv"))

# os.mkdir("folder/fn1")
# os.makedirs("nested1/nested2/nested3")
# os.rmdir("nested1")
# os.remove("xyz1.txt")

# os.rename("xyz.txt", "test/xyz2.txt")
# os.renames("two.txt", "text/two.txt")

# for root, dirs, files in os.walk("test", topdown=False):
#     print("Root:", root)
#     print("Dirs:", dirs)
#     print("Files:", files)

# def remove_empty_dirs(root_tree):
#     print(f"Удаление пустых директорий в ветви {root_tree}")
#     print("-" * 50)
#     for root, dirs, files in os.walk(root_tree):
#         if not os.listdir(root):
#             os.rmdir(root)
#             print(f"Директория {root} удалена.")
#     print("-" * 50)
#
#
# remove_empty_dirs("test")


# import os.path
# import time

# print(os.path.split(r"D:\PythonBase\test\nested2\nested3\test.txt"))
#
# print(os.path.join(r"D:\PythonBase", "test", "nested2", "nested3", "test.txt"))
#
# print(os.path.exists(r"D:\PythonBase\test\nested2\nested3\test.txt"))
#
# print(os.path.isfile(r"D:\PythonBase\test\nested2\nested3\test.txt"))
# print(os.path.isdir(r"D:\PythonBase\test\nested2\nested3"))
#
# print(os.path.getsize("main.py") / 1024)
#
# path = "main.py"
#
# print(os.path.getctime(path))  # время последнего изменения файла (сек) или время создания файла
# print(os.path.getatime(path))  # время последнего доступа к файлу (сек)
# print(os.path.getmtime(path))  # время последнего изменения файла (сек)
#
#
# print(time.strftime("%d.%m.%Y", time.localtime(os.path.getctime(path))))
# print(time.strftime("%d.%m.%Y", time.localtime(os.path.getatime(path))))
# print(time.strftime("%d.%m.%Y", time.localtime(os.path.getmtime(path))))


# import os
#
# dirs = [r'Work\F1', r'Work\F2\F21']

# for d in dirs:
#     os.makedirs(d)

# files = {
#     'Work': ['w.txt'],
#     r'Work\F1': ['f11.txt', 'f12.txt', 'f13.txt'],
#     r'Work\F2\F21': ['f211.txt', 'f212.txt']
# }
#
# for d, f in files.items():
#     for file in f:
#         file_path = os.path.join(d, file)
#         open(file_path, 'w').close()
#
#
# file_with_text = [r'Work\w.txt', r'Work\F1\f12.txt', r'Work\F2\F21\f211.txt', r'Work\F2\F21\f212.txt']
#
# for file in file_with_text:
#     with open(file, 'w') as f:
#         f.write(f"Какой-то текст для файла {file}")
#
#
# def print_tree(root, topdown):
#     print(f"Обход {root} {'сверху вниз' if topdown else 'снизу вверх'}")
#     for root, dirs, files in os.walk(root, topdown):
#         print(root)
#         print(dirs)
#         print(files)
#     print("-" * 50)
#
#
# print_tree("Work", False)
# print_tree("Work", True)

# Work\w.txt
# Work\F1\f11.txt
# Work\F1\f12.txt
# Work\F1\f13.txt
# Work\F2\F21\f211.txt
# Work\F2\F21\f212.txt

# print("Вносим изменения")


print("Новые изменения")
