from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str):
        
        result = []
        
        len_p = len(p)
        set_p = Counter(p)
        
        for index, i in enumerate(s):
            
            a = s[index:index+len_p]
            if len(a) < len_p:
                break
            if Counter(s[index:index+len_p]) == set_p:
                result.append(index)
                
        return result

        #copied
        def findAnagrams1(self, s: str, p: str):
            result=[]
            if len(s)<len(p):
                return result
            countString=[0]*26
            countSubString=[0]*26
            for i in range(0,len(p)):
                countSubString[ord(p[i])-ord('a')]+=1
                countString[ord(s[i])-ord('a')]+=1
            start=0
            end=len(p)-1
            while end<len(s):
                if countString==countSubString:
                    result.append(start)
                end+=1
                if end==len(s):
                    break
                countString[ord(s[end])-ord('a')]+=1
                countString[ord(s[start])-ord('a')]-=1
                start+=1

            return result