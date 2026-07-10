class Solution:
    def isValid(self, s: str) -> bool:
        opening = {'(', '{', '['}
        closing = {'(':')', '{':'}', '[':']'}
        string = []
        for paran in s:
            if paran in opening: string.append(paran)
            else:
                if not string or closing[string.pop()] != paran:
                    return False

        return not string