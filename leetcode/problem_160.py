# 160. Intersection of Two Linked Lists
# Difficulty: Easy
# https://leetcode.com/problems/intersection-of-two-linked-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, head_a: ListNode, head_b: ListNode) -> ListNode:
        node_set = set()
        
        while head_a or head_b:
            if head_a:
                if head_a in node_set:
                    return head_a
                else:
                    node_set.add(head_a)
            
                head_a = head_a.next
            if head_b:
                if head_b in node_set:
                    return head_b
                else:
                    node_set.add(head_b)
            
                head_b = head_b.next
