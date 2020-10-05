from itertools import zip_longest

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        output = ''
        carry_over = 0
        
        for char1, char2 in zip_longest(num1[::-1], num2[::-1]):
                    
            #char1 = int(char1) if char1 else 0
            #char2 = int(char2) if char2 else 0
            char1 = ord(char1)-ord('0') if char1 else 0
            char2 = ord(char2)-ord('0') if char2 else 0
            
            val = char1+char2+carry_over
            carry_over = val // 10
            
            output += str(val%10)
        
        if carry_over:
            output += str(carry_over)
        
        return output[::-1]

if __name__ == "__main__":
    num1="310"
    num2="298"
    print(Solution().combinationSum(num1, num2))
    print(f"Correct Answer is: 608")