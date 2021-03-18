# 478. Generate Random Point in a Circle
# Difficulty: Medium
# https://leetcode.com/problems/generate-random-point-in-a-circle/

import math
import random

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center
        

    def randPoint(self) -> List[float]:
        random_radian = random.uniform(0, 2 * math.pi)
        hyp = math.sqrt(random.uniform(0, 1)) * self.radius
        
        x_offset = math.cos(random_radian) * hyp
        y_offset = math.sin(random_radian) * hyp
        
        return [self.x_center + x_offset, self.y_center + y_offset]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()