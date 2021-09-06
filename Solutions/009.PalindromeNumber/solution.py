'''
    David Ewald 9/6/21
    009 Palindrome Number: Easy

    Given an integer x, return true if x is palindrome integer.

    An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

'''

class Solution:
    '''
        I like this because it is a clean 1 liner and it works.
        However this converts to string, would like another solution with no string conversion
    '''
    def isPalindrome(self, x: int) -> bool:
        return True if str(x) == str(x)[::-1] else False
        