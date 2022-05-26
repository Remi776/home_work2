# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
#Второй замечательный предел !

number = int(input('Enter the number: '))
result = {i: (1 + 1/i)**i for i in range(1, number + 1)}
print(result)