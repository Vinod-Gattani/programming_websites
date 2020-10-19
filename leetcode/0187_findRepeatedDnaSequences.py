from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        start = 0
        end = 10
        
        str_map = {}
        result = []
        
        while end <= len(s):
            seq = s[start:end]
            occur = str_map.get(seq,0)
            if occur==1:
                result.append(seq)
            str_map[seq] = occur + 1
                
            start+=1
            end+=1
        
        return result
    
if __name__ == "__main__":
    string = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    print(Solution().findRepeatedDnaSequences(string))
    print(f"Correct Answer is: ['AAAAACCCCC','CCCCCAAAAA']")