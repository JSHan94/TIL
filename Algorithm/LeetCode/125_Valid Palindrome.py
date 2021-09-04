class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for i in s:
            if ord('A') <= ord(i) <= ord('Z') or ord('a') <= ord(i) <= ord('z'):
                res+= i.lower()
            elif ord('0') <= ord(i) <= ord('9'):
                res+= i
        return res[::-1] == res
    
