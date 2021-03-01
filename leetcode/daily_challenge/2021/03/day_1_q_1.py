# Distribute Candies
# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/588/week-1-march-1st-march-7th/3657/

class Solution:
    def distributeCandies(self, candy_types: List[int]) -> int:
        num_can_eat_candies = int(len(candy_types) / 2)
        possible_candies = len(set(candy_types))
        return min(num_can_eat_candies, possible_candies)
