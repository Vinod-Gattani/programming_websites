class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        char_map = dict()
        
        for index, (char1, char2) in enumerate(zip(s, t)):
            
            char1 = "char1_{}".format(char1)
            char2 = "char2_{}".format(char2)
            
            if char1 not in char_map:
                char_map[char1] = index
            if char2 not in char_map:
                char_map[char2] = index
            
            if char_map[char1] != char_map[char2]:
                return False
        
        return True
        
    def isIsomorphic_copied(self,s,t):
        return len(set(s))==len(set(t))==len(set(zip(s,t)))    

if __name__ == "__main__":
    s = "egg"
    t = "add"
    print(Solution().isIsomorphic(s, t))
    print(f"Correct Answer is: True")