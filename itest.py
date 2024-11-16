string_valu = 'Hello how are you doing'
result = " ".join(string_valu.split()[::-1])
print(result)

my_list = [1,2,3,4,5,6,7,8,9,10,11,12,12,11,1,2,3,4,5,6,7,8]
new_list = []
for i in my_list:
    if my_list.count(i) == 1:
        new_list.append(i)
print(new_list)
from collections import Counter
my_str = 'a,a,a,b,c,d,d,b,f'
result = Counter(my_str).pop(',')
result.pop(",")
print(result)

