

# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

lines = iter(sys.stdin)

mean_a, mean_b = map(float, next(lines).split())

cost_a = lambda x: 160 + 40*(x + x**2)
cost_b = lambda x: 128 + 40*(x + x**2)

print(round(cost_a(mean_a),3))
print(round(cost_b(mean_b),3))
