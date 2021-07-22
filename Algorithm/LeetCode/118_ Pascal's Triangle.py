# 이항계수로 풀긴했는데, DP로 푸는게 더 맞는듯..

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for n in range(numRows):
            row = []
            for r in range(n+1):
                nCr =int( math.factorial(n) / (math.factorial(n-r)*math.factorial(r)) )
                
                row.append(nCr)
                
            res.append(row)
        return res
      
# class Solution:
#     def generate(self, num_rows: int) -> List[List[int]]:
#         triangle = []

#         for row_num in range(num_rows):
#             # The first and last row elements are always 1.
#             row = [None for _ in range(row_num + 1)]
#             row[0], row[-1] = 1, 1

#             # Each triangle element is equal to the sum of the elements
#             # above-and-to-the-left and above-and-to-the-right.
#             for j in range(1, len(row) - 1):
#                 row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]

#             triangle.append(row)

#         return triangle
