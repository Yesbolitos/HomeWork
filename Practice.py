'''numb = int(input('Введите число для факториала: '))
counter = 1
factNumber = 1
while counter <= numb:
    factNumber = factNumber * counter
    counter += 1

print(factNumber)

numb= int(input('Введите число для факториала: '))
fact=1
for counter in range(2,numb+1):
    fact=fact*counter
print(" факториал цифры  ",numb," это: ",fact)

n = 34
while n <= 67:
	if n % 2 != 1:
		print (n)
	n += 1

revers = list(range(13, 0, -1))
print(revers)

for x in reversed(range(1,14)):
    print(x)

i = 1
while i <= 20:
    print(i ** 2)
    i += 1'''

#Task 3
number = int(input('Введите число до которой необходимо вычислить сумму значений: '))

counter = 1
totalSum = 0
while counter <= number:
    totalSum = totalSum + counter
    #total += counter
    counter += 1

print(totalSum)

while number != 0:
    number = int(input(""))
    sum = sum + number
    count += 1

if count == 0:
    print("Input some numbers")
else:
    print("Average and Sum of the above numbers are: ", sum / (count - 1), sum)

#Task 4
n = 34
while n <= 67:
	if n % 2 != 1:
		print (n)
	n += 1








