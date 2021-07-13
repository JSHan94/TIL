class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_digits = [str(i) for i in digits]
        num = int("".join(str_digits))
        num += 1
        return [int(i) for i in str(num)]
