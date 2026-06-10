class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0 :
            return 0
        
        DP = [float("inf")] * (amount + 1) # DP[i] is the min coins to make i amount
        DP[0] = 0


        for i in range(1, amount+1):
            print(i)
            for c in coins:
                if i - c >= 0:
                    DP[i] = min(DP[i], 1 + DP[i-c])
               
        
        return DP[amount] if DP[amount] != float('inf') else -1
            
                


        