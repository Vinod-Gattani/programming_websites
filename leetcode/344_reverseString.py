from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l_s = len(s)
        
        for i in range(l_s//2):
            #print(i, l_s-i-1)
            
            s[i], s[l_s-i-1] = s[l_s-i-1], s[i]
            
            
        return s