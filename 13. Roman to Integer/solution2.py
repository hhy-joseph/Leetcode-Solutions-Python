class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numerals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        pre_val = 10000
        total = 0
        for char in s:
            # Roman numerals are usually written largest to smallest from left to right.
            cur_val = roman_numerals[char]
            if cur_val > pre_val:
                # take away in the case of six instances
                total = total - pre_val
                cur_val = abs(pre_val-cur_val)
                # prev: C:100
                # cur: M: 1000
            pre_val =  roman_numerals[char]
            total += cur_val
        return total
