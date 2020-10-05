class Solution:
    def myAtoi(self, str: str) -> int:
        
        valid_number = 0
        start = False
        negative_number = False
        
        for char in str:
            
            if char == "+":
                if start:
                    break
                start=True
            elif char=="-":
                if start:
                    break
                start=True
                negative_number=True
            elif char.isdigit():
                valid_number = valid_number*10 + int(char)
                start = True
            elif start is True:
                break
            elif char != " ":
                break
                
        if valid_number:
            if negative_number:
                valid_number = -1*valid_number
            valid_number = max(min(valid_number, 2147483647), -2147483648)
            return valid_number

        else:
            return 0
        
if __name__ == "__main__":
    string = "4193 with words"
    print(Solution().myAtoi(string))
    print(f"Correct Answer is: 4193")