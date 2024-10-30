# Example 1:
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:
#
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
#
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

#Not working
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        _dict = {}
        start = ''
        for i in s:
            if i not in _dict:
                _dict[i] = 1
            elif i == start:
                _dict[i] = 1
            start = i
        return len(_dict)
s = "abcabcbb"
s = "bbbbb"
s = "pwwkew"
result = Solution().lengthOfLongestSubstring(s)
print(result)

#Right answer
class Solution(object):
    def length_of_longest_substring(s):
        _dict = {}
        left = 0
        max_len = 0
        for right, char in enumerate(s):
            if char in _dict and _dict[char] >= left:
                left = _dict[char] + 1
            _dict[char] = right
            max_len = max(max_len, right - left + 1)
        return max_len












