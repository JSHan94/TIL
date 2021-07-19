class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pa,pb = 0, len(numbers)-1
        
        while pa < pb:
            s = numbers[pa] + numbers[pb]
            if s > target:
                pb -=1
            elif s < target:
                pa +=1
            else :
                return [pa+1,pb+1]
            
        return -1
