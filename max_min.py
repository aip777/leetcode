

def max_min(data:list)->list:
    max_num = data[0]
    min_num = data[0]
    for i in data:
        if i>max_num:
            max_num = i
        if i<min_num:
            min_num = i
    return [max_num, min_num]
data = [2,5,6,7,8,9,12,3,4,35,34,3,41,1,43,43,43,90,99]
print(max_min(data))
