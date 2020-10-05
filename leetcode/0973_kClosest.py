from typing import List

def euclideanDistance(point):
    
    x1 = point[0]
    x2 = point[1]
    
    return x1**2 + x2**2
    
from heapq import heappush, heappop

class Solution:
    
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        k_closest = []
        distance = list(map(euclideanDistance, points))
        
        for index, dist in enumerate(distance):
            heappush(k_closest, (-dist, index))
            if len(k_closest) > K:
                heappop(k_closest)

        result = [points[i] for _,i in k_closest]
        return result
    
    def kClosest1(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        distance = map(euclideanDistance, points)
        
        merged = sorted(zip(points, distance), key= lambda x: x[1])
        return [x[0] for x in merged[:K]]