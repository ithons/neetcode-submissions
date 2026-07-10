def isValid(freq, k):
    if not freq: return True
    max_letter = max(freq, key=freq.get)
    sum = 0
    for key, value in freq.items():
        if key != max_letter:
            sum += value
    return sum <= k

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 1
        l = 0
        r = 0
        freq = {}
        while r<len(s):
            if isValid(freq, k):
                char = s[r]
                if char in freq: freq[char] += 1
                else: freq[char] = 1
                longest = max(longest, r-l)
                r+=1
            else:
                char = s[l]
                freq[char] -= 1
                l+=1
        if isValid(freq, k): longest = max(longest, r-l)
        return longest