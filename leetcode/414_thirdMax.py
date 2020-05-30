from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        max_num = set()
        
        for num in nums:
            max_num.add(num)
            if len(max_num) > 3:
                max_num.remove(min(max_num))
                
        if len(max_num) < 3:
            return max(max_num)
        else:
            return min(max_num)

    #copied O1Soln
    def thirdMax1(self, nums: List[int]) -> int:
        
        
        one = -float('inf')
        two = -float('inf')
        three = -float('inf')
        
        for num in nums:
            if num > one:
                one, two, three = num, one, two
            elif two < num < one:
                two, three = num, two
            elif three < num < two:
                three = num
                
        if three == -float('inf'):
            return one
        else:
            return three