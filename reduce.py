from functools import reduce

data = [1,2,3,4,5,6]
result = reduce(lambda x,y:x+y, data)
print(result)


def add(x:int,y:int)->int:
    return x+y
result = reduce(add, data)
print(result)
