class Solution:
    def longestPrefix(self, s: str) -> str:
        
        max_index = -1
        
        for index, _ in enumerate(s[:-1]):
            
            if s[:index+1] == s[-1*(index+1):]:
                max_index = index
        
        return s[:max_index+1]
    
if __name__ == "__main__":
    s="ababab"
    print(Solution().longestPrefix(s))
    print(f"Correct Answer is: abab")