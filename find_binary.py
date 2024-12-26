
# Convert 25 to binary:
# 25÷2=12, remainder = 1
# 12÷2=6, remainder = 0
# 6÷2=3, remainder = 0
# 3÷2=1, remainder = 1
# 1÷2=0, remainder = 1

def find_binary(num):
    result = bin(num)[2:]
    return result

print(find_binary(25))
