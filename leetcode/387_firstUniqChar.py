from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_c = Counter(s)
        
        for _s in s_c:
            if s_c[_s] == 1:
                return s.find(_s)
        
        return -1
                
        