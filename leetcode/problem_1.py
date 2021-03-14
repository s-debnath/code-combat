# 1. Two Sum
# Difficulty: Easy
# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_index = {}
        
        for index, num in enumerate(nums):
            desired_diff = target - num
            if desired_diff not in nums_index:
                nums_index[num] = index
            else:
                return [index, nums_index[desired_diff]]
