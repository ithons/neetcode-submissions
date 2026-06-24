class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        indices = {}
        out = []
        for string in strs:
            sorted_string = "".join(sorted(string))
            if sorted_string in indices:
                out[indices[sorted_string]].append(string)
            else:
                indices[sorted_string] = len(out)
                out.append([string,])
        return out