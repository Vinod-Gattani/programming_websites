
from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        gain = (x-y for x, y in zip(gas, cost))
        
        n = len(gas)
        
        dp = [None]*n
        dp[0] = next(gain)
    
        for i in range(1, n):
            dp[i] = dp[i-1] + next(gain)
        
        if dp[-1] < 0:
            return -1
        
        return (dp.index(min(dp)) + 1) % n
    
    
if __name__ == "__main__":
    gas=[1,2,3,4,5]
    cost=[3,4,5,1,2]
    
    print(Solution().canCompleteCircuit(gas,cost))
    
    print(f"Correct Answer is: 3")