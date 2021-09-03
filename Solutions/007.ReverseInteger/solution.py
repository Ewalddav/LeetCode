'''
    David Ewald 9/3/21
    007 Reverse Integer: Easy

    Given a signed 32-bit integer x, return x with its digits reversed. 
    If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

    Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

'''

class Solution:
    '''
        This could probably be faster if we popped off the integers without string conversion
        Note: We can check bit integer range using '-1 << 31 and 1 << 31'
    '''
    def reverse(self, x: int) -> int:
        num = str(abs(x))
        if x < 0:
            num = num[::-1]
            x = int('-' + num)
        else:
            num = num[::-1]
            x = int(num)

        if x not in range((-1 << 31), (1 << 31) - 1):
            return 0
        
        return x
