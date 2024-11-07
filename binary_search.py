def binary_search(arr,x):
    arr = sorted(arr)
    _low = 0
    _height = len(arr)-1
    _mid = 0
    while _low <= _height:
        mid = (_height+_low)//2
        if arr[mid]<x:
            _low = mid + 1
        elif arr[mid]>x:
            _height = mid - 1
        else:
            index = [mid]
            return arr[mid], index
    return -1

arr = [1, 2, 3, 4,5, 8, 9,10,11,12]
x = 11
result = binary_search(arr, x)
print(result)