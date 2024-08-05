# Is Subsequence Problem Solution

## Description

This repository contains a Python solution to check if a string `s` is a subsequence of another string `t`. A string `s` is a subsequence of `t` if `s` can be derived from `t` by deleting some or no characters without changing the order of the remaining characters.

## Function Signature

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
Parameters
s: The string to check as a subsequence.
t: The string to check against.
Returns
True if s is a subsequence of t.
False if s is not a subsequence of t.
Explanation
The function follows these steps:

Initialize a pointer for s: Start with the first character of s.
Iterate through each character in t:
For each character in t, check if it matches the current character in s (pointed to by the pointer).
If it matches, move the pointer to the next character in s.
Check if all characters in s were matched:
If the pointer has reached the end of s, all characters were matched in order, so return True.
Otherwise, return False.
```
