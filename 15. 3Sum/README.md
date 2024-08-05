# Is Subsequence Problem Solution

## Description

This repository contains two Python solutions to check if a string `s` is a subsequence of another string `t`. A string `s` is a subsequence of `t` if `s` can be derived from `t` by deleting some or no characters without changing the order of the remaining characters.

## Solutions

### Solution 1 (solution.py)

This solution checks if `s` is a subsequence of `t` by iterating through each character in `t` and matching it with the characters in `s` in order.

### Solution 2 (solution2.py)
This solution checks if s is a subsequence of t by creating a list of characters from t that are in s and then comparing the joined list with s.

Explanation
Create an empty list: Initialize an empty list called merged.
Iterate through each character in t:
For each character in t, check if it is in s.
If it is, append it to the merged list.
Join the list and compare:
Join the characters in the merged list to form a string.
Compare the formed string with s. If they are equal, return True; otherwise, return False.
