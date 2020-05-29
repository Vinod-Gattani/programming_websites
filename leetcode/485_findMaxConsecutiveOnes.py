class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        
        running_count = 0
        max_count = 0
        
        for i in nums:
            
            if i:
                running_count += i
                max_count = max(max_count, running_count)
            else:
                running_count = 0
                
        return max_count
            
        