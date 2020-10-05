from typing import List

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        #take 1 day cost
        
        dp = [0]*(days[-1]+1)
        
        for i in range(1, len(dp)):
            
            if i not in days:
                dp[i] = dp[i-1]
                
            else:
                dp[i] = min(costs[0]+dp[max(0, i-1)],
                           costs[1]+dp[max(0,i-7)],
                           costs[2]+dp[max(0, i-30)])
                
        
        return dp[-1]


if __name__ == "__main__":
    days=[1,4,6,7,8,20]
    costs=[2,7,15]

    print(Solution().mincostTickets(days, costs))

    print(f"Correct Answer is: 11")