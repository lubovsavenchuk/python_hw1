# Задача 1: Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

print('Введите цифру дня недели')
digit = int (input ())
if (digit <= 5):
   print('День рабочий')
elif (digit > 5 and digit <= 7):
   print('Выходной день')
else:
   print('Введено неверное значение')
