from collections import Counter

def first_non_repeated(s: str) -> str:
    count = Counter(s)
    for char in s:
        if count[char] == 1:
            return char
    return None

def easy_way(s:str)->str:
    count = Counter(s)
    return min(count.keys())
print(first_non_repeated("swiss"))
print(easy_way("swiss"))
