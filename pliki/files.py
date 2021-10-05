'''
open() - otwieranie pliku
r - odczyt
w - zapis
x - tworzenie
a - dopisywanie
b - binarny
t - tekstowy
+
.close - zamknięcie pliku 
'''
# sposób niezalecany

f = open('file.txt')
lines = f.readlines() # lista linii
for line in lines:
    print(line)
f.close()

# sposób zalecany

with open('file.txt') as f:
    while True:
        line = f.readline() # czyta jedną linię
        if not line:
            break
        print(line)

with open('file.txt', 'w') as f:
    for i in range(10):
        f.write(f"To jest linia numer: {i}\n") # zapisywanie