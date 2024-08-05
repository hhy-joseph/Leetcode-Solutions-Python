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
