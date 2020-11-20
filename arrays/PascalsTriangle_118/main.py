from typing import List

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        t_l = []
        l = []
        for n in range(numRows):
            l = [0]*(n+1)
            for k in range(len(l)):
                l[k] = int(fact(n)/(fact(k)*fact(n-k)))
            t_l.append(l)
        return t_l

    def updated_solution(self, numRows: int) -> List[List[int]]:
        triangle = []
        for num_row in range(numRows):
            row = [None for _ in range(num_row + 1)]
            row[0], row[-1] = 1, 1
            # print(row)
            for j in range(1, len(row)-1):
                print(j)
                row[j] = triangle[num_row - 1][j-1] + triangle[num_row - 1][j]
            triangle.append(row)
        return triangle

solution = Solution()
print(solution.updated_solution(5))
# print([_ for _ in range(5)])
# n! = n*(n-1)*(n-2)*...*2*1
