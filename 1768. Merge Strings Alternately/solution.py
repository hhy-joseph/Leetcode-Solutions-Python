class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        This function merges two strings alternately character by character.
        
        :param word1: The first string.
        :type word1: str
        :param word2: The second string.
        :type word2: str
        :return: The merged string with characters from word1 and word2 alternated.
        :rtype: str
        """
        merged = []  # Initialize a list to store the merged characters
        len1, len2 = len(word1), len(word2)
        min_len = min(len1, len2)
        
        # Iterate through both strings up to the length of the shorter string
        for i in range(min_len):
            merged.append(word1[i])
            merged.append(word2[i])
        
        # Append the remaining part of the longer string
        if len1 > len2:
            merged.extend(word1[min_len:])
        else:
            merged.extend(word2[min_len:])
        
        # Join the list into a single string and return it
        return ''.join(merged)
