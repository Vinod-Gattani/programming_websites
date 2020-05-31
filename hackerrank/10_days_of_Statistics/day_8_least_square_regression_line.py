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

def reg_coefficients(*args):

    X = args[0]
    Y = args[1]
    n_obs = len(X)

    mean_x, std_x = mean_std(X, n_obs)
    mean_y, std_y = mean_std(Y, n_obs)

    corr = correlation(X, Y, n_obs)

    b = corr*(std_y/std_x)

    a = mean_y - b*mean_x

    return b, a

if __name__ == "__main__":
    lines = iter(sys.stdin)
    X = []
    Y = []

    for i in range(5):
        x, y = map(int, next(lines).split())
        X.append(x)
        Y.append(y)
    
    b, a = reg_coefficients(X, Y)

    result = a + b*80

    print(round(result, 3))