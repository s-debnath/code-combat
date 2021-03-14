# 322. Coin Change
# Difficulty: Medium
# https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = sorted(filter(lambda coin: coin <= amount, coins))
        
        subamounts = [amount+1] * (amount + 1)
        subamounts[0] = 0
        for idx in range(0, amount+1):
            for coin in coins:
                if coin > idx:
                    continue
                
                diff = idx - coin
                subamounts[idx] = min(subamounts[diff]+1, subamounts[idx])
                                        
        return subamounts[-1] if subamounts[-1] <= amount else -1
