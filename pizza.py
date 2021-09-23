# import sys
import math

pi = math.pi

list = []
list.append(str(input("Podaj nazwę pizzerii: ")))

list.append(str(input("\nPodaj nazwę pierwszej pizzy: ")))
list.append(int(input("Podaj rozmiar pierwszej pizzy: ")))
list.append(float(input("Podaj cenę pierwszej pizzy: ")))
print("\nNazwa restauracji: {}, pizza: {}, rozmiar: {}, cena: {}\n".format(list[0], list[1], list[2], list[3]))

list.append(str(input("Podaj nazwę drugiej pizzy: ")))
list.append(int(input("Podaj rozmiar drugiej pizzy: ")))
list.append(float(input("Podaj cenę drugiej pizzy: ")))
print("Nazwa restauracji: {}, pizza: {}, rozmiar: {}, cena: {}\n".format(list[0], list[4], list[5], list[6]))

list.append(str(input("Podaj nazwę trzeciej pizzy: ")))
list.append(int(input("Podaj rozmiar trzeciej pizzy: ")))
list.append(float(input("Podaj cenę trzeciej pizzy: ")))
print("Nazwa restauracji: {}, pizza: {}, rozmiar: {}, cena: {}\n".format(list[0], list[7], list[8], list[9]))

ratio1 = list[3] / (pi * math.pow((list[2] / 2), 2))
ratio2 = list[6] / (pi * math.pow((list[5] / 2), 2))
ratio3 = list[9] / (pi * math.pow((list[8] / 2), 2))

min = min(ratio1, ratio2, ratio3)

if min == ratio1:
    print("Nazwa restauracji: {}, pizza: {}, rozmiar: {}, cena: {}".format(list[0], list[1], list[2], list[3]))
elif min == ratio2:
    print("Nazwa restauracji: {}, pizza: {}, rozmiar: {}, cena: {}".format(list[0], list[4], list[5], list[6]))
elif min == ratio3:
    print("Nazwa restauracji: {}, pizza: {}, rozmiar: {}, cena: {}".format(list[0], list[7], list[8], list[9]))
else:
    print("Error")