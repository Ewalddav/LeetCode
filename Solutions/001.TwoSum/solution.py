'''
    David Ewald 8/29/21
    001 Two Sum : Easy

    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.

'''

from typing import List

class Solution:
    '''
        Using 2 pointers, 1 infront of the other to check sum of two pointer value
    '''
    def twoSumSlow(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j
        return []

    '''
        Using Hashmap to store previous values to indexes, checking target to current value
    '''
    def twoSumFast(self, nums: List[int], target: int) -> List[int]:
        previousNums = {}
        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in previousNums:
                return i, previousNums[dif]
            else:
                previousNums[nums[i]] = i
        return []
