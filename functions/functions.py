def a():
    pass

print(a())

def b():
    return 2, 3, 4

x, y ,z = b()

print(x, y, z)
print(b()[1])

def c(a, b= 5):
    return a*b

print(c(10, 20))

def d(text: str) -> str:
    return text

print(d('abc'))

def e(*args):
    for arg in args:
        print(arg)

e(1, 2, 3, 'a', 'b', 'c', ['1', '2', '3'])

def f(**kwargs):
    result = 0
    for kwarg in kwargs:
        result += kwargs[kwarg]
    print(result)

f(v=2, c=4, x=5)

def g(*args, **kwargs):
    result = 0
    for arg in args:
        result += arg
    for key in kwargs:
        result += kwargs[key]
    return result

print(g(1, 2, 3, 4, f=5))