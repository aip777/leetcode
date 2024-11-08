class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1
        is_negative = x < 0
        x = abs(x)

        reversed_num = 0
        while x > 0:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10

        if is_negative:
            reversed_num = -reversed_num

        if reversed_num < INT_MIN or reversed_num > INT_MAX:
            return 0

        return reversed_num
x = 123
result = Solution().reverse(x)
print(result)