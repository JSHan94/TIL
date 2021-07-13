class Solution:
    def addBinary(self, a: str, b: str) -> str:
        s = str(int(a) + int(b))
        carry = 0
        res = ""
        for item in s[::-1] :
            if carry + int(item) >= 2 :
                res += str(carry + int(item) - 2 )
                carry = 1
            else :
                
                res += str(carry + int(item))
                carry = 0
        if carry == 1:
            res+= "1"    
        return res[::-1]
                
