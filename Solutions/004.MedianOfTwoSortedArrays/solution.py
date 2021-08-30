'''
    David Ewald 8/30/21
    004 Median of Two Sorted Arrays: Hard

    Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

    The overall run time complexity should be O(log (m+n)).

'''

from typing import List

class Solution:
    '''
        We first merge the two sorted arrays which in theory is O(n) or O(log(m+n)), seems to be some debate,
        then we pick median based on odd or even length or merge array
    '''
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mergeList = []
        i = 0
        j = 0
        k = 0
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                mergeList.append(nums1[i])
                i = i + 1
            else:
                mergeList.append(nums2[j])
                j = j + 1
            k = k + 1
        
        while i < len(nums1):
            mergeList.append(nums1[i])
            k = k + 1
            i = i + 1
        
        while j < len(nums2):
            mergeList.append(nums2[j])
            k = k + 1
            j = j + 1

        if len(mergeList) % 2 == 0:
            return (mergeList[(len(mergeList) // 2) - 1] + mergeList[len(mergeList) // 2]) / 2
        else:
            return mergeList[len(mergeList) // 2]
