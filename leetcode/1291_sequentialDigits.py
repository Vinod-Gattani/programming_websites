from typing import List

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        
        result = []
        
                    
        for i in range(1, 10):
            number = i
            if number >= low and number <= high:
                result.append(number)
            
            for j in range(i+1, 10):
                number = 10*number + j
                
                if number > high:
                    break                    
                elif number >= low:
                    result.append(number)

        result.sort()
        
        return result
        
if __name__ == "__main__":
    low=100
    high=300
    print(Solution().sequentialDigits(low, high))
    print(f"Correct Answer is: [123,234]")