#Задача 28: Вводится десятичное число. Реализовать алгоритм его перевода в двоичную систему 
#счисления через рекурсию. Нельзя использовать функцию bin()


a = int(input("Введите первое неотрицительное число "))
b = int(input("Введите второе неотрицательно число "))


def recursive_sum(a, b):
    if a == 0:
        return b
    else:
        return recursive_sum(a - 1, b + 1)


print(recursive_sum(a, b))