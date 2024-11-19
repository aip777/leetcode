

def find_list_instance(data:dict)->list:
    data_list = []
    for item in data:
        if isinstance(data[item], list):
            data_list.append(data[item])
    return data_list

data = {'name':'khan', 'email':['ariful.i777@gmail.com','ariful.islam@gmail.com'], 'product_list':['books','pen']}
result = find_list_instance(data)
print(result)


d = [[]]*5
d[0].append(20)
d[1].append(30)
print(d)

