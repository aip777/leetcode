# Input: [1, 20, 3, 4, 5]
# Output: 100
from copy import deepcopy


def max_num(n:list)->list:
    _list = []
    for i in n:
        p = deepcopy(n)
        p.remove(i)
        for m in p:
            _list.append(i*m)
    print(_list)
    return max(_list)
n = [1, 20, 3, 4, 5]
result = max_num(n)
print(result)

def max_product(arr: list) -> int:
    arr.sort()
    return max(arr[0] * arr[1], arr[-1] * arr[-2])
print(max_product([1, 20, 3, 4, 5,6,66,5]))