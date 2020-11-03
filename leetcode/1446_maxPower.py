class Solution:
    def maxPower(self, s: str) -> int:
        
        start_char = None
        
        power = 0
        power_running = 0
        
        for char in s:
            if char == start_char:
                power_running += 1
            else:
                power = max(power, power_running)
                power_running = 1
            
            start_char = char
        
        power = max(power, power_running)
        
        return power
            
if __name__ == "__main__":
    string = "hooraaaaaaaaaaays"
    print(Solution().maxPower(string))
    print(f"Correct Answer is: 11")