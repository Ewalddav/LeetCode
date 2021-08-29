'''
    David Ewald 8/29/21
    003 Longest Substring Without Repeating Characters: Medium

    Given a string s, find the length of the longest substring without repeating characters.

'''

'''
    Using sliding window with 2 pointers, moving the left/slow pointer when we find dup and delete
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        left = 0
        result = 0

        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            result = max(result, right - left + 1)

        return result

