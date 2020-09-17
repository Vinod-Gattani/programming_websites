from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) <= 1:
            return sum(nums)
        elif len(nums) == 2:
            return max(nums)
        else:
            dp = [0]*len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0:2])
            for i in range(2, len(nums)):
                dp[i] = max(nums[i]+dp[i-2], dp[i-1])
                
        
        return dp[-1]
    
    
if __name__ == "__main__":
    nums = [1,2,3,1]
    print(Solution().rob(nums))
    print(f"Correct Answer is: 4")