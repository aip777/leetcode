
def move_number(data:list, target:int)->list:
    non_zero = [i for i in data if i !=target]
    zeros = len(data) - len(non_zero)
    result = [target] * zeros
    return non_zero + result

data = [0, 1, 1,1,1,1, 0, 3, 12]
target = 0
print(move_number(data, target))
