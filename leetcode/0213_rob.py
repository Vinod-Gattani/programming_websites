
from typing import List

def rob_1(nums):
    dp = [0]*len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0:2])
    for i in range(2, len(nums)):
        dp[i] = max(nums[i]+dp[i-2], dp[i-1])


    return dp[-1]

class Solution:

    
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) <= 1:
            return sum(nums)
        elif len(nums) == 2:
            return max(nums)
        else:
            return max(rob_1(nums[1:]), rob_1(nums[:-1]))

if __name__ == "__main__":
    nums = [2,3,2]
    print(Solution().rob(nums))
    print(f"Correct Answer is: 3")