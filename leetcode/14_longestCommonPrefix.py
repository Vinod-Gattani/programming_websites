from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs:
            return ""
        
        start_index = 0
        first_word = strs[0]
        
        for char in first_word:
            for word in strs:
                try:
                    if word[start_index] != char:
                        return first_word[:start_index]
                except IndexError:
                    return first_word[:start_index]
            
            start_index += 1
        
        return first_word[:start_index]
        
        
if __name__ == "__main__":
    strs=["flower","flow","flight"]
    print(Solution().longestCommonPrefix(strs))
    print(f"Correct Answer is: fl")