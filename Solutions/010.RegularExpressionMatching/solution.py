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
        Magic, dynamic programming, still need to dig into this one more
    '''
    def isMatch(self, s: str, p: str) -> bool:
        boolMatrix = [[False for i in range(len(p) + 1)] for j in range(len(s) + 1)]

        boolMatrix[0][0] = True

        for j in range(1, len(boolMatrix[0])):
            if p[j - 1] == '*':
                boolMatrix[0][j] = boolMatrix[0][j - 2]

        for i in range(1, len(boolMatrix)):
            for j in range(1, len(boolMatrix[i])):
                if p[j - 1] == '*':
                    boolMatrix[i][j] == boolMatrix[i][j - 2]

                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        boolMatrix[i][j] == boolMatrix[i][j] or boolMatrix[i - 1][j]
  
                elif p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    boolMatrix[i][j] = boolMatrix[i - 1][j - 1]

        return boolMatrix[-1][-1]

if __name__ == "__main__":
    sol = Solution()
    sol.isMatch('aa', 'a*')
