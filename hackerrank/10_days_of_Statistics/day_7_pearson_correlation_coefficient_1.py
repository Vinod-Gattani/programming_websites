# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys
import math


def mean_std(*args):

    obs = args[0]
    n_obs = args[1]

    sum_x_sq = 0
    sum_x = 0

    for i in obs:
        sum_x += i
        sum_x_sq += i*i
    
    mean = sum_x/n_obs
    variance = sum_x_sq/n_obs - (sum_x/n_obs)**2

    std = math.sqrt(variance)

    return mean, std

def correlation(*args):
    X = args[0]
    Y = args[1]
    n_obs = args[2]

    mean_x, std_x = mean_std(X, n_obs)
    mean_y, std_y = mean_std(Y, n_obs)

    nr = 0

    for x, y in zip(X, Y):

        nr += (x-mean_x)*(y-mean_y)
    
    dr = n_obs*std_x*std_y

    result = nr/dr

    return result

if __name__ == "__main__":
    lines = iter(sys.stdin)
    total_obs = int(next(lines))
    X = list(map(float, next(lines).split()))
    Y = list(map(float, next(lines).split()))

    result = correlation(X, Y, total_obs)

    print(round(result, 3))