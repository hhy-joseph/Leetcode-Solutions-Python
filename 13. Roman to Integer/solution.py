class Solution:
    def romanToInt(self, s: str) -> int:
        """
        This function converts a Roman numeral string to an integer.
        
        :param s: Roman numeral string.
        :type s: str
        :return: Integer representation of the Roman numeral.
        :rtype: int
        """
        # Dictionary to map Roman numerals to their integer values
        m = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        # Initialize the answer variable
        ans = 0
        
        # Iterate through the string of Roman numerals
        for i in range(len(s)):
            # If the current numeral is less than the next one, subtract its value
            if i < len(s) - 1 and m[s[i]] < m[s[i+1]]:
                ans -= m[s[i]]
            else:
                # Otherwise, add its value
                ans += m[s[i]]
        
        # Return the final computed integer
        return ans
