# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys
import numpy as np

lines = iter(sys.stdin)

m, n = map(int, next(lines).split())

X = []
Y = []

for i in range(n):
    values = list(map(float, next(lines).split()))

    X.append(values[:-1])
    Y.append(values[-1])

X = np.array(X)
X = np.hstack((np.ones(shape=(n,1)),X))
Y = np.array(Y)

b = np.linalg.inv(np.dot(X.transpose(), X))
a = np.dot(Y, X)
beta = np.dot(a, b)

q = int(next(lines))

constant = beta[0]

for i in range(q):
    values = list(map(float, next(lines).split()))
    
    result = constant
    for i, j in zip(beta[1:], values):
        result += i*j
    
    print(round(result,2))
    