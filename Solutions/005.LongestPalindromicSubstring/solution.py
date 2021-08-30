'''
    David Ewald 8/30/21
    005 Longest Palindromic Substring: Medium

    Given a string s, return the longest palindromic substring in s.

'''

class Solution:
    '''
        Brute force technique, should be O(n)^3, very slow
    '''
    def longestPalindromeSlow(self, s: str) -> str:
        j = 0
        longestPalindrone = ''
        while j in range(len(s)):
            i = j
            while i in range(len(s)):
                p = s[j:i+1]
                if p == p[::-1]:
                    if len(p) > len(longestPalindrone):
                        longestPalindrone = p
                i = i + 1
            j = j + 1
        
        return longestPalindrone

    '''
        Start from the middle, use 2 pointers, both stepping away from middle 1 space in both directions.
    '''
    def longestPalindromeFast(self, s: str) -> str:
        longestPalindrone = ''
        for i in range(len(s)):
            # Even Case
            l, r = i , i
            while (l >= 0 and r < len(s) and s[l] == s[r]):
                if (r - l + 1) > len(longestPalindrone):
                    longestPalindrone = s[l:r+1]
                l -= 1
                r += 1
            
            # Odd Case
            l, r = i , i + 1
            while (l >= 0 and r < len(s) and s[l] == s[r]):
                if (r - l + 1) > len(longestPalindrone):
                    longestPalindrone = s[l:r+1]
                l -= 1
                r += 1
            
        return longestPalindrone
  