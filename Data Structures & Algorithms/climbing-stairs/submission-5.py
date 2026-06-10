class Solution:
    def climbStairs(self, n: int) -> int:
        DP = [0] * n
       
        if not DP :
            return 0
        if n == 1:
            return 1
        DP[0] = 1
        DP [1] = 2
        for i in range(2, n):
            DP[i] = DP[i-1] + DP[i-2] 

        return DP[n-1]
        