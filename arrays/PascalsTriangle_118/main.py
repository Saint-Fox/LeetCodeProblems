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


solution = Solution()
print(solution.generate(5))
# print(fact(5))
# n! = n*(n-1)*(n-2)*...*2*1
