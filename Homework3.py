# Task 1
Number = int(input('Введите число'))
if Number >= 2 and Number <= 9:
    print('Число больше 2 и меньше 9')
else:
    print('Неизвестное число')


#Task 2

weight = int(input('Введите вес'))
if weight >= 0 and weight <= 2:
    print('Посылка будет отправление тарифом 3.5 долларов за кг')
elif weight >= 3 and weight <=5:
    print('Посылка будет отправление тарифом 5.5 долларов за кг')
elif weight >= 6 and weight <= 10:
    print('Посылка будет отправление тарифом 7 долларов за кг')
elif weight >= 10 and weight <= 50:
    print('Посылка будет отправление тарифом 10 долларов за кг')
else:
    print('Посылка не может быть отправлена')

# Task 3

addNumber = int(input('Введите число'))
if addNumber % 2 == 0:
    print('Число четное')
else:
    print('Ваше число нечетное, перезапустите программу')

