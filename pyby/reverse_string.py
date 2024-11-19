
def reverse_string():
    name = input("Enter your name: ")
    reverse_string = ''
    length = len(name)

    while length>0:
        reverse_string += name[length-1]
        length -= 1
    return reverse_string

# result = reverse_string()
# print(result)

# optimize
def reverse_string_main()->str:
    name = input("Enter your name: ")
    r_sting = ''
    for i in name:
        r_sting = i + r_sting
    return r_sting

# result = reverse_string_main()
# print(result)


# more optimize
def reverse_string_main()->str:
    name = input("Enter your name: ")
    return name[::-1]

result = reverse_string_main()
print(result)
