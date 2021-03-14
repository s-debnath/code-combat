# 82. Remove Duplicates from Sorted List II
# Difficulty: Medium
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        new_head = None
        current_node = head
        prev_node = None
        
        while current_node:
            if current_node.next is None or current_node.val != current_node.next.val:
                if new_head is None:
                    new_head = current_node
                prev_node = current_node
                current_node = current_node.next
            else:
                removed_value = current_node.val
                while current_node and current_node.val == removed_value: 
                    current_node = current_node.next
                if prev_node:
                    prev_node.next = current_node

        return new_head