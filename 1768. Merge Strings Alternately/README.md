# Merge Alternately Problem Solution

## Description

This repository contains a Python solution to merge two strings alternately character by character. The function `mergeAlternately` takes two strings as input and returns a single string with characters from both strings alternated. If one string is longer than the other, the remaining characters from the longer string are appended at the end.

## Function Signature

```python
def mergeAlternately(word1: str, word2: str) -> str:
    """
    This function merges two strings alternately character by character.
    
    :param word1: The first string.
    :type word1: str
    :param word2: The second string.
    :type word2: str
    :return: The merged string with characters from word1 and word2 alternated.
    :rtype: str
    """
