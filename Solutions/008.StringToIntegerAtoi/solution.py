'''
    David Ewald 9/3/21
    008 String to Integer (Atoi): Medium

    Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

    The algorithm for myAtoi(string s) is as follows:

    Read in and ignore any leading whitespace.
    Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
    Read in next the characters until the next non-digit charcter or the end of the input is reached. The rest of the string is ignored.
    Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
    If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
    Return the integer as the final result.
    Note:

    Only the space character ' ' is considered a whitespace character.
    Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.

'''

class Solution:
    '''
        This works but seems to be sorta slow and uses more memory than most other solutions, could probably recursion this one
        after we deal with the whitespace and  +/-
    '''
    def myAtoi(self, s: str) -> int:
        cleanString = s.strip()
        num = 0
        positive = True
        if not cleanString:
            return num
        else:
            if cleanString[0] == '-':
                cleanString = cleanString[1:]
                positive = False
            elif cleanString[0] == '+':
                cleanString = cleanString[1:]
                positive = True
            else:
                num = 0

        i = 0
        while i < len(cleanString) and cleanString[i].isnumeric():
            i += 1

        if i <= 0:
            return num

        if positive:
            num = int(cleanString[:i])
        else:
            num = int('-' + cleanString[:i])
        
        if num > (1 << 31) - 1:
            return (1 << 31) - 1
        elif num < (-1 << 31):
            return (-1 << 31)
        else:
            return num
