#ransom note

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        magazine = list(magazine)
        
        for letter in ransomNote:
            try:
                index = magazine.index(letter)
                magazine.pop(index)
            except:
                return False
        
        return True
        