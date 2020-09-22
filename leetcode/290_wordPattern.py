
from collections import defaultdict

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        
        if len(words) != len(pattern):
            return False
        
        pattern_mapping = defaultdict(lambda :set())
        word_mapping = defaultdict(lambda : set())

        for p, word in zip(pattern, words):
            
            pattern_mapping[p].update([word])
            word_mapping[word].update(p)
            
        #print(pattern_mapping)
        
        for _, value in pattern_mapping.items():
            if len(value) != 1:
                        return False
        for _, value in word_mapping.items():
                    if len(value) != 1:
                        return False
        
        return True

    #using single hash map
    #save first occurence of word and character
    def wordPattern_copied(self, pattern: str, s: str) -> bool:
        map_index = {}
        words = s.split()
        
        if len(pattern) != len(words):
            return False
        
        for i in range(len(words)):
            c = pattern[i]
            w = words[i]

            char_key = 'char_{}'.format(c)
            char_word = 'word_{}'.format(w)
            
            if char_key not in map_index:
                map_index[char_key] = i
            
            if char_word not in map_index:
                map_index[char_word] = i 
            
            if map_index[char_key] != map_index[char_word]:
                return False
        
        return True
    
    
if __name__ == "__main__":
    pattern = "abba"
    s = "dog cat cat dog"

    print(Solution().wordPattern(pattern, s))
    print(f"Correct Answer is: True")