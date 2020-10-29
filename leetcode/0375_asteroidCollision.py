from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        output = []
        
        for asteroid in asteroids:
            if not output or output[-1] < 0 or asteroid > 0:
                output.append(asteroid)
                
            else:
    
                asteroid_abs = abs(asteroid)
                prev_value = output[-1]
            
                while output and (asteroid < 0 and prev_value > 0):
                    
                    if prev_value == asteroid_abs:
                        output.pop()
                        break
                    elif prev_value > asteroid_abs:
                        break
                    else:
                        output.pop()
                        if not output or output[-1] < 0:
                            output.append(asteroid)
                            break
                        else:
                            prev_value = output[-1]

        return output
    
if __name__ == "__main__":
    asteroids = [5,10,-5]
    print(Solution().asteroidCollision(asteroids))
    print(f"Correct Answer is: [5,10]")