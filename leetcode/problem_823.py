# 823. Binary Trees With Factors
# Difficulty: Medium
# https://leetcode.com/problems/binary-trees-with-factors/


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr = sorted(arr)
        num_ways_dict = {}
        
        for num in arr:
            if num not in num_ways_dict:
                num_ways_dict[num] = 1
            else:
                num_ways_dict[num] += 1
                
            for pnum in arr:
                if pnum >= num:
                    break;
                                    
                if num % pnum != 0:
                    continue
                
                result = num // pnum
                        
                if result in num_ways_dict and result >= pnum:
                    mult_factor = 2 if result != pnum else 1
                    num_ways_dict[num] += num_ways_dict[pnum] * num_ways_dict[result] * mult_factor
                    
                    
        return sum(num_ways_dict.values()) % (10**9 + 7)
