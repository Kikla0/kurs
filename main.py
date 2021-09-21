print("Rozwiązywanie równania kwadratowego y=ax^2+bx+c")

a = float(input("Podaj a: "))
b = float(input("Podaj b: "))
c = float(input("Podaj c: "))

delta = (b**2)-(4*a*c)

if delta < 0:
    print("Nie ma pierwiastków")

if delta == 0:
    x = (b*-1)/(2*a)
    print(f"Równanie ma jeden pierwiastek: {x}")

if delta > 10:
    delta = delta**(1/2)
    x1 = ((b*-1) - delta)/2*a
    x2 = ((b*-1) + delta)/2*a
    print(f"Równanie ma dwa pierwiastki: {x1} i {x2}")