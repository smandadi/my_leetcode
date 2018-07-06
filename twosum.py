#!/usr/bin/env python3
"""
Description: 
	Leetcode Two Sum 

Problem:
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1]. 

Link:
	https://leetcode.com/problems/two-sum/description/
"""

class Solution():
	""" 
	Standard class with solution in twosum function
	"""
	def twoSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		for i,j in enumerate(nums):
			diff = target - j
			if diff in nums[i+1:]:
				return [i, nums[i+1:].index(diff) + i + 1]


if __name__ == "__main__":
	output = Solution().twoSum([2, 7, 11, 15], 9)
	print(output)
