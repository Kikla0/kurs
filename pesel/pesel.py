pesel = input("Podaj numer z 10-ma cyframi: ")

numbers = []
weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
sum = 0

for digit in pesel:
    numbers.append(int(digit))

for i in range(len(numbers)):
    number = numbers[i] * weights[i]
    if number > 9:
        number = str(number)
        number = int(number[-1])
    numbers[i] = number

for i in range(len(numbers)):
    sum += numbers[i]

if sum > 9:
    sum = str(sum)
    sum = int(sum[-1])

checksum = 10 - sum
if checksum == 10:
    checksum = 0

pesel = pesel + str(checksum)

print(pesel)