class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_s = "".join([char for char in s if char.isalnum()]).lower()
        return filtered_s == filtered_s[::-1]