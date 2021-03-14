# 623. Add One Row to Tree
# Difficulty: Medium
# https://leetcode.com/problems/add-one-row-to-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if not root:
            return root
        
        if d == 1:
            new_root = TreeNode(val=v, left=root)
            return new_root
        
        traverse(root, 1, v, d)
       
        return root
    
def traverse(node: TreeNode, current_depth: int, value: int, desired_depth: int) -> None:
    if not node:
        return
    
    next_depth = current_depth + 1
    
    if next_depth != desired_depth:
        traverse(node.left, next_depth, value, desired_depth)
        traverse(node.right, next_depth, value, desired_depth)
    else:
        new_left = TreeNode(val=value, left=node.left)
        node.left = new_left

        new_right = TreeNode(val=value, right=node.right)
        node.right = new_right