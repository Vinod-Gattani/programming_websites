class Solution:
    
    def countDigit(self, n): 
        if n == 0: 
            return 0
        return 1 + self.countDigit(n // 10) 

    
    def findNumbers(self, nums) -> int:
        
        result = 0
        
        for i in nums:
            digit_count = self.countDigit(i)
            
            if digit_count % 2 == 0:
                result += 1
                
        return result