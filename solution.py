from typing import List
import bisect

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Create a list to store the number of ways to make each amount
        dp = [0] * (amount + 1)
        dp[0] = 1  # There's one way to make amount 0: use no coins

        # Iterate over each coin
        for coin in coins:
            # Update the dp array for all amounts from coin to amount
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]

        return dp[amount]
