def div(a,b):
    return a/b

def outer(func):
    def inner(a,b):
        if b>a:
            a,b=b,a
        return func(a,b)
    return inner

div = outer(div)

print(div(2,4))