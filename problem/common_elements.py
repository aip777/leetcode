def common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))

lst1 = [2,34,5,6]
lst2 = [2,3,4,5,1]
print("Common elements:", common_elements(lst1, lst2))

