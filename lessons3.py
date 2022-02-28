#Task 1
NumOne = int(input('add First Number'))
NumTwo = int(input('add Second Number'))

if NumOne == NumTwo:
    print('Введенные цифры равноы между собой')
elif NumOne >= NumTwo:
    print('Первая цифра больше или равно к второй цифре')
else:
    print('Первая цифра меньше чем второй')

print('1.Сложение \n2.Вычитание \n3.Умножение')
fo = int(input('Номер операции'))
if fo == 1:
    print('Сложение', NumOne + NumTwo)
elif fo == 2:
    print('Вычитание', NumOne - NumTwo)
elif fo == 3:
    print('Умножение', NumOne * NumTwo)


addNumber = int(input('Введите число'))
if addNumber % 2 == 0:
    print('Число четное')
else:
    print('Число нечетное')







