class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        
        if needle in haystack:
            haystack = haystack.replace(needle,"A")
            for idx,i in enumerate(haystack):
                if i == "A":
                    return idx
        return -1
