# Missing Number
# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/588/week-1-march-1st-march-7th/3659/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total_nums = len(nums)
        expected_sum = (total_nums*(total_nums+1))//2
        actual_sum = sum(nums)
        return expected_sum - actual_sum
