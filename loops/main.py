print("Ładowarka paczek\n")

package_count = 1
package = 0
sent = 0
empty = 0
max_empty = 0
sum_empty = 0

error = 0

while True:
    mass = input("Podaj masę elementu: ")
    if mass == '':
        error = 0
        break
    if type(mass) != "int":
        error = 1
        break
    mass = int(mass)
    if mass <= 0 or mass > 10:
        error = 1
        break
    package += mass
    sent += mass
    if package > 20:
        package_count += 1
        package -= mass
        empty = 20 - package
        sum_empty += empty
        package = 0
        if empty > max_empty:
            max_empty = empty
    
if error == 1:
    print("Podano niewłaściwą masę elementu!")
elif error == 0:
    print(f"Liczba paczek: {package_count}\nSuma wysłanych kg: {sent}\nSuma pustych kg: {sum_empty}\nNajwięcej pustych kg w paczce: {max_empty}")
else:
    print("Błąd!")