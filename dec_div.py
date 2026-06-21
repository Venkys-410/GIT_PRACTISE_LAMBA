

def wrap(func):
    def inner(a,b):
        if b == 0:
            a,b = b,a
        return func(a,b)
    return inner

@wrap
def div(a,b):
    return a/b

x = div(18,6)

print(x)
print('Hello World')