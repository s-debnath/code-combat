# Integer to Roman
# https://leetcode.com/explore/featured/card/march-leetcoding-challenge-2021/589/week-2-march-8th-march-14th/3667/


class Solution:
    def intToRoman(self, num: int) -> str:                
        numeral_config = [
            {
                "num_range": (1000, 10000),
                "base_symbol": "M",
                "midpoint_symbol": "V",
                "next_symbol": "X"
            },
            {
                "num_range": (100, 1000),
                "base_symbol": "C",
                "midpoint_symbol": "D",
                "next_symbol": "M"
            },
                        {
                "num_range": (10, 100),
                "base_symbol": "X",
                "midpoint_symbol": "L",
                "next_symbol": "C"
            },
                        {
                "num_range": (1, 10),
                "base_symbol": "I",
                "midpoint_symbol": "V",
                "next_symbol": "X"
            }
        ]
        
        final = ""
        for config in numeral_config:
            lower_range, higher_range = config['num_range']
            base_symbol = config['base_symbol']
            midpoint_symbol = config['midpoint_symbol']
            next_symbol = config['next_symbol']
        
            if lower_range <= num < higher_range:
                place = num//lower_range

                if place < 4:
                    final += base_symbol * place
                elif place == 4:
                    final += base_symbol + midpoint_symbol
                elif place == 5:
                    final += midpoint_symbol
                elif place < 9:
                    final += midpoint_symbol + (base_symbol*(place-5))
                else:
                    final += base_symbol + next_symbol

                num -= place * lower_range

            
        return final