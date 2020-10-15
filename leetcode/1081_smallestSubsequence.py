class Solution:
    def smallestSubsequence(self, s: str) -> str:
        
        last_index = {}
    
        
        for index, char in enumerate(s):
            last_index[char] = index
        
        result = []
        
        for index, char in enumerate(s):
            
            if char not in result:
                while result and char < result[-1] and index < last_index[result[-1]]:
                    result.pop()
                
                result.append(char)
        
        return "".join(result)
    
    
if __name__ == "__main__":
    s = "bcabc"
    print(Solution().smallestSubsequence(s))
    print(f"Correct Answer is: abc")