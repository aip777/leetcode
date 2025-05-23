def fun(x):
    x[0] = 5
    return x

g = [10,11,12]
print(fun(g),g)