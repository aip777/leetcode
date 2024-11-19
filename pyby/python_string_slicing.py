# input "A4BD37E"
# output "ABDE347"

def sorted_string():
    string = input("Enter your string: ")
    sorted_string = sorted(string)
    str_obj = ''
    number = ''
    for char in sorted_string:
        if char.isalpha():
            str_obj += char
        elif char.isnumeric():
            number += char
    return str_obj+number
print(sorted_string())
