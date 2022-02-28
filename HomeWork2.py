# Task1
addWord = input('Введите слово')
print ('имя наоборот', ''+ addWord[:: -1])

# Task2
text = 'Я обучаюсь курсу Python Django'
print(len(text))
print(text[17:30])

# Task3
word1 = '$$$Python@@@'
word2 = '%%%Programming'
word3 = 'City&&&'
word4 = '****Computer***'

left= word1.strip('$')
print(left)
right= word1.strip('@')
print(right)
atBothSides= word1.strip('$'+'@')
print(atBothSides)

left= word2.strip('%')
print(left)

right = word3.strip('&')
print(right)

atBothSides= word4.strip('*')
print(atBothSides)


#Task4
# .format
Number = input('Введите число')
Color = input('Ваш Любимый цвет')
City =  input('Любимый город')
food = input('Любимая еда')

print('Цифра: {0}  Цвет: {1}  Город: {2}  Еда: {3}'.format(Number,Color,City,food))

# F-string
print(f'Введите число: {Number}\nВаш Любимый цвет: {Color}\nЛюбимый город: {City}\nЛюбимая еда: {food}')




