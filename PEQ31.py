class Solution:
   def solve(self, coins, amount):
      dp = [0] * (amount + 1)
      dp[0] = 1
      for d in coins:
         for i in range(1, len(dp)):
            if i - d >= 0:
               dp[i] += dp[i - d]
      return dp[-1] % (10 ** 9 + 7)
ob = Solution()
coins = [1,2,5,10,20,50,100,200]
amount = 200
print(ob.solve(coins, amount))
