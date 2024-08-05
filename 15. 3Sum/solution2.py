class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        merged = []
        
        for char in t:
            if char in s:
                merged.append(char)
        
        return ''.join(merged) == s
