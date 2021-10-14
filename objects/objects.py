# definicja klasy
class Animal:
    NAME = "" # zmienna klasowa
    AGE = 0 # zmienna klasowa

    def __init__(self): # "konstruktor"
        self.name = "John" # ustawienie domyślnej wartości
        self.age = 2
    
    def print_details(self): # metoda wypisująca stan
        print(f"Imie: {self.name}, wiek: {self.age}")
'''
    def __init__(self, name='Rex', age=2): # "konstruktor"
        self.name = name # ustawienie domyślnej wartości
        self.age = age

my_cat = Animal('Bonifacy', 4)

    def __init__(self, name='Rex', age=2):"
        self._name = name # pola chronione
        self._age = age
    
    def __init__(self, name='Rex', age=2): # "konstruktor"
        self.__name = name # pola prywatne
        self.__age = age
'''

# tworzenie obiektu
my_dog = Animal() # tworzenie obiekty
my_dog.print_details() # uruchomienie metody print_details
print(my_dog.name) # dostęp do pola name obiektu  my_dog
my_dog.age = 3 # aktualizacja pola age obiektu my_dog

# dziedziczenie i polimorfizm

# dziedziczenie
class A:
    LICZBA = 20
    def a(self):
        print(self.LICZBA)

class B(A):
    pass

b = B()

b.a()

# polimorfizm
class A:
    LICZBA = 20
    def a(self):
        print(self.LICZBA)

class B(A):
    def a(self):
        print("Metoda klasy B")

b = B()

print(b.LICZBA)

b.a()