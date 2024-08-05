# Longest Substring Without Repeating Characters

## Description

This function, `lengthOfLongestSubstring`, finds the length of the longest substring without repeating characters in a given string `s`. The solution utilizes a sliding window approach with two pointers and a dictionary to keep track of characters' positions.

## Approach

1. **Initialization**:
   - A dictionary `char_dict` is used to store the last seen position of each character.
   - Two pointers, `left` and `right`, are used to define the sliding window.
   - A variable `max_length` is initialized to keep track of the maximum length of substrings without repeating characters.

2. **Sliding Window**:
   - Iterate through the string using the `right` pointer.
   - If the current character (`s[right]`) is found in the dictionary and its last seen position is within the current window (i.e., `char_dict[s[right]] >= left`), move the `left` pointer to the position right after the last occurrence of the current character (`left = char_dict[s[right]] + 1`).

3. **Update Dictionary and Maximum Length**:
   - Update the last seen position of the current character in the dictionary (`char_dict[s[right]] = right`).
   - Calculate the length of the current window (`right - left + 1`) and update `max_length` if this window is the longest found so far.

4. **Return Result**:
   - After iterating through the string, return `max_length` as the length of the longest substring without repeating characters.

## Example Usage

```python
sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))  # Output: 3 (substring "abc")
print(sol.lengthOfLongestSubstring("bbbbb"))     # Output: 1 (substring "b")
print(sol.lengthOfLongestSubstring("pwwkew"))    # Output: 3 (substring "wke")
