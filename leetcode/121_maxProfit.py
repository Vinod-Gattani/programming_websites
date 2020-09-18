
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) <= 1:
            return 0
        
        max_profit = 0
        buy_price = prices[0]
        
        for price in prices[1:]:
            
            max_profit = max(max_profit, price - buy_price)
            buy_price = min(buy_price, price)
                
        return max_profit
    
    
if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    print(Solution().maxProfit(prices))
    print(f"Correct Answer is: 5")