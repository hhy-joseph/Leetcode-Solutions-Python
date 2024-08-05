from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        This function finds the longest common prefix string amongst an array of strings.
        If there is no common prefix, it returns an empty string.
        
        :param strs: List of strings.
        :type strs: List[str]
        :return: The longest common prefix.
        :rtype: str
        """
        # If the input list is empty, return an empty string
        if not strs:
            return ""
        
        # Find the minimum length string in the list
        min_length = min(len(s) for s in strs)
        
        # Initialize the prefix
        prefix = ""
        
        # Iterate over the range of the minimum length
        for i in range(min_length):
            # Take the character from the first string as the reference
            current_char = strs[0][i]
            
            # Check this character against all other strings at the same position
            for string in strs:
                if string[i] != current_char:
                    return prefix
            
            # If the current character is common in all strings, add it to the prefix
            prefix += current_char
        
        return prefix
