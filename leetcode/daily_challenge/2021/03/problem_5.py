# Average of Levels in Binary Tree
# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/588/week-1-march-1st-march-7th/3661/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        level_values = traverse(root, 0, {})
        return list(map(lambda level: mean(level), level_values.values()))
    
    

def traverse(node: TreeNode, level: int, level_values: dict[int, List[int]]) -> dict[int, List[int]]:
    if not node:
        return
        
    if level not in level_values:
        level_values[level] = [node.val]
    else:
        level_values[level].append(node.val)
    
    next_level = level + 1
    traverse(node.left, next_level, level_values)
    traverse(node.right, next_level, level_values)
    
    return level_values