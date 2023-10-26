#Задача1
#Пользователь вводит число N, программа возвращает N-ный член последовательности Фибоначчи.
# Числа Фиббоначи: первые два члена 1 и 1.
# Каждый следующий член - сумма двух предыдущих.
number = int(input("Введите число N: "))
a, b = 1, 1
if number == 1:
    print(a)
elif number == 2:
    print(b)
else:
    for i in range(3, number + 1):
        a, b = b, a + b
print(b)

#Задача2
#Пользователь вводит число, программа проверяет, является ли оно простым.
number = int(input())
count = 0
for i in range(1,number+1):
    if number%i == 0:
        count += 1
if count > 2:
    print('Число составное')
else:
    print('число простое')

#Задача3
#Программа возвращает простые делители введенного числа, или сообщает, что оно простое.
num = int(input())
l = []
for i in range(1,num+1):
    if num%i == 0:
        l.append(i)
if len(l)>2:
    print('Делители числа:', l)
else:
    print('число простое')

#Задача4
#Программа находит наибольший общий делитель для двух введенных чисел.
num1 = int(input())
num2 = int(input())
l = []
for i in range(1,(num1*num2)+1):
    if num1%i == 0 and num2%i == 0:
        l.append(i)
print(max(l))

#Задача5
#Программа запрашивает число, а затем выводит квадрат из *, где длина стороны равна данному числу.
n=int(input())
for i in range(n):
    print(n*'*')

#Задача6
#Программа запрашивает два числа, а затем выводит прямоугольник из *, где длины сторон равны данным числам.
num1 = int(input())
num2 = int(input())
for i in range(num2):
    print(num1*'*')

#Задача7
#Программа запрашивает два числа и выводит на экран прямоугольник, в котором змейкой по вертикали записаны числа, начиная с 1.
length = int(input("Введите длину: "))
height = int(input("Введите высоту: "))

number = 1
step = 1

for i in range(height):
    for j in range(length):
        print(number, end=" ")
        number += step
    print()