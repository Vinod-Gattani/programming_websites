from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph = {}
        
        for (x, y), v in zip(equations, values):
            if x in graph:
                graph[x][y] = v
            else:
                graph[x] = {y:v}
            
            if y in graph:
                graph[y][x] = 1/v
            else:
                graph[y] = {x: 1/v}
                
        
        def dfs(s,t):
            if s not in graph:
                return -1
            
            elif s==t:
                return 1

            for node in graph[s]:
                if node==t:
                    return graph[s][node]
                elif node in visited:
                    pass
                else:
                    visited.add(node)
                    v = dfs(node, t)

                    if v != -1:
                        return v*graph[s][node]
            return -1
        
        res = []
        for (s,t) in queries:
            visited = set()
            res.append(dfs(s,t))
        
        return res
    
if __name__ == "__main__":
    equations = [["a","b"],["b","c"]]
    values = [2.0,3.0]
    queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
    
    print(Solution().calcEquation(equations, values, queries))
    print(f"Correct Answer is: [6.0, 0.5, -1.0, 1.0, -1.0 ]")
