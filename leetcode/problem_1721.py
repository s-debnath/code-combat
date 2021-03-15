# 1721. Swapping Nodes in a Linked List
# Difficulty: Medium
# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        cur_node = head
        node_arr = []
        
        while cur_node:
            node_arr.append(cur_node)
            cur_node = cur_node.next
            
        kth_node = node_arr[k-1]
        neg_kth_node = node_arr[-(k)]     
       
        kth_node.val, neg_kth_node.val = neg_kth_node.val, kth_node.val
        
        return head
