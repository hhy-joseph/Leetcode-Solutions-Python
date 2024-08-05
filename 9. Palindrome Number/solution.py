class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        This function checks if an integer is a palindrome. An integer is a palindrome 
        when it reads the same backward as forward.
        
        :param x: Integer to be checked.
        :type x: int
        :return: True if the integer is a palindrome, False otherwise.
        :rtype: bool
        """
        # Negative numbers are not palindromes
        if x < 0:
            return False
        
        # Initialize variables to store the reversed number and the original number
        reversed_num = 0
        original_num = x
        
        # Loop to reverse the digits of the number
        while x != 0:
            # Get the last digit of the number
            digit = x % 10
            # Build the reversed number
            reversed_num = reversed_num * 10 + digit
            # Remove the last digit from the number
            x = x // 10
        
        # Check if the reversed number is the same as the original number
        return reversed_num == original_num
