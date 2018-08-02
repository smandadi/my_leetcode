#!/usr/bin/env python3
"""
Description: 
	Container With Most Water

Problem:
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

Pic: https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg

Example:
Input: [1,8,6,2,5,4,8,3,7]
Output: 49

Link:
	https://leetcode.com/problems/container-with-most-water/description/
"""


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        max_volume = 0
        b_length = len(height) - 1
        
        while i < b_length:
            volume = (b_length - i) * min(height[i], height[b_length])
            max_volume = max(max_volume, volume)
            if height[i] < height[b_length]:
                i += 1
            else:
                b_length -= 1
        return max_volume
    
if __name__ == "__main__":
    answer = Solution()
    print(answer.maxArea([1,8,6,2,5,4,8,3,7]))