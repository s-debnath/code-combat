# 869. Reordered Power of 2
# Difficulty: Medium
# https://leetcode.com/problems/reordered-power-of-2/

class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        sorted_num_str = "".join(sorted(str(N), reverse=True))
        sorted_num_int = int(sorted_num_str)
        
        power_of_two = 0
        i = 0
        
        while power_of_two <= sorted_num_int:
            power_of_two = 2 ** i
            sorted_power_of_two_str = "".join(sorted(str(power_of_two), reverse=True))
            
            if sorted_power_of_two_str == sorted_num_str:
                return True
            
            i += 1

        return False