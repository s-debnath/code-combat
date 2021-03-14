# 645. Set Mismatch
# Difficulty: Easy
# https://leetcode.com/problems/set-mismatch/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        total_nums = len(nums)
        expected_sum = (total_nums*(total_nums+1))//2
        
        actual_sum = 0
        duplicate = 0
        existing_nums = set()
        
        for num in nums:
            if num in existing_nums:
                duplicate = num
            else:
                existing_nums.add(num)
            actual_sum += num
            
        missing_num = expected_sum - (actual_sum - duplicate)
        
        return [duplicate, missing_num]
