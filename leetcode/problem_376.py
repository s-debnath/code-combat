# 376. Wiggle Subsequence
# Difficulty: Medium
# https://leetcode.com/problems/wiggle-subsequence/

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        len_nums = len(nums)
        
        if len_nums < 2:
            return len_nums
    
        points = 1  
                    
        idx = 1
        while idx < len_nums:
            current = nums[idx]
            previous = nums[idx - 1]
                    
            if previous < current:
                points += 1
                idx += 1
                while idx < len_nums and nums[idx - 1] <= nums[idx]:
                    idx += 1
            elif previous > current: 
                points += 1
                idx += 1
                while idx < len_nums and nums[idx - 1] >= nums[idx]:
                    idx += 1
            else:
                idx += 1
        
        return points
