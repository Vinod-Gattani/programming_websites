class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        return len(s.strip().split(" ")[-1])
    
    
if __name__ == "__main__":
    s="Hello World"
    print(Solution().lengthOfLastWord(s))
    print(f"Correct Answer is: 5")