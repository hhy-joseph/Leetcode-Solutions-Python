class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        Add two numbers represented by linked lists l1 and l2, and return the sum as a linked list.
        :param l1: ListNode
        :param l2: ListNode
        :return: ListNode
        """
        carry = 0
        # Initialize the dummy head of the result list
        result = temp_node = ListNode(val=0)
        
        # Loop until both lists are exhausted and no carry remains
        while l1 or l2 or carry:
            # Extract the current values from l1 and l2, or use 0 if the list is exhausted
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            # Calculate the sum and the carry
            total = v1 + v2 + carry
            carry = total // 10
            reminder = total % 10
            
            # Create a new node with the computed digit
            temp_node.next = ListNode(val=reminder)
            
            # Move the temp_node pointer to the new node
            temp_node = temp_node.next
            
            # Advance the l1 and l2 pointers if they are not already exhausted
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        # Return the next node of the dummy head as the result
        return result.next
