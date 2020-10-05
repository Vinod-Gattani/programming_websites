from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        if not nums:
            return 1
        
        for index, num in enumerate(nums):
            if int(num) <= 0:
                continue
            try:
                nums[int(num)-1] = str(nums[int(num)-1])
            except:
                pass
                
        for index, num in enumerate(nums):

            if type(num) != str:
                return index+1
            
        return max(1, max(map(int, nums))  +1)
    
if __name__ == "__main__":
    nums=[3,4,-1,1]
    print(Solution().firstMissingPositive(nums))
    print(f"Correct Answer is: 2")