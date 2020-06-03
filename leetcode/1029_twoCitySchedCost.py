from typing import List

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        costs = sorted(costs, key= lambda x: abs(x[0]-x[1]), reverse=True)
        
        city_a = 0
        city_b = 0
        total_cost = 0
        num = len(costs) // 2
        
        for cost in costs:
            cost_a = cost[0]
            cost_b = cost[1]
            
            if cost_a < cost_b and city_a < num:
                total_cost += cost_a
                city_a += 1
            elif city_b < num or city_a >= num:
                total_cost += cost_b
                city_b += 1
            else:
                total_cost += cost_a
                city_a += 1
                
        return total_cost