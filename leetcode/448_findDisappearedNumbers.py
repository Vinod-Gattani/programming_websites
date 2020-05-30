from typing import List

class Solution:
    def findDisappearedNumbers1(self, nums: List[int]) -> List[int]:
        
        return list( set(range(1,len(nums)+1)) - set(nums))
    
    
    #https://www.youtube.com/watch?v=re7fhVyKWZI
    def findDisappearedNumbers(self, nums):
        
        missing_nums = []
        
        for num in nums:
            pos = abs(num)
            
            if nums[pos-1] > 0:
                nums[pos-1] = nums[pos-1]*-1
        
        for index, num in enumerate(nums):
            if num > 0:
                missing_nums.append(index + 1)
                
        return missing_nums