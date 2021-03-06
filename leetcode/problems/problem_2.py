# 2. Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:        
        if not l1:
            return l2
        
        if not l2:
            return l1
        
        result_head = ListNode()
        current_node = result_head
        carryover = False
        
        while l1 or l2 or carryover:
            val1 = 0
            if l1:
                val1 = l1.val
                l1 = l1.next
            
            val2 = 0
            if l2:
                val2 = l2.val
                l2 = l2.next
                
            val_total = val1 + val2
            if carryover:
                val_total += 1
                
            carryover = val_total >= 10
            
            val_digit = val_total if not carryover else val_total - 10
                
            current_node.val = val_digit
            
            if l1 or l2 or carryover:
                current_node.next = ListNode()
                current_node = current_node.next
            
        return result_head