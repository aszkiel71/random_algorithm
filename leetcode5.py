#https://leetcode.com/problems/longest-palindromic-substring/


def longestPalindrome(s):
    def subset(L):
        n = len(s)
        result = set()
        for i in range(n):
            for j in range(i+1, n+1):
                result.add(s[i:j])
        return result

    max_len = -1
    tmp_res = ''
    print(subset(s))
    for i in subset(s):
        if len(i) > max_len and i == i[::-1]:
            max_len = len(i)
            tmp_res = i
    return tmp_res

print(longestPalindrome("babad"))

# good tho t.c. is O(n^3)
# another version:

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        start, max_len = 0, 0
        def expand_from_center(left: int, right: int):
            nonlocal start, max_len
            while left >= 0 and right < len(s) and s[left] == s[right]:
                current_len = right - left + 1
                if current_len > max_len:
                    start, max_len = left, current_len
                left -= 1
                right += 1

        for i in range(len(s)):
            expand_from_center(i, i)
            expand_from_center(i, i + 1)

        return s[start:start + max_len]
