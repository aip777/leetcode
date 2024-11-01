# Example 1:
#
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:
#
# Input: s = "cbbd"
# Output: "bb"


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        _list = [*s]
        print(_list)
        _next = ''
        _previous = ''
        _length = len(s)
        _inx = 0
        result = ''
        for i in range(_length-1):
            _inx = i
            if _length>_inx:
                m = i+1
                _next = _list[m]
                print("_next", _next)
            if i>0:
                _previous = _list[i-1]
                print("_previous", _previous)
            if _next == _previous:
                result += _list[i]
                result += _next
        return result



# s = "babad"
# result = Solution().longestPalindrome(s)
# print(result)


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest_palindrome = ""
        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        for i in range(len(s)):
            odd_palindrome = expand_around_center(i, i)
            even_palindrome = expand_around_center(i, i + 1)
            longest_palindrome = max(longest_palindrome, odd_palindrome, even_palindrome, key=len)
        return longest_palindrome


s = "babad"
result = Solution().longestPalindrome(s)
print(result)

