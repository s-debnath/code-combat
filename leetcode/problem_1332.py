# 1332. Remove Palindromic Subsequences
# Difficulty: Easy
# https://leetcode.com/problems/remove-palindromic-subsequences/

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if s == "":
            return 0
        elif s == s[::-1]
            return 1
        else:
            return 2
