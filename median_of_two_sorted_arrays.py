#!/usr/bin/env python3
"""
Description:
    Leetcode Median of Two Sorted Arrays

Problem:
    There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Examples:
    1) nums1 = [1, 3]
       nums2 = [2]

    The median is 2.0

    2) nums1 = [1, 2]
       nums2 = [3, 4]

    The median is (2 + 3)/2 = 2.5

Link:
    https://leetcode.com/problems/median-of-two-sorted-arrays/description/

"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num = nums1 + nums2
        num = sorted(num)
        if len(num)%2 != 0:
            return num[len(num)//2]
        x = len(num)//2
        m = num[x] + num[x-1]
        return m/2


if __name__ == "__main__":
    output = Solution().findMedianSortedArrays([1,2], [3,4])
    print(output)