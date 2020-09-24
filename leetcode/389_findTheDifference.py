class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        for char1, char2 in zip(sorted_s, sorted_t):
            
            if char1 != char2:
                return char2
            
        return sorted_t[-1]
    
    def findTheDifference_copied(self, s: str, t: str) -> str:
        ans=0
        for c in s:
            ans^=ord(c)
        for c in t:
            ans^=ord(c)
        return chr(ans)
        
        #another copied
        total = 0
        for i, char in enumerate(s):
            total += ord(t[i])
            total -= ord(char)
        total += ord(t[-1])
        return chr(total)

if __name__ == "__main__":
    s = "abcd"
    t = "abcde"
    print(Solution().findTheDifference(s,t))
    print(f"Correct Answer is: e")