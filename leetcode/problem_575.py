# 575. Distribute Candies
# Difficulty: Easy
# https://leetcode.com/problems/distribute-candies/

class Solution:
    def distributeCandies(self, candy_types: List[int]) -> int:
        num_can_eat_candies = int(len(candy_types) / 2)
        possible_candies = len(set(candy_types))
        return min(num_can_eat_candies, possible_candies)
