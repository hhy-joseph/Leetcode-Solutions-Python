# Time Complexity O(N)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Dictionary to store the number and its index
        searched_dict = {}
        
        # Loop through each number in the list along with its index
        for index, num in enumerate(nums):
            # Calculate the difference needed to reach the target
            diff = target - num
            
            # Check if the difference exists in the dictionary
            if diff in searched_dict:
                # If it exists, return the current index and the index of the difference
                return index, searched_dict[diff]
            
            # Otherwise, store the current number and its index in the dictionary
            searched_dict[num] = index
