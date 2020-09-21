from typing import List

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        passengers = [0]*1001
        
        for num_passengers, start_loc, end_loc in trips:
            for i in range(start_loc,end_loc):
                passengers[i] += num_passengers
        
        return max(passengers) <= capacity
    
    def carPooling_copied(self, trips: List[List[int]], capacity: int) -> bool:
        timestamp = [0] * 1001
        for trip in trips:
            timestamp[trip[1]] += trip[0]
            timestamp[trip[2]] -= trip[0]

        used_capacity = 0
        for passenger_change in timestamp:
            used_capacity += passenger_change
            if used_capacity > capacity:
                return False

        return True
    
if __name__ == "__main__":
    
    trips = [[2,1,5],[3,3,7]]
    capacity = 4
    
    print(Solution().carPooling(trips, capacity))
    print(f"Correct Answer is: False")