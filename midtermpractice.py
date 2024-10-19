a = 10

def f():
    a = 1
    return a * 1000

def g():
    b = a
    return b

k = f() + g()
print(a * k)

