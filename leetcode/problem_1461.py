# 1461. Check If a String Contains All Binary Codes of Size K
# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        substrings = set()
                
        for i in range(0, len(s) - k + 1):
            substrings.add(s[i:(i+k)])
                        
        return len(substrings) >= (2**k)