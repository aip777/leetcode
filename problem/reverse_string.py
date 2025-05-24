def reverse_string(s):
    reversed_str = ''
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

def reverse_string_tow(s):
    return s[::-1]

s = input("1. Enter a string to reverse: ")
print("Reversed string:", reverse_string(s))