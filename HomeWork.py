#Task1
nameRe = input('addName')
force = 1
while force <= 20:
    print(force, nameRe)
    force = force + 1

#Task2
for i in range(1, 25, 3):
    num = i * 5
    print(f"{i} умножается на 5, результат {int(num)}.")

#Task3
myNumberList = [123,34,5,65]

counter = 0
#myNumberList[0]

while counter < len(myNumberList):
    print(myNumberList[counter] + 10)
    counter += 1 # counter  = counter + 1


# Task 4
word = input('Введите слово в котором надо удвоить буквы:')
for x in word:
    print(x * 2, end = '' )


