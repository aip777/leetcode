def count_vowels(s):
    return sum(1 for char in s.lower() if char in 'aeiou')

s = input("5. Enter a string to count vowels: ")
print("Number of vowels:", count_vowels(s))