#Task1
name = input('Имя')
age = input('Возраст')
gender = input('Пол')
company = input('Работа')
maritalStatus = input('Семейное положение')
address = input('Где проживаете')
# Task1,4
print('Длина имени', len(name[1:]))
# Task2
if 'a' in company:
    print('Это буква есть в слове')
if 'a' not in company:
    print('Этой буквы нет в слове')
#Task3
print('2 индекс:' + address[2])
#Task5
print('обратный порядок' + company[::-1])
#Task6
print('Имя:{0}\n Возраст:{1}\n Пол:{2}\n Работа:{3}\n '
      'Семейное положение: {4}\n'
      ' Где проживаете: {5}'.format(name,age,gender,company,maritalStatus,address))

#Task7

stix = """Белеет парус одинокой
          В тумане моря голубом!..
          Что ищет он в стране далекой? 
          Что кинул он в краю родном?..
          
          Играют волны — ветер свищет,
          И мачта гнется и скрыпит... 
          Увы! он счастия не ищет
          И не от счастия бежит!"""

print(stix)


