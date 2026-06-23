class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_unique = set(s)
        t_unique = set(t)
        if s_unique != t_unique: return False
        for key in set(s):
            if s.count(key) != t.count(key): return False
        return True