# Is Subsequence Problem Solution

## Description

This repository contains two Python solutions to check if a string `s` is a subsequence of another string `t`. A string `s` is a subsequence of `t` if `s` can be derived from `t` by deleting some or no characters without changing the order of the remaining characters.

## Solutions

### Solution 1 (solution.py)

This solution checks if `s` is a subsequence of `t` by iterating through each character in `t` and matching it with the characters in `s` in order.

#### Function Signature

```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        This function checks if string s is a subsequence of string t.
        
        :param s: String to check as a subsequence.
        :type s: str
        :param t: String to check against.
        :type t: str
        :return: True if s is a subsequence of t, False otherwise.
        :rtype: bool
        """
        # Initialize a pointer for the string s
        s_index = 0
        
        # Iterate through each character in string t
        for char in t:
            # If the character in t matches the character in s at s_index
            if s_index < len(s) and char == s[s_index]:
                # Move the pointer to the next character in s
                s_index += 1
        
        # If we have matched all characters in s, return True
        return s_index == len(s)
