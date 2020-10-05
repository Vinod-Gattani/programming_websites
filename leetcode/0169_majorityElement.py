

from collections import Counter

class Solution:
    def majorityElement(self, nums) -> int:
        
        c = Counter(nums)
        
        count = len(nums)//2 + 1
        
            
        for _c in c:
            if c[_c]>=count:
                return _c
            
        
        
            
            