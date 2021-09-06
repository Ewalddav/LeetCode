'''
    David Ewald 9/6/21
    010 Regular Expression Matching: Hard

    Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

    '.' Matches any single character.​​​​
    '*' Matches zero or more of the preceding element.
    The matching should cover the entire input string (not partial).

'''

class Solution:
    '''
        Here we go!
    '''
    def isMatch(self, s: str, p: str) -> bool:
        