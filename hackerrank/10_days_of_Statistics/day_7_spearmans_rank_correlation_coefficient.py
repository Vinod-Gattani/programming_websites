# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

def get_rank(X):
    
    indices = list(range(len(X)))
    indices.sort(key=lambda x: X[x])
    rank = [0] * len(indices)
    for i, x in enumerate(indices):
        rank[x] = i
    
    return rank

def correlation(*args):
    X = args[0]
    Y = args[1]
    n_obs = args[2]

    r_X = get_rank(X)
    r_Y = get_rank(Y)

    nr = 0

    for x, y in zip(r_X, r_Y):
        nr += (x-y)**2

    dr = n_obs*(n_obs**2 - 1)

    result = 1 - (6*nr)/dr

    return result


if __name__ == "__main__":
    lines = iter(sys.stdin)
    total_obs = int(next(lines))
    X = list(map(float, next(lines).split()))
    Y = list(map(float, next(lines).split()))

    result = correlation(X, Y, total_obs)

    print(round(result, 3))