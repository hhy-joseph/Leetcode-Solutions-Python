class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Dictionary to keep track of the last seen position of each character
        char_dict = {}
        
        # Initialize the left pointer of the window and the maximum length
        left = 0
        max_length = 0 
        
        # Iterate through the string with the right pointer
        for right in range(len(s)):
            # Check if the current character is a repeat within the current window
            if s[right] in char_dict and char_dict[s[right]] >= left:
                # Move the left pointer to the position right after the last occurrence
                left = char_dict[s[right]] + 1
            
            # Update the last seen index of the current character
            char_dict[s[right]] = right
            
            # Calculate the length of the current substring and update max_length if it's longer
            max_length = max(max_length, right - left + 1)
        
        return max_length
