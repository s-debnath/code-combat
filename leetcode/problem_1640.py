# 1640. Check Array Formation Through Concatenation
# Difficulty: Easy
# https://leetcode.com/problems/check-array-formation-through-concatenation/

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        arr_lookup = {}
        
        for i in range(0, len(arr)):
            arr_lookup[arr[i]] = i
            
        for piece in pieces:
            piece_len = len(piece)
            start = piece[0]
            start_index = arr_lookup.get(start)
                        
            if start_index is None:
                return False
            
            arr_slice = arr[start_index:start_index+piece_len]
            
            if piece_len != len(arr_slice) or piece != arr_slice:
                return False
            
        return True