# 820. Short Encoding of Words
# Difficulty: Medium
# https://leetcode.com/problems/short-encoding-of-words/

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        sorted_words = sorted(words, key=lambda x:len(x), reverse=True)
        included_values = []
        
        for word in sorted_words:
            should_be_included = True
            for included in included_values:
                if included.endswith(word):
                    should_be_included = False
            if should_be_included:
                included_values.append(word)
        
        encoded_string = '#'.join(included_values)
        return len(encoded_string) + 1
