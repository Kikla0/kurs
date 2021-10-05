with open('text.txt') as file:
    for line in file.readlines():
        date, value = line.replace('\n', '').split(',')
        print(date, value)
    
with open('text2.txt', 'r') as file:
    file.write(f'{date}, {value}')