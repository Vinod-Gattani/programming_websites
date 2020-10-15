class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        last_index = {}
    
        
        for index, char in enumerate(s):
            last_index[char] = index
            
        min_index = sorted(last_index.values(), reverse=True)
        
        result = []
        
        for index, char in enumerate(s):
            
            if char not in result:
                while result and char < result[-1] and index < last_index[result[-1]]:
                    result.pop()
                
                result.append(char)
        
        return "".join(result)
    
    
if __name__ == "__main__":
    s = "bcabc"
    print(Solution().removeDuplicateLetters(s))
    print(f"Correct Answer is: abc")