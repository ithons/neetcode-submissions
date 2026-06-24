class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = [char.lower() for char in s if char.isalnum()]
        l, r = 0, len(filtered) - 1
        while l < r:
            if filtered[l] != filtered[r]:
                return False
            l += 1
            r -= 1
            
        return True