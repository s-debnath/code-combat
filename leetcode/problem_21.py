# 21. Merge Two Sorted Lists
# Difficulty: Easy
# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None and l2 is None:
            return None
        
        first_combined_node = ListNode()
        curr_node = first_combined_node
                        
        while l1 or l2:
            if l1 is not None and (l2 is None or l1.val < l2.val):
                curr_node.val = l1.val
                l1 = l1.next
            else:
                curr_node.val = l2.val
                l2 = l2.next
            
            if l1 or l2: 
                next_node = ListNode()
                curr_node.next = next_node
                curr_node = next_node
        
        return first_combined_node
