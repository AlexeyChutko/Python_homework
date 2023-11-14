#Problem1
#Используя наборы символов из пакета string написать функцию,
# которая получает на вход строку и возвращает строку,
# в которой все буквы латинского алфавита из исходной строки преобразованы в заглавные символы.
# Использовать функции стандартной библиотеки upper() и find() нельзя.

def LetterIncreaser():
    import string
    letters = list(string.ascii_lowercase)
    bigletters = string.ascii_uppercase
    newstr = []
    stroka = input()
    i = 0
    while i < len(stroka):
        if stroka[i] in letters:
            ind = letters.index(stroka[i])
            newstr.append(bigletters[ind])
            i += 1
        else:
            newstr.append(stroka[i])
            i += 1
    print(''.join(newstr))

LetterIncreaser()

#Problem2
#Добавить к предыдущему заданию функцию с преобразованием всех символов в прописные и функцию с отражением
# (все заглавные становятся прописными и наоборот),
# минимально дублируя код. Использовать функции стандартной библиотеки lower() и find() нельзя.

def LetterIncreaserOrDecreaser():
    import string
    letters = list(string.ascii_lowercase)
    bigletters = list(string.ascii_uppercase)
    newstr = []
    stroka = input()
    i = 0
    while i < len(stroka):
        if stroka[i] in letters:
            ind1 = letters.index(stroka[i])
            newstr.append(bigletters[ind1])
            i += 1
        elif stroka[i] in bigletters:
            ind2 = bigletters.index(stroka[i])
            newstr.append(letters[ind2])
            i += 1
        else:
            newstr.append(stroka[i])
            i += 1

    print(''.join(newstr))


LetterIncreaserOrDecreaser()


#Написать программу на Python3, которая сначала запрашивает положительное число-основание системы счисления,
# затем два числа в системе счисления с этим основанием,
# и потом четвертое число-основание системы счисления, в которой надо вывести результат.
# В ходе выполнения программа возвращает результат сложения двух чисел в требуемой системе счисления.
# Нельзя использовать для перевода функцию int().
