# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
from itertools import product

lines = iter(sys.stdin)

K, M = list(map(int, next(lines).split()))

values = dict()

data = [map(int, next(lines).split()[1:]) for i in range(K)]

F = lambda x: x**2
S = lambda x: sum(map(F, x)) % M

print(max(map(S, product(*data))))